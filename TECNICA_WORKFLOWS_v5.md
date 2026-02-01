# 👨‍💻 Documentação Técnica - Workflow Profissional v5.0

## 🏗️ Arquitetura da Plataforma

### Camadas de Implementação

```
┌─────────────────────────────────────────────────┐
│          LAYER 1: APRESENTAÇÃO (UI)             │
│  ├─ Sidebar: Gerenciamento de Projetos         │
│  ├─ Tabs: 7 abas de cálculo                    │
│  └─ Componentes: Streamlit widgets             │
├─────────────────────────────────────────────────┤
│     LAYER 2: LÓGICA DE NEGÓCIO (Functions)     │
│  ├─ dimensionar_condutor()                     │
│  ├─ dimensionar_transformador()                │
│  ├─ dimensionar_disjuntor()                    │
│  └─ calcular_curto_circuito()                  │
├─────────────────────────────────────────────────┤
│     LAYER 3: DADOS (Tables & State)            │
│  ├─ Tabelas NBR 5410 (condutores)              │
│  ├─ Tabelas NBR 5356 (transformadores)         │
│  ├─ Session State (projetos, histórico)        │
│  └─ Histórico de cálculos                      │
├─────────────────────────────────────────────────┤
│    LAYER 4: EXPORTAÇÃO (Reports & Formats)     │
│  ├─ Excel (openpyxl)                           │
│  ├─ Texto (gerar_relatorio)                    │
│  └─ Visualização (Matplotlib)                  │
└─────────────────────────────────────────────────┘
```

---

## 📊 Estrutura de Dados - Session State

### Inicialização (linhas ~1175-1180)

```python
if 'projetos' not in st.session_state:
    st.session_state.projetos = {}
if 'projeto_atual' not in st.session_state:
    st.session_state.projeto_atual = None
if 'historico_calculos' not in st.session_state:
    st.session_state.historico_calculos = []
```

### Estrutura de Projeto

```python
st.session_state.projetos = {
    'Nome Projeto A': {
        'nome': str,           # Nome do projeto
        'cliente': str,        # Cliente
        'local': str,          # Localização
        'data_criacao': str,   # Timestamp criação
        'modulos': {
            'condutores': [    # Lista de cálculos de condutores
                {
                    'circuito': 'Iluminação Corredor',
                    'num_circuito': 1,
                    'resultado': {},        # Retorno da função
                    'parametros': {},       # Parâmetros inseridos
                    'timestamp': '15/12/2024 10:35'
                }
            ],
            'transformadores': [],  # Similar à acima
            'disjuntores': [],      # Similar à acima
            'curto_circuito': []    # Similar à acima
        }
    },
    'Nome Projeto B': { ... }
}
```

### Estrutura de Histórico

```python
st.session_state.historico_calculos = [
    {
        'tipo': 'Condutor',                # Tipo de cálculo
        'circuito': 'Iluminação Corredor', # Identificador
        'secao': '2.5 mm²',                # Resultado principal
        'corrente': 15.0,                  # Parâmetro
        'queda': '2.1%',                   # Métrica
        'conforme': 'Sim',                 # Status
        'timestamp': '15/12/2024 10:35'    # Quando foi
    },
    # ... 100+ mais registros
]
```

---

## 🎯 Padrão de Implementação - Cada Aba

### Template Genérico (Estrutura)

```python
# ABA X: MÓDULO (WORKFLOW PROFISSIONAL)
with tabX:
    st.header("🔋 Título do Módulo (Norma)")
    st.markdown("**Objetivo:** Descrição")
    
    if not st.session_state.projeto_atual:
        st.warning("⚠️ Selecione projeto na sidebar")
    else:
        # SEÇÃO 1: IDENTIFICAÇÃO
        st.subheader("📍 1. Identificação")
        col1, col2, col3, col4 = st.columns(4)
        # Campos de entrada para identificar o item
        
        # SEÇÃO 2-3: PARÂMETROS E OPÇÕES
        st.subheader("⚡ 2. Parâmetros")
        # Campos técnicos de entrada
        
        st.subheader("🔧 3. Opções de Projeto")
        # Campos adicionais de projeto
        
        # SEÇÃO 4: PROCESSAMENTO
        st.divider()
        col1, col2, col3 = st.columns([2, 2, 1])
        
        with col1:
            btn_calcular = st.button(\"🔄 Calcular\", use_container_width=True)
        with col2:
            btn_salvar = st.button(\"💾 Salvar\", use_container_width=True)
        
        if btn_calcular:
            # Chamada da função de cálculo
            resultado = funcao_calculo(param1, param2, ...)
            
            # Armazenar em session_state
            st.session_state['resultado_modulo'] = {
                'identificacao': campo_identificacao,
                'resultado': resultado,
                'parametros': {...},
                'timestamp': datetime.now().strftime(...)
            }
            
            st.divider()
            
            # SEÇÃO 5: RESULTADO
            st.subheader(\"📊 5. Resultado\")
            
            # Status geral
            if resultado['conforme']:
                st.success(\"✅ CONFORME\")
            else:
                st.error(\"❌ NÃO CONFORME\")
            
            # Métricas
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric(\"Métrica 1\", f\"{valor1:.2f}\")
            # ... mais métricas
            
            # Alertas
            if resultado['alertas']:
                for alerta in resultado['alertas']:
                    st.warning(f\"• {alerta}\")
            
            # SEÇÃO 6: ANÁLISE COMPARATIVA (opcional)
            st.subheader(\"📊 6. Análise Comparativa\")
            # DataFrame com opções
            df = pd.DataFrame(dados)
            st.dataframe(df, use_container_width=True)
            
            # SEÇÃO 7: EXPORTAÇÃO
            st.subheader(\"📥 7. Exportar\")
            col1, col2, col3 = st.columns(3)
            
            with col1:
                excel_file = exportar_excel(resultado, ...)
                st.download_button(\"📊 Excel\", ...)
            
            with col2:
                relatorio = gerar_relatorio(resultado, ...)
                st.download_button(\"📄 Relatório\", ...)
            
            with col3:
                if st.button(\"👁️ Visualizar\"):
                    st.text(relatorio)
            
            # Adicionar ao histórico
            st.session_state.historico_calculos.append({
                'tipo': 'Nome Módulo',
                'identificacao': campo_identificacao,
                # ... mais campos
                'timestamp': datetime.now().strftime(...)
            })
        
        if btn_salvar:
            if 'resultado_modulo' in st.session_state:
                projeto = st.session_state.projetos[
                    st.session_state.projeto_atual
                ]
                if 'modulo_nome' not in projeto['modulos']:
                    projeto['modulos']['modulo_nome'] = []
                
                projeto['modulos']['modulo_nome'].append(
                    st.session_state['resultado_modulo']
                )
                st.success(\"✅ Salvo no projeto!\")
            else:
                st.warning(\"⚠️ Execute o cálculo primeiro\")
```

---

## 🔧 Implementações Específicas

### Aba 1: Condutores (linhas ~1253-1448)

**Função Principal:** `dimensionar_condutor()`
**Entrada:** 8 parâmetros (corrente, comprimento, etc.)
**Saída:** Dict com 10+ chaves (seção, queda, conforme, etc.)

**Workflow Específico:**
- Ajusta para tipo de instalação (Tabela 33)
- Busca ampacidade em Tabela 36
- Aplica fator de agrupamento (Tabela 42)
- Calcula queda de tensão real

**Histório Registra:**
```python
{
    'tipo': 'Condutor',
    'circuito': nome_circuito,
    'secao': f\"{resultado_cond['secao_selecionada']} mm²\",
    'corrente': corrente_circuito,
    'queda': f\"{resultado_cond['queda_tensao_real']:.2f}%\",
    'conforme': 'Sim' if resultado_cond['conforme'] else 'Não',
    'timestamp': datetime.now().strftime(...)
}
```

---

### Aba 2: Transformadores (linhas ~1540-1766)

**Função Principal:** `dimensionar_transformador()`
**Entrada:** 5 parâmetros (kW, tensões, fator demanda, margem)
**Saída:** Dict com 6+ chaves (kva_selecionado, correntes, conforme, etc.)

**Novidade:** Tabela Comparativa com 5 opções de kVA

```python
opcoes_kva = [10, 15, 20, 25, 30, 37.5, 45, 50, 75, 100, 150, 200]
opcoes_selecionadas = [
    kva for kva in opcoes_kva 
    if kva >= resultado_trafo['potencia_projeto']
][:5]  # Pega as 5 menores opções viáveis

# Cria tabela comparativa
dados_comparacao = []
for kva_opt in opcoes_selecionadas:
    pot_disponivel = kva_opt * 0.9
    margem = ((pot_disponivel - resultado_trafo['potencia_demanda']) 
              / pot_disponivel * 100)
    # ... mais dados
    
df_comparacao = pd.DataFrame(dados_comparacao)
st.dataframe(df_comparacao, ...)
```

---

### Aba 3: Disjuntores (linhas ~1768-2000)

**Função Principal:** `dimensionar_disjuntor()`
**Entrada:** 3 parâmetros (corrente, tipo circuito, padrão)
**Saída:** Dict com 5+ chaves (corrente_nominal, padrão, conforme, etc.)

**Novidade 1:** Seletividade com corrente montante

```python
if usar_selectividade:
    # Verifica se corrente nominal deixa margem
    # para protetor montante atuar primeiro
    margem_minima = 0.5  # 50% de diferença
    
    if (corrente_upstream / resultado_disj['corrente_nominal']) >= (1 + margem_minima):
        # Seletividade garantida ✅
```

**Novidade 2:** Capacidade de ruptura

```python
# Verifica se o disjuntor aguenta a corrente de falta
if capacidade_ruptura >= (corrente_falta / 1000):
    # Capacidade adequada ✅
```

---

### Aba 4: Curto-Circuito (linhas ~2002-2250)

**Função Principal:** `calcular_curto_circuito()`
**Entrada:** 8 parâmetros (kVA, impedâncias, comprimento, seção, etc.)
**Saída:** Dict com Ik secundário e Ik no ponto

**Novidade 1:** Ajuste de Temperatura

```python
if material_cabo == \"Cobre\":
    rho_base = 0.0172
else:
    rho_base = 0.0282

# Resistividade ajustada por temperatura
rho_cable = rho_base * (1 + 0.00393 * (temperatura_cabo - 20))
```

**Novidade 2:** Análise de Sensibilidade com 3 cenários

```python
# Cenário 1: Uk reduzido 20% (nominal)
resultado_uk_menor = calcular_curto_circuito(
    uk_percent=uk_percent * 0.8,
    ...
)

# Cenário 2: À origem (pior caso)
resultado_origem = calcular_curto_circuito(
    comprimento_cabo=0,
    ...
)

# Cenário 3: 100m (típico)
resultado_100m = calcular_curto_circuito(
    comprimento_cabo=100,
    ...
)

# Monta tabela comparativa
cenarios = [
    {'Cenário': 'Nominal', 'Ik': f\"{resultado_uk_menor['ik_ponto']:.2f}\", ...},
    {'Cenário': 'Pior Caso', 'Ik': f\"{resultado_origem['ik_ponto']:.2f}\", ...},
    {'Cenário': 'Melhor Caso', 'Ik': f\"{resultado_100m['ik_ponto']:.2f}\", ...}
]
```

---

## 🔌 Integração com Projeto

### Salvar Cálculo no Projeto

```python
if btn_salvar:
    if 'resultado_modulo' in st.session_state:
        # Obtém projeto ativo
        projeto = st.session_state.projetos[
            st.session_state.projeto_atual
        ]
        
        # Inicializa lista se não existir
        if 'modulo_nome' not in projeto['modulos']:
            projeto['modulos']['modulo_nome'] = []
        
        # Adiciona cálculo
        projeto['modulos']['modulo_nome'].append(
            st.session_state['resultado_modulo']
        )
        
        st.success(\"✅ Salvo!\")
    else:
        st.warning(\"⚠️ Execute cálculo primeiro\")
```

### Adicionar ao Histórico

```python
st.session_state.historico_calculos.append({
    'tipo': 'Condutor',
    'circuito': nome_circuito,
    'secao': f\"{resultado_cond['secao_selecionada']} mm²\",
    'corrente': corrente_circuito,
    'queda': f\"{resultado_cond['queda_tensao_real']:.2f}%\",
    'conforme': 'Sim' if resultado_cond['conforme'] else 'Não',
    'timestamp': datetime.now().strftime(\"%d/%m/%Y %H:%M:%S\")
})
```

---

## 📦 Funções de Utilidade

### Exportar Excel (existente)

```python
def exportar_excel(resultado, tipo='condutor', **kwargs):
    # Recebe resultado do cálculo e parâmetros
    # Retorna BytesIO com arquivo .xlsx formatado
    
    # Estrutura:
    # - Aba 1: Resultado Principal
    # - Aba 2: Parâmetros de Entrada
    # - Aba 3: Cálculos Intermediários
```

### Gerar Relatório (existente)

```python
def gerar_relatorio(resultado, tipo='condutor', **kwargs):
    # Recebe resultado do cálculo
    # Retorna string formatada com relatório completo
    
    # Inclui:
    # - Título e data
    # - Resumo técnico
    # - Tabelas de resultados
    # - Conformidade NBR
    # - Recomendações
```

---

## 🚀 Como Estender a Plataforma

### Adicionar Nova Aba (Ex: Fio de Aterramento)

1. **Criar função de cálculo:**

```python
def dimensionar_aterramento(resistencia_solo, profundidade, **kwargs):
    \"\"\"Calcula resistência de aterramento\"\"\"
    # Implementação
    return {
        'resistencia_aterramento': valor,
        'conforme': bool,
        'alertas': [],
        # ... mais campos
    }
```

2. **Adicionar Tab:**

```python
tab8 = st.tabs([..., \"⚡ Aterramento\"])

# Usar padrão estabelecido
with tab8:
    st.header(\"Dimensionamento de Aterramento\")
    # ... seguir padrão de workflow
```

3. **Integrar com Projeto:**

```python
if 'aterramentos' not in projeto['modulos']:
    projeto['modulos']['aterramentos'] = []
```

---

## 📊 Performance e Otimizações

### Session State - Minimizar Recálculos

```python
# ✅ BOM: Armazena resultado
if btn_calcular:
    resultado = funcao_calculo(...)
    st.session_state['resultado'] = resultado

# ❌ RUIM: Recalcula a cada renderização
resultado = funcao_calculo(...)  # Sem cache!
```

### Usar @st.cache_data para Dados Estáticos

```python
@st.cache_data
def carregar_tabelas_nbr():
    # Tabelas carregadas uma única vez
    return {
        'tabela_36_cobre': {...},
        'tabela_36_aluminio': {...}
    }
```

### Limpar Session State Periodicamente

```python
if st.button(\"🗑️ Limpar Sessão\"):
    st.session_state.clear()
    st.rerun()
```

---

## 🧪 Validação e Testes

### Verificação de Conformidade

Cada função retorna campo `'conforme': bool` baseado em:

**Aba 1 (Condutores):**
- ✅ Queda de tensão < limite (3% típico)
- ✅ Ampacidade > corrente de circuito
- ✅ Material e instalação válidos

**Aba 2 (Transformadores):**
- ✅ kVA selecionado ≥ demanda com margem
- ✅ Correntes dentro de limites
- ✅ Relação de transformação válida

**Aba 3 (Disjuntores):**
- ✅ Corrente nominal ≥ corrente de circuito
- ✅ Capacidade de ruptura ≥ falta prevista
- ✅ Padrão apropriado para tipo de carga

**Aba 4 (Curto-Circuito):**
- ✅ Cálculo de impedância coerente
- ✅ Corrente de falta calculada > 0
- ✅ Cenários de sensibilidade válidos

---

## 📈 Próximas Expansões Recomendadas

### Phase 6 (Curto Prazo)
- [ ] Persistência em banco de dados (SQLite/PostgreSQL)
- [ ] Autenticação de usuários
- [ ] Compartilhamento de projetos em equipe

### Phase 7 (Médio Prazo)
- [ ] API REST para integração
- [ ] Mobile app (React Native)
- [ ] Desktop app (Electron)
- [ ] Integração com CAD (AutoCAD/Revit)

### Phase 8 (Longo Prazo)
- [ ] Módulo de custeamento
- [ ] Integração com fornecedores
- [ ] IA para otimizações
- [ ] Conformidade ISO 50001/ISO 55000

---

## 🔍 Debugging e Troubleshooting

### Problema: Session state não persiste entre abas

**Solução:**
```python
# ✅ CORRETO
if 'resultado_condutor' in st.session_state:
    resultado = st.session_state['resultado_condutor']

# ❌ ERRADO
resultado = resultado_condutor  # Variável local perdida
```

### Problema: Botão não responde

**Solução:**
```python
# Verifique se btn_calcular está dentro do if:
if st.button(\"Calcular\"):  # ✅
    resultado = funcao()
    st.session_state['resultado'] = resultado
    st.divider()  # DEPOIS do cálculo
    st.metric(\"Resultado\", resultado['valor'])
```

### Problema: Dados do projeto desaparecem ao recarregar

**Causa:** Session state é perdida ao fechar o navegador  
**Solução:** Implementar persistência em DB (Phase 6)

---

## 📚 Referências de Código

### Linhas Principais do Arquivo app.py

| Seção | Linhas | Descrição |
|-------|--------|-----------|
| Imports | 1-25 | Bibliotecas necessárias |
| Session Init | 1175-1180 | Inicialização de projetos |
| Sidebar | 1182-1231 | Gerenciamento de projetos |
| Aba 1 | 1253-1448 | Condutores profissional |
| Aba 2 | 1540-1766 | Transformadores profissional |
| Aba 3 | 1768-2000 | Disjuntores profissional |
| Aba 4 | 2002-2250 | Curto-circuito profissional |
| Aba 5+ | 2252+ | Balanceamento, Unifilar, SPDA |

---

## ✅ Checklist de Implementação

- [x] Session State Management
- [x] Sidebar com Gerenciamento de Projetos
- [x] Aba 1 Workflow Profissional
- [x] Aba 2 Workflow Profissional
- [x] Aba 3 Workflow Profissional
- [x] Aba 4 Workflow Profissional
- [x] Histórico de Cálculos
- [x] Exportação (Excel/TXT)
- [x] Tabelas Comparativas
- [x] Análise de Sensibilidade
- [x] Validação de Conformidade
- [ ] Persistência em BD
- [ ] Autenticação
- [ ] API REST
- [ ] Mobile App

---

**Documentação Técnica v5.0**  
**Versão:** 1.0  
**Data:** Dezembro 2024  
**Status:** ✅ Completa

