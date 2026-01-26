import streamlit as st
import numpy as np
import pandas as pd
from datetime import datetime
from io import BytesIO
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

# Configuração página
st.set_page_config(
    page_title="Software Projetos Elétricos",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizado
st.markdown("""
<style>
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
        font-size: 1.1rem;
        font-weight: 500;
    }
    .metric-box {
        background-color: #f0f2f6;
        padding: 15px;
        border-radius: 5px;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# ============ TABELAS E DADOS ============

ampacidade_cu = {
    1.5: 17.5, 2.5: 24, 4: 32, 6: 41, 10: 57, 16: 76, 25: 99,
    35: 125, 50: 155, 70: 194, 95: 232, 120: 263, 150: 295,
    185: 327, 240: 369
}

secoes_minimas = {
    'Iluminacao': 1.5,
    'Tomada_residencial': 2.5,
    'Tomada_forcados': 6,
    'Corrente_continua': 6
}

tamanhos_padrao_kva = [10, 15, 25, 30, 45, 50, 75, 100, 150, 200, 300, 500, 750, 1000]

# ============ FUNÇÕES DE CÁLCULO ============

def dimensionar_transformador(potencia_total_kw, tensao_primaria=13800, tensao_secundaria=380, 
                              fator_demanda=0.8, margem_crescimento=0.2):
    """
    Dimensiona transformador conforme NBR 5356.
    """
    alertas = []
    
    potencia_demanda = potencia_total_kw * fator_demanda
    potencia_projeto = potencia_demanda * (1 + margem_crescimento)
    potencia_kva = potencia_projeto / 0.92  # Considerando FP=0.92
    
    # Encontrar tamanho padrão
    kva_selecionado = next((kva for kva in tamanhos_padrao_kva if kva >= potencia_kva), None)
    
    if kva_selecionado is None:
        alertas.append("Potência fora da faixa padrão. Consulte fabricante.")
        kva_selecionado = potencia_kva
    
    corrente_primaria = (kva_selecionado * 1000) / (tensao_primaria * np.sqrt(3))
    corrente_secundaria = (kva_selecionado * 1000) / (tensao_secundaria * np.sqrt(3))
    
    return {
        "potencia_demanda": round(potencia_demanda, 2),
        "potencia_projeto": round(potencia_projeto, 2),
        "kva_selecionado": kva_selecionado,
        "corrente_primaria": round(corrente_primaria, 2),
        "corrente_secundaria": round(corrente_secundaria, 2),
        "conforme": len(alertas) == 0,
        "alertas": alertas
    }


def dimensionar_condutor(corrente_circuito, comprimento_circuito=30, queda_tensao_max=3.0, 
                         tensao_nominal=380, tipo_instalacao='cond_visivel', material='cobre'):
    """
    Dimensiona condutor conforme NBR 5410 (critério de queda de tensão).
    """
    alertas = []
    
    # Fator de comprimento reduzido
    comprimento_reduzido = 2 * comprimento_circuito
    
    # Resistividade (Ω·mm²/m)
    rho = 0.0175 if material == 'cobre' else 0.029
    
    # Queda de tensão máxima em V
    delta_u_max = (queda_tensao_max / 100) * tensao_nominal
    
    # Cálculo: U = R*I*L => S = rho*L*I / (delta_u)
    secao_minima = (rho * comprimento_reduzido * corrente_circuito) / delta_u_max
    
    # Tabelas simplificadas por instalação
    secoes_disponiveis = [1.5, 2.5, 4, 6, 10, 16, 25, 35, 50, 70, 95, 120, 150, 185, 240]
    secao_selecionada = next((s for s in secoes_disponiveis if s >= secao_minima), None)
    
    if secao_selecionada is None:
        alertas.append("Seção calculada muito grande. Verifique parâmetros.")
        secao_selecionada = secoes_disponiveis[-1]
    
    # Verificar ampacidade
    ampacidade = ampacidade_cu.get(secao_selecionada, 0)
    if corrente_circuito > ampacidade:
        alertas.append(f"Corrente {corrente_circuito}A > Ampacidade {ampacidade}A. Aumentar seção.")
    
    # Queda de tensão real
    r_real = (rho * comprimento_reduzido) / secao_selecionada
    queda_real = (r_real * corrente_circuito * 100) / tensao_nominal
    
    if queda_real > queda_tensao_max:
        alertas.append(f"Queda {queda_real:.2f}% > máximo {queda_tensao_max}%. Aumentar seção.")
    
    return {
        "secao_minima_calculada": round(secao_minima, 2),
        "secao_selecionada": secao_selecionada,
        "ampacidade": ampacidade,
        "queda_tensao_real": round(queda_real, 2),
        "conforme": len(alertas) == 0,
        "alertas": alertas
    }


def dimensionar_disjuntor(corrente_circuito, tipo_circuito='geral', padrao='c'):
    """
    Seleciona disjuntor conforme corrente do circuito e padrão.
    """
    alertas = []
    
    # Tamanhos padrão (A)
    tamanhos_c = [2, 6, 10, 16, 20, 25, 32, 40, 50, 63, 80, 100, 125, 160, 200, 250, 400]
    tamanhos_b = [2, 6, 10, 16, 20, 25, 32, 40, 50, 63, 80, 100, 125, 160, 200]
    tamanhos_d = [2, 6, 10, 16, 20, 25, 32, 40, 50, 63, 80, 100, 125, 160, 200, 250, 400]
    
    tamanhos = tamanhos_c if padrao == 'c' else (tamanhos_b if padrao == 'b' else tamanhos_d)
    
    # Seleção: primeiro que cumpre Iz >= In
    corrente_nominal = next((t for t in tamanhos if t >= corrente_circuito), None)
    
    if corrente_nominal is None:
        alertas.append(f"Corrente {corrente_circuito}A fora da faixa disponível.")
        corrente_nominal = tamanhos[-1]
    
    # Verificação de proteção (In <= Iz)
    if corrente_nominal > corrente_circuito * 1.25:
        alertas.append(f"In {corrente_nominal}A > 1.25*Iz {corrente_circuito*1.25:.1f}A. Verificar seleção.")
    
    return {
        "corrente_nominal": corrente_nominal,
        "padrao": padrao.upper(),
        "tipo": tipo_circuito,
        "conforme": len(alertas) == 0,
        "alertas": alertas
    }


def calcular_curto_circuito(kva_transformador, tensao_secundaria=380, uk_percent=5.0, comprimento_cabo=0, 
                           secao_cabo=0, rho_cabo=0.023, x_cabo_unit=0.00008, tipo_curto='trifasico'):
    """
    Calcula corrente de curto-circuito conforme IEC 60909/NBR 5410.
    """
    import unicodedata
    alertas = []
    
    # Normalizar tipo_curto removendo acentos
    tipo_curto_norm = unicodedata.normalize('NFKD', tipo_curto.lower()).encode('ASCII', 'ignore').decode('ASCII')
    
    uk = uk_percent / 100
    zk_trafo = (tensao_secundaria ** 2) / (kva_transformador * 1000) * uk
    
    if tipo_curto_norm == 'trifasico':
        ik_sec = (tensao_secundaria / np.sqrt(3)) / zk_trafo / 1000
        fator = 1.0
    elif tipo_curto_norm == 'bifasico':
        ik_sec = (tensao_secundaria / 2) / zk_trafo / 1000
        fator = np.sqrt(3)/2
    elif tipo_curto_norm == 'monofasico':
        ik_sec = tensao_secundaria / zk_trafo / 1000
        fator = 1.5
    else:
        alertas.append("Tipo de curto inválido.")
        return {"alertas": alertas}
    
    ik_ponto = ik_sec
    
    if comprimento_cabo > 0 and secao_cabo > 0:
        r_cabo = (rho_cabo * comprimento_cabo) / secao_cabo
        x_cabo = x_cabo_unit * comprimento_cabo
        z_cabo = np.sqrt(r_cabo**2 + x_cabo**2)
        z_total = np.sqrt(zk_trafo**2 + z_cabo**2)
        ik_ponto = (tensao_secundaria / np.sqrt(3)) / z_total / 1000 * fator
    
    conforme = len(alertas) == 0
    return {
        "ik_secundario": ik_sec,
        "ik_ponto": ik_ponto,
        "conforme": conforme,
        "alertas": alertas
    }


def gerar_relatorio(resultado, tipo='condutor', **kwargs):
    """
    Gera memorial descritivo conforme normas.
    """
    rel = f"{'='*60}\n"
    rel += f"MEMORIAL DESCRITIVO - {tipo.upper()}\n"
    rel += f"Normas: NBR 5410 / NBR 5356 / IEC 60909\n"
    rel += f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M')}\n"
    rel += f"{'='*60}\n\n"
    
    if tipo == 'condutor':
        rel += f"Corrente do Circuito: {kwargs.get('corrente_circuito', 0):.2f} A\n"
        rel += f"Comprimento: {kwargs.get('comprimento_circuito', 0):.1f} m\n"
        rel += f"Queda de Tensão Máxima: {kwargs.get('queda_tensao_max', 3)}%\n\n"
        rel += f"Seção Mínima Calculada: {resultado['secao_minima_calculada']:.2f} mm²\n"
        rel += f"Seção Selecionada: {resultado['secao_selecionada']} mm²\n"
        rel += f"Ampacidade: {resultado['ampacidade']} A\n"
        rel += f"Queda de Tensão Real: {resultado['queda_tensao_real']:.2f}%\n"
        
    elif tipo == 'transformador':
        rel += f"Potência Total: {kwargs.get('potencia_total_kw', 0):.2f} kW\n"
        rel += f"Fator de Demanda: {kwargs.get('fator_demanda', 0.8):.1%}\n"
        rel += f"Margem de Crescimento: {kwargs.get('margem_crescimento', 0.2):.1%}\n\n"
        rel += f"Potência Demanda: {resultado['potencia_demanda']:.2f} kW\n"
        rel += f"Potência Projeto: {resultado['potencia_projeto']:.2f} kW\n"
        rel += f"Transformador Selecionado: {resultado['kva_selecionado']} kVA\n"
        rel += f"Corrente Primária: {resultado['corrente_primaria']:.2f} A\n"
        rel += f"Corrente Secundária: {resultado['corrente_secundaria']:.2f} A\n"
        
    elif tipo == 'disjuntor':
        rel += f"Corrente do Circuito: {kwargs.get('corrente_circuito', 0):.2f} A\n"
        rel += f"Tipo de Circuito: {kwargs.get('tipo_circuito', 'geral')}\n\n"
        rel += f"Padrão Selecionado: {resultado['padrao']}\n"
        rel += f"Corrente Nominal: {resultado['corrente_nominal']} A\n"
        
    elif tipo == 'curto_circuito':
        rel += f"Transformador: {kwargs.get('kva_transformador', 0)} kVA\n"
        rel += f"Tensão Secundária: {kwargs.get('tensao_secundaria', 380)} V\n"
        rel += f"Impedância Uk: {kwargs.get('uk_percent', 5)}%\n"
        rel += f"Tipo de Curto: {kwargs.get('tipo_curto', 'trifásico')}\n\n"
        rel += f"Ik no Secundário: {resultado['ik_secundario']:.2f} kA\n"
        rel += f"Ik no Ponto: {resultado['ik_ponto']:.2f} kA\n"
    
    if resultado.get('alertas', []):
        rel += "\nALERTAS:\n"
        for i, alerta in enumerate(resultado['alertas'], 1):
            rel += f"  {i}. {alerta}\n"
    else:
        rel += "\n✓ Cálculo conforme as normas aplicáveis.\n"
    
    rel += f"\n{'='*60}\n"
    return rel


def exportar_excel(resultado, tipo='condutor', **kwargs):
    """
    Exporta resultado para arquivo Excel com formatação profissional.
    """
    output = BytesIO()
    
    # Criar workbook
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = tipo.capitalize()
    
    # Estilos
    header_fill = PatternFill(start_color="366092", end_color="366092", fill_type="solid")
    header_font = Font(color="FFFFFF", bold=True, size=12)
    title_font = Font(bold=True, size=14, color="366092")
    border = Border(
        left=Side(style='thin'),
        right=Side(style='thin'),
        top=Side(style='thin'),
        bottom=Side(style='thin')
    )
    
    # Título
    ws.merge_cells('A1:D1')
    title = ws['A1']
    title.value = f"Cálculo de {tipo.capitalize()} - NBR 5410/5356"
    title.font = title_font
    
    # Data
    ws.merge_cells('A2:D2')
    date_cell = ws['A2']
    date_cell.value = f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M')}"
    date_cell.font = Font(italic=True, size=10)
    
    row = 4
    
    # ENTRADA
    ws.merge_cells(f'A{row}:D{row}')
    input_header = ws[f'A{row}']
    input_header.value = "PARÂMETROS DE ENTRADA"
    input_header.font = header_font
    input_header.fill = header_fill
    row += 1
    
    if tipo == 'condutor':
        dados_entrada = [
            ['Corrente do Circuito', f"{kwargs.get('corrente_circuito', 0):.2f}", "A"],
            ['Comprimento', f"{kwargs.get('comprimento_circuito', 0):.1f}", "m"],
            ['Queda Tensão Máx.', f"{kwargs.get('queda_tensao_max', 3)}", "%"],
            ['Tensão Nominal', f"{kwargs.get('tensao_nominal', 380):.0f}", "V"],
        ]
    elif tipo == 'transformador':
        dados_entrada = [
            ['Potência Total', f"{kwargs.get('potencia_total_kw', 0):.2f}", "kW"],
            ['Fator Demanda', f"{kwargs.get('fator_demanda', 0.8):.1%}", "-"],
            ['Margem Crescimento', f"{kwargs.get('margem_crescimento', 0.2):.1%}", "-"],
            ['Tensão Primária', f"{kwargs.get('tensao_primaria', 13800):.0f}", "V"],
            ['Tensão Secundária', f"{kwargs.get('tensao_secundaria', 380):.0f}", "V"],
        ]
    elif tipo == 'disjuntor':
        dados_entrada = [
            ['Corrente Circuito', f"{kwargs.get('corrente_circuito', 0):.2f}", "A"],
            ['Tipo Circuito', kwargs.get('tipo_circuito', 'geral'), "-"],
        ]
    elif tipo == 'curto_circuito':
        dados_entrada = [
            ['Potência Trafo', f"{kwargs.get('kva_transformador', 0):.0f}", "kVA"],
            ['Tensão Secundária', f"{kwargs.get('tensao_secundaria', 380):.0f}", "V"],
            ['Impedância Uk', f"{kwargs.get('uk_percent', 5):.1f}", "%"],
            ['Tipo Curto', kwargs.get('tipo_curto', 'trifásico'), "-"],
        ]
    
    for param, valor, unidade in dados_entrada:
        ws[f'A{row}'] = param
        ws[f'B{row}'] = valor
        ws[f'C{row}'] = unidade
        for col in ['A', 'B', 'C']:
            ws[f'{col}{row}'].border = border
            ws[f'{col}{row}'].alignment = Alignment(horizontal='left')
        row += 1
    
    row += 1
    
    # RESULTADOS
    ws.merge_cells(f'A{row}:D{row}')
    output_header = ws[f'A{row}']
    output_header.value = "RESULTADOS"
    output_header.font = header_font
    output_header.fill = header_fill
    row += 1
    
    if tipo == 'condutor':
        dados_saida = [
            ['Seção Mínima Calculada', f"{resultado['secao_minima_calculada']:.2f}", "mm²"],
            ['Seção Selecionada', f"{resultado['secao_selecionada']}", "mm²"],
            ['Ampacidade', f"{resultado['ampacidade']}", "A"],
            ['Queda Tensão Real', f"{resultado['queda_tensao_real']:.2f}", "%"],
            ['Conforme NBR 5410', "SIM" if resultado['conforme'] else "NÃO", ""],
        ]
    elif tipo == 'transformador':
        dados_saida = [
            ['Potência Demanda', f"{resultado['potencia_demanda']:.2f}", "kW"],
            ['Potência Projeto', f"{resultado['potencia_projeto']:.2f}", "kW"],
            ['Transformador', f"{resultado['kva_selecionado']}", "kVA"],
            ['Corrente Primária', f"{resultado['corrente_primaria']:.2f}", "A"],
            ['Corrente Secundária', f"{resultado['corrente_secundaria']:.2f}", "A"],
            ['Conforme NBR 5356', "SIM" if resultado['conforme'] else "NÃO", ""],
        ]
    elif tipo == 'disjuntor':
        dados_saida = [
            ['Padrão', resultado['padrao'], ""],
            ['Corrente Nominal', f"{resultado['corrente_nominal']}", "A"],
            ['Tipo', resultado['tipo'].title(), ""],
            ['Conforme', "SIM" if resultado['conforme'] else "NÃO", ""],
        ]
    elif tipo == 'curto_circuito':
        dados_saida = [
            ['Ik Secundário', f"{resultado['ik_secundario']:.2f}", "kA"],
            ['Ik no Ponto', f"{resultado['ik_ponto']:.2f}", "kA"],
            ['Conforme IEC 60909', "SIM" if resultado['conforme'] else "NÃO", ""],
        ]
    
    for param, valor, unidade in dados_saida:
        ws[f'A{row}'] = param
        ws[f'B{row}'] = valor
        ws[f'C{row}'] = unidade
        for col in ['A', 'B', 'C']:
            cell = ws[f'{col}{row}']
            cell.border = border
            cell.alignment = Alignment(horizontal='left')
            if 'Conforme' in param:
                cell.font = Font(bold=True)
        row += 1
    
    # Alertas
    if resultado.get('alertas', []):
        row += 1
        ws.merge_cells(f'A{row}:D{row}')
        alert_header = ws[f'A{row}']
        alert_header.value = "ALERTAS"
        alert_header.font = Font(color="FFFFFF", bold=True, size=11)
        alert_header.fill = PatternFill(start_color="C00000", end_color="C00000", fill_type="solid")
        row += 1
        
        for i, alerta in enumerate(resultado['alertas'], 1):
            ws.merge_cells(f'A{row}:D{row}')
            alert_cell = ws[f'A{row}']
            alert_cell.value = f"{i}. {alerta}"
            alert_cell.font = Font(color="C00000")
            alert_cell.border = border
            row += 1
    
    # Ajustar largura das colunas
    ws.column_dimensions['A'].width = 30
    ws.column_dimensions['B'].width = 15
    ws.column_dimensions['C'].width = 10
    ws.column_dimensions['D'].width = 10
    
    wb.save(output)
    output.seek(0)
    return output


# ============ INTERFACE STREAMLIT ============

st.title("⚡ Software para Projetos Elétricos")
st.markdown("**Dimensionamento conforme NBR 5410 / NBR 5356 / IEC 60909**")

tab1, tab2, tab3, tab4 = st.tabs([
    "📦 Condutores", 
    "🔋 Transformadores", 
    "⚙️ Disjuntores",
    "⚡ Curto-Circuito"
])

# ============ ABA 1: CONDUTORES ============
with tab1:
    st.header("Dimensionamento de Condutores")
    st.markdown("Critério: Queda de tensão máxima (NBR 5410)")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        corrente_circuito = st.number_input("Corrente do Circuito (A)", min_value=0.1, value=20.0, step=0.5, key="cond_corrente")
        comprimento_circuito = st.number_input("Comprimento Circuito (m)", min_value=0.0, value=30.0, step=5.0, key="cond_comprimento")
    with col2:
        queda_tensao_max = st.number_input("Queda de Tensão Máx. (%)", min_value=0.1, value=3.0, step=0.5, key="cond_queda")
        tensao_nominal = st.number_input("Tensão Nominal (V)", min_value=127.0, value=380.0, step=127.0, key="cond_tensao")
    with col3:
        material = st.selectbox("Material do Condutor", ["Cobre", "Alumínio"], key="cond_material")
        tipo_instalacao = st.selectbox("Tipo de Instalação", ["Condutor Visível", "Em Eletroduto", "Enterrado"], key="cond_instalacao")
    
    if st.button("Calcular Dimensionamento", key="btn_condutor"):
        resultado_cond = dimensionar_condutor(
            corrente_circuito=corrente_circuito,
            comprimento_circuito=comprimento_circuito,
            queda_tensao_max=queda_tensao_max,
            tensao_nominal=tensao_nominal,
            material=material.lower()
        )
        
        st.divider()
        
        # Resultados
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Seção Mínima", f"{resultado_cond['secao_minima_calculada']:.2f} mm²")
        with col2:
            st.metric("Seção Selecionada", f"{resultado_cond['secao_selecionada']} mm²")
        with col3:
            st.metric("Ampacidade", f"{resultado_cond['ampacidade']} A")
        
        col1, col2 = st.columns(2)
        with col1:
            if resultado_cond['conforme']:
                st.success("✓ Condutor conforme com as normas!")
            else:
                st.warning("⚠️ Verificar alertas abaixo")
        
        with col2:
            st.metric("Queda Real", f"{resultado_cond['queda_tensao_real']:.2f}%")
        
        if resultado_cond['alertas']:
            st.error("**Alertas:**")
            for alerta in resultado_cond['alertas']:
                st.error(f"  • {alerta}")
        
        # Exportação
        col1, col2 = st.columns(2)
        with col1:
            excel_file = exportar_excel(resultado_cond, tipo='condutor', 
                                       corrente_circuito=corrente_circuito,
                                       comprimento_circuito=comprimento_circuito,
                                       queda_tensao_max=queda_tensao_max,
                                       tensao_nominal=tensao_nominal)
            st.download_button(
                label="📥 Baixar Excel",
                data=excel_file,
                file_name=f"condutor_{datetime.now().strftime('%d%m%Y_%H%M%S')}.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
        
        # Relatório
        with col2:
            relatorio = gerar_relatorio(resultado_cond, tipo='condutor', 
                                       corrente_circuito=corrente_circuito,
                                       comprimento_circuito=comprimento_circuito,
                                       queda_tensao_max=queda_tensao_max)
            st.download_button(
                label="📄 Baixar Relatório",
                data=relatorio,
                file_name=f"condutor_{datetime.now().strftime('%d%m%Y_%H%M%S')}.txt",
                mime="text/plain"
            )
        
        with st.expander("📋 Visualizar Relatório"):
            st.text(relatorio)


# ============ ABA 2: TRANSFORMADORES ============
with tab2:
    st.header("Dimensionamento de Transformadores")
    st.markdown("Seleção conforme potência e margens de segurança (NBR 5356)")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        potencia_total_kw = st.number_input("Potência Total (kW)", min_value=0.5, value=100.0, step=5.0, key="trafo_potencia")
        tensao_primaria = st.number_input("Tensão Primária (V)", min_value=100.0, value=13800.0, step=100.0, key="trafo_primaria")
    with col2:
        tensao_secundaria = st.number_input("Tensão Secundária (V)", min_value=100.0, value=380.0, step=10.0, key="trafo_secundaria")
        fator_demanda = st.slider("Fator de Demanda", 0.5, 1.0, 0.8, 0.05, key="trafo_fator")
    with col3:
        margem_crescimento = st.slider("Margem de Crescimento (%)", 0.0, 50.0, 20.0, 5.0, key="trafo_margem")
        margem_crescimento = margem_crescimento / 100
    
    if st.button("Calcular Transformador", key="btn_trafo"):
        resultado_trafo = dimensionar_transformador(
            potencia_total_kw=potencia_total_kw,
            tensao_primaria=tensao_primaria,
            tensao_secundaria=tensao_secundaria,
            fator_demanda=fator_demanda,
            margem_crescimento=margem_crescimento
        )
        
        st.divider()
        
        # Resultados
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Potência Demanda", f"{resultado_trafo['potencia_demanda']:.2f} kW")
            st.metric("Transformador", f"{resultado_trafo['kva_selecionado']} kVA")
        with col2:
            st.metric("Potência Projeto", f"{resultado_trafo['potencia_projeto']:.2f} kW")
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Corrente Primária", f"{resultado_trafo['corrente_primaria']:.2f} A")
        with col2:
            st.metric("Corrente Secundária", f"{resultado_trafo['corrente_secundaria']:.2f} A")
        
        if resultado_trafo['conforme']:
            st.success("✓ Transformador conforme com as normas!")
        else:
            st.warning("⚠️ Verificar alertas")
        
        if resultado_trafo['alertas']:
            st.error("**Alertas:**")
            for alerta in resultado_trafo['alertas']:
                st.error(f"  • {alerta}")
        
        # Exportação
        col1, col2 = st.columns(2)
        with col1:
            excel_file = exportar_excel(resultado_trafo, tipo='transformador',
                                       potencia_total_kw=potencia_total_kw,
                                       fator_demanda=fator_demanda,
                                       margem_crescimento=margem_crescimento,
                                       tensao_primaria=tensao_primaria,
                                       tensao_secundaria=tensao_secundaria)
            st.download_button(
                label="📥 Baixar Excel",
                data=excel_file,
                file_name=f"transformador_{datetime.now().strftime('%d%m%Y_%H%M%S')}.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
        
        with col2:
            relatorio = gerar_relatorio(resultado_trafo, tipo='transformador',
                                       potencia_total_kw=potencia_total_kw,
                                       fator_demanda=fator_demanda,
                                       margem_crescimento=margem_crescimento)
            st.download_button(
                label="📄 Baixar Relatório",
                data=relatorio,
                file_name=f"transformador_{datetime.now().strftime('%d%m%Y_%H%M%S')}.txt",
                mime="text/plain"
            )
        
        with st.expander("📋 Visualizar Relatório"):
            st.text(relatorio)


# ============ ABA 3: DISJUNTORES ============
with tab3:
    st.header("Seleção de Disjuntores")
    st.markdown("Proteção conforme corrente do circuito")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        corrente_circuito_disj = st.number_input("Corrente do Circuito (A)", min_value=0.1, value=20.0, step=0.5, key="disj_corrente")
    with col2:
        padrao = st.selectbox("Padrão", ["C", "B", "D"], key="disj_padrao")
    with col3:
        tipo_circuito = st.selectbox("Tipo", ["Geral", "Iluminação", "Tomada", "Ar Condicionado"], key="disj_tipo")
    
    if st.button("Selecionar Disjuntor", key="btn_disj"):
        resultado_disj = dimensionar_disjuntor(
            corrente_circuito=corrente_circuito_disj,
            tipo_circuito=tipo_circuito.lower(),
            padrao=padrao.lower()
        )
        
        st.divider()
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Padrão", resultado_disj['padrao'])
        with col2:
            st.metric("Corrente Nominal", f"{resultado_disj['corrente_nominal']} A")
        with col3:
            st.metric("Tipo", resultado_disj['tipo'].title())
        
        if resultado_disj['conforme']:
            st.success("✓ Disjuntor conforme!")
        else:
            st.warning("⚠️ Verificar alertas")
        
        if resultado_disj['alertas']:
            st.error("**Alertas:**")
            for alerta in resultado_disj['alertas']:
                st.error(f"  • {alerta}")
        
        # Exportação
        col1, col2 = st.columns(2)
        with col1:
            excel_file = exportar_excel(resultado_disj, tipo='disjuntor',
                                       corrente_circuito=corrente_circuito_disj,
                                       tipo_circuito=tipo_circuito)
            st.download_button(
                label="📥 Baixar Excel",
                data=excel_file,
                file_name=f"disjuntor_{datetime.now().strftime('%d%m%Y_%H%M%S')}.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
        
        with col2:
            relatorio = gerar_relatorio(resultado_disj, tipo='disjuntor',
                                       corrente_circuito=corrente_circuito_disj,
                                       tipo_circuito=tipo_circuito)
            st.download_button(
                label="📄 Baixar Relatório",
                data=relatorio,
                file_name=f"disjuntor_{datetime.now().strftime('%d%m%Y_%H%M%S')}.txt",
                mime="text/plain"
            )
        
        with st.expander("📋 Visualizar Relatório"):
            st.text(relatorio)


# ============ ABA 4: CURTO-CIRCUITO ============
with tab4:
    st.header("Cálculo de Corrente de Curto-Circuito")
    st.markdown("Conforme IEC 60909 / NBR 5410")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        kva_transformador = st.number_input("Potência Trafo (kVA)", min_value=1.0, value=300.0, step=10.0, key="cc_kva")
        tensao_secundaria = st.number_input("Tensão Sec. (V)", min_value=100.0, value=380.0, step=10.0, key="cc_tensao")
        uk_percent = st.number_input("Impedância Uk (%)", min_value=0.1, value=5.0, step=0.5, key="cc_uk")
    with col2:
        comprimento_cabo = st.number_input("Comprimento Cabo (m)", min_value=0.0, value=0.0, step=5.0, key="cc_comprimento")
        secao_cabo = st.selectbox("Seção Cabo (mm²)", [0, 1.5, 2.5, 4, 6, 10, 16, 25, 35, 50, 70, 95, 120, 150], key="cc_secao")
    with col3:
        rho_cabo = 0.023
        x_cabo_unit = 0.00008
        tipo_curto = st.selectbox("Tipo Curto", ["Trifásico", "Bifásico", "Monofásico"], key="cc_tipo")
    
    if st.button("Calcular Curto-Circuito", key="btn_cc"):
        resultado_cc = calcular_curto_circuito(
            kva_transformador=kva_transformador,
            tensao_secundaria=tensao_secundaria,
            uk_percent=uk_percent,
            comprimento_cabo=comprimento_cabo,
            secao_cabo=secao_cabo,
            rho_cabo=rho_cabo,
            x_cabo_unit=x_cabo_unit,
            tipo_curto=tipo_curto.lower()
        )
        
        st.divider()
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Ik Secundário", f"{resultado_cc['ik_secundario']:.2f} kA")
        with col2:
            st.metric("Ik no Ponto", f"{resultado_cc['ik_ponto']:.2f} kA")
        
        if resultado_cc['conforme']:
            st.success("✓ Cálculo conforme!")
        else:
            st.warning("⚠️ Verificar alertas")
        
        if resultado_cc['alertas']:
            st.error("**Alertas:**")
            for alerta in resultado_cc['alertas']:
                st.error(f"  • {alerta}")
        
        # Exportação
        col1, col2 = st.columns(2)
        with col1:
            excel_file = exportar_excel(resultado_cc, tipo='curto_circuito',
                                       kva_transformador=kva_transformador,
                                       tensao_secundaria=tensao_secundaria,
                                       uk_percent=uk_percent,
                                       tipo_curto=tipo_curto)
            st.download_button(
                label="📥 Baixar Excel",
                data=excel_file,
                file_name=f"curto_circuito_{datetime.now().strftime('%d%m%Y_%H%M%S')}.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
        
        with col2:
            relatorio = gerar_relatorio(resultado_cc, tipo='curto_circuito',
                                       kva_transformador=kva_transformador,
                                       tensao_secundaria=tensao_secundaria,
                                       uk_percent=uk_percent,
                                       tipo_curto=tipo_curto)
            st.download_button(
                label="📄 Baixar Relatório",
                data=relatorio,
                file_name=f"curto_circuito_{datetime.now().strftime('%d%m%Y_%H%M%S')}.txt",
                mime="text/plain"
            )
        
        with st.expander("📋 Visualizar Relatório"):
            st.text(relatorio)


# Footer
st.divider()
st.markdown("""
---
**Software de Projetos Elétricos** | Normas: NBR 5410 • NBR 5356 • IEC 60909
""")
