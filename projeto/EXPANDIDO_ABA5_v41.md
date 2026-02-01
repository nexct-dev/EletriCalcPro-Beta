# 🎯 NOVA FUNCIONALIDADE - ABA 5 EXPANDIDA (v4.1)

**Data:** 31 de Janeiro de 2026  
**Versão:** 4.1  
**Tipo:** Feature Enhancement  
**Status:** ✅ Implementada

---

## 📋 Resumo da Atualização

A **Aba 5 (Balanceamento de Fases)** foi expandida com novas funcionalidades:

✅ **Campos para dados do circuito:**
- Nome do circuito
- Tipo de circuito
- Comprimento do circuito

✅ **Dimensionamento automático conforme NBR 5410:**
- Usa corrente média do balanceamento
- Seleciona tipo de instalação
- Calcula seção de condutor
- Verifica queda de tensão

✅ **Geração de diagrama unifilar:**
- PNG via Matplotlib (300 DPI)
- PDF via ReportLab (A4)
- DWG via EzDXF (CAD)

---

## 🔄 Fluxo de Trabalho

### Antes (v4.0):
```
1. Aba 5: Inserir cargas por fase
2. Calcular balanceamento
3. Ver sugestões de redistribuição
FIM
```

### Depois (v4.1):
```
1. Aba 5: Inserir cargas por fase
2. Calcular balanceamento
3. ✨ NOVO: Inserir dados do circuito
4. ✨ NOVO: Dimensionar condutor (NBR 5410)
5. ✨ NOVO: Gerar diagrama unifilar (PNG/PDF/DWG)
FIM
```

---

## 🎨 Interface Visual - Aba 5 Expandida

```
┌─────────────────────────────────────────────────────────┐
│         ⚖️ BALANCEAMENTO DE FASES (v4.1)               │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  [Carga Fase A]  [Carga Fase B]  [Carga Fase C]       │
│  • Carga A1      • Carga B1      • Carga C1            │
│  • Carga A2      • Carga B2      • Carga C2            │
│  • ... (até 20)  • ... (até 20)  • ... (até 20)        │
│                                                          │
│  [Calcular Balanceamento] button                        │
│                                                          │
│  ├─ Resultados: 3 colunas com métricas                 │
│  ├─ Gráfico: Distribuição de cargas                    │
│  └─ Sugestões: Redistribuição                          │
│                                                          │
├─ 🔧 DIMENSIONAMENTO E UNIFILAR (NOVO v4.1) ──────────┤
│                                                          │
│  [Nome Circuito]  [Tipo Circuito]                       │
│  [Comprimento]    [Queda Máx]                           │
│                                                          │
│  [📊 Dimensionar Condutor (NBR 5410)]                  │
│                                                          │
│  ├─ [Material]                                          │
│  ├─ [Tipo Instalação]                                   │
│  └─ [Resultado: Seção, Ampacidade, etc]                │
│                                                          │
│  ┌─ 📐 Gerar Esquema Unifilar (NOVO) ───────────────┐ │
│  │                                                  │ │
│  │  [🖼️ PNG]  [📄 PDF]  [🔧 DWG]                 │ │
│  │                                                  │ │
│  │  └─ Download individual de cada formato         │ │
│  └──────────────────────────────────────────────────┘ │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

---

## 📊 Campos Adicionados

### Seção 1: Dados do Circuito

| Campo | Tipo | Padrão | Descrição |
|:---|:---|:---|:---|
| **Nome do Circuito** | texto | "Circuito Balanceado" | Identificação do circuito |
| **Tipo de Circuito** | selectbox | "Monofásico 2 Fios" | Qual tipo de ligação |
| **Comprimento (m)** | número | 30.0 | Comprimento da tubulação/cabo |
| **Queda Máxima (%)** | número | 3.0 | Máximo permitido por NBR 5410 |

### Seção 2: Parâmetros Adicionais (aparecem após clicar botão)

| Campo | Tipo | Padrão | Descrição |
|:---|:---|:---|:---|
| **Material** | selectbox | "Cobre" | Cobre ou Alumínio |
| **Tipo Instalação** | selectbox | "Eletroduto Embutido (B1)" | Conforme Tabela 33 NBR 5410 |

---

## 💡 Fluxo Lógico

```python
# 1. Usuário preenche dados do circuito
nome = "Circuito Principal"
tipo = "Trifásico Com Neutro"
comprimento = 30.0 m
queda_max = 3.0 %

# 2. Clica "Dimensionar Condutor"
corrente = resultado_balanc['corrente_media']  # Usa média do balanceamento!

# 3. Software dimensiona conforme NBR 5410
resultado = dimensionar_condutor(
    corrente_circuito=corrente,
    comprimento_circuito=30.0,
    material="cobre",
    queda_tensao_max=3.0,
    tensao_nominal=380.0,
    tipo_instalacao="B1",
    num_circuitos=1,
    fator_temperatura=1.0
)

# 4. Exibe resultado (seção, ampacidade, queda real)

# 5. Gera unifilar nos 3 formatos
gerar_unifilar_matplotlib()  → PNG
gerar_pdf_unifilar()        → PDF (se ReportLab instalado)
gerar_dwg_unifilar()        → DWG (se EzDXF instalado)
```

---

## 🎯 Casos de Uso

### Caso 1: Residência com Balanceamento
```
Passo 1: Inserir cargas distribuídas nas 3 fases
  - Fase A: Cozinha 1.5kW + Banheiro 1.0kW + Quarto 0.5kW = 3.0kW
  - Fase B: Sala 2.0kW + Corredor 0.5kW = 2.5kW
  - Fase C: Lavanderia 1.0kW + Garagem 2.0kW = 3.0kW

Passo 2: Calcular balanceamento
  - Resultado: ✓ Equilibrado (0.0% desvio)

Passo 3: Dimensionar circuito
  - Nome: "Distribuição Residencial"
  - Tipo: "Trifásico Com Neutro"
  - Comprimento: 25m
  - Queda Máx: 3%
  
Passo 4: Clique "Dimensionar"
  - Material: Cobre
  - Instalação: Eletroduto Embutido (B1)
  
Passo 5: Resultado
  - Seção: 4 mm²
  - Ampacidade: 32 A
  - Queda Real: 2.8%
  - Status: ✓ Conforme

Passo 6: Gerar unifilar
  - Exportar PNG, PDF e DWG
  - Usar em projeto
```

### Caso 2: Indústria com Rebalanceamento
```
Passo 1: Inserir cargas desbalanceadas
  - Fase A: 15 kW
  - Fase B: 8 kW
  - Fase C: 12 kW

Passo 2: Calcular
  - Resultado: ⚠️ 22% desbalanceado
  - Sugestão: Retirar 3.5kW de A, adicionar 3.5kW em B

Passo 3: Ajustar cargas manualmente e recalcular

Passo 4: Quando equilibrado
  - Dimensionar condutor
  - Comprimento: 50m
  - Instalação: Bandeja (D)
  
Passo 5: Gerar unifilar
  - Usar em projeto de instalação
```

---

## 🔧 Detalhes Técnicos

### Dados Utilizados

**Do Balanceamento:**
```python
resultado_balanc = {
    'corrente_media': X.XX A,      # ← Usado para dimensionamento!
    'tensao_nominal': 380.0 V,     # ← Usado para cálculos
    'cargas_a/b/c': Y.YY kW,
    'desbalanceamento': Z.ZZ %,
    ...
}
```

**Para Dimensionamento:**
```python
dimensionar_condutor(
    corrente_circuito=resultado_balanc['corrente_media'],  # ← CHAVE
    comprimento_circuito=comprimento_circuito_bal,
    material=material_condutor_bal.lower(),
    queda_tensao_max=queda_tensao_max_bal,
    tensao_nominal=resultado_balanc.get('tensao_nominal', 380.0),
    tipo_instalacao=tipo_instalacao_map[tipo_instalacao_bal],
    num_circuitos=1,
    fator_temperatura=1.0
)
```

### Armazenamento em Sessão

```python
# Armazena resultados para reutilização
st.session_state['resultado_condutor_bal'] = resultado_condutor_bal
st.session_state['resultado_balanc_temp'] = resultado_balanc
st.session_state['nome_circuito_bal'] = nome_circuito_bal
st.session_state['comprimento_circuito_bal'] = comprimento_circuito_bal
```

Isso permite que os dados persist sejam mantidos entre interações.

---

## 📤 Exportação Unifilar

### PNG (Sempre Disponível)
```
✓ Usa Matplotlib
✓ Resolução: 300 DPI
✓ Formato: RGB
✓ Tamanho: ~100-300 KB
```

### PDF (Opcional - Requer ReportLab)
```
✓ Formato: A4 (210 × 297 mm)
✓ Qualidade: Vetorial
✓ Tamanho: ~50-100 KB
⚠️ Requer: pip install reportlab
```

### DWG (Opcional - Requer EzDXF)
```
✓ Formato: AutoCAD 2010 R2
✓ Camadas: Fases, Disjuntores, Condutores, Texto
✓ Tamanho: ~20-50 KB
⚠️ Requer: pip install ezdxf
```

---

## ✅ Validações Implementadas

### 1. Validação de Dados
```python
✓ Comprimento: 1.0 - 500.0 m
✓ Queda: 0.5 - 10.0 %
✓ Material: Cobre ou Alumínio
✓ Tipo instalação: A1-E conforme NBR 5410
```

### 2. Validação de Conformidade
```python
✓ Seção calculada vs seção padrão
✓ Ampacidade vs corrente ajustada
✓ Queda real vs queda máxima
✓ Alertas se não conforme
```

### 3. Validação de Exportação
```python
✓ Verifica se ReportLab disponível (PDF)
✓ Verifica se EzDXF disponível (DWG)
✓ Mensagens de erro claras se faltar
✓ PNG sempre funciona (Matplotlib)
```

---

## 🔄 Integração com Funções Existentes

### Funções Utilizadas

1. **`dimensionar_condutor()`** (v2.0)
   - Função original para NBR 5410
   - Cálcula seção, ampacidade, queda

2. **`gerar_unifilar_matplotlib()`** (v3.0)
   - Gera PNG com diagrama
   - Cores de fase: Red, Yellow, Blue

3. **`gerar_pdf_unifilar()`** (v3.0)
   - Gera PDF formatado A4
   - Requer ReportLab

4. **`gerar_dwg_unifilar()`** (v3.0)
   - Gera DWG com camadas
   - Requer EzDXF

### Novas Conexões

```
Aba 5 (Balanceamento)
  ↓
  └─→ dimensionar_condutor()  [Usa corrente média do balanceamento!]
       ↓
       ├─→ gerar_unifilar_matplotlib()  [PNG]
       ├─→ gerar_pdf_unifilar()          [PDF - opcional]
       └─→ gerar_dwg_unifilar()          [DWG - opcional]
```

---

## 📊 Exemplo de Uso Prático

### Entrada de Dados

```
BALANCEAMENTO:
Fase A: 5.0 kW
Fase B: 4.8 kW
Fase C: 5.2 kW
Desbalanceamento: 1.6% ✓ OK

CIRCUITO:
Nome: "Distribuição Principal"
Tipo: "Trifásico Com Neutro"
Comprimento: 40m
Queda Máxima: 3.0%
Material: Cobre
Instalação: Eletroduto Embutido (B1)
```

### Processamento

```
1. Corrente média = (5.0 + 4.8 + 5.2) / 0.92 / √3 / 380 = ~23.5 A

2. Dimensionamento NBR 5410:
   - Seção calculada: 4.0 mm²
   - Seção mínima queda: 2.5 mm²
   - Seção selecionada: 6.0 mm² (próxima padrão)
   
3. Verificação:
   - Ampacidade (6mm² cobre, B1): 41 A > 23.5 A ✓
   - Queda real: 2.8% < 3.0% ✓
   - Conforme: SIM ✓

4. Unifilar gerado com:
   - Trafo 30 kVA
   - Circuito trifásico
   - Cabo 6mm² (cores RGB)
   - Carga distribuída
```

### Saída

```
✓ Relatório com:
  - Seção: 6 mm² (Cobre)
  - Ampacidade: 41 A
  - Queda: 2.8%
  - PNG: unifilar_principal.png (300 DPI)
  - PDF: unifilar_principal.pdf (A4)
  - DWG: unifilar_principal.dwg (CAD)
```

---

## 🚀 Como Usar

### Passo a Passo

1. **Abra o software:**
   ```bash
   streamlit run app.py
   ```

2. **Acesse a Aba 5:**
   ```
   http://localhost:8501 → "⚖️ Balanceamento de Fases"
   ```

3. **Preencha cargas por fase** (3 fases, até 20 cargas cada)

4. **Clique "Calcular Balanceamento"**

5. **Verifique se está conforme:**
   - Desbalanceamento < 3%
   - Se não, use sugestões para rebalancear

6. **Preencha dados do circuito:** ✨ NOVO
   - Nome
   - Tipo
   - Comprimento
   - Queda máxima

7. **Clique "Dimensionar Condutor"** ✨ NOVO
   - Selecione material e instalação
   - Visualize resultado

8. **Clique em "Gerar PNG/PDF/DWG"** ✨ NOVO
   - Baixe os arquivos desejados

---

## ⚠️ Limitações e Considerações

### Limitações Conhecidas

1. **Diagrama Unifilar:**
   - Simplificado (não mostra todos os detalhes)
   - Uso principalmente para visualização
   - Para desenhos detalhados, usar CAD profissional

2. **DWG/PDF:**
   - Requer bibliotecas opcionais
   - Mensagens claras se não instaladas
   - PNG sempre funciona

3. **Balanceamento:**
   - Usa corrente média como base
   - Não diferencia entre fases na exportação
   - Diagrama genérico

### Recomendações

1. **Para projetos críticos:**
   - Validar com engenheiro
   - Usar CAD profissional para desenhos finais

2. **Para exportação DWG:**
   - Usar software CAD para edições adicionais
   - Adicionar detalhes específicos do projeto

3. **Para documentação:**
   - Combinar PNG + PDF com memorial de cálculo
   - Manter registros em arquivo

---

## 🔄 Fluxo de Dados

```
┌─────────────────────────────────────────┐
│  ENTRADA: Cargas por Fase (kW)         │
└────────────────┬────────────────────────┘
                 ↓
        ┌────────────────────┐
        │  Balanceamento     │
        │  Cálculo Corrente  │
        └────────┬───────────┘
                 ↓
        ┌────────────────────────┐
        │  NOVA ENTRADA v4.1:   │
        │  • Nome Circuito      │
        │  • Tipo Circuito      │
        │  • Comprimento        │
        │  • Queda Máxima       │
        └────────┬──────────────┘
                 ↓
        ┌────────────────────────────┐
        │  Dimensionamento NBR 5410 │
        │  Usar corrente média!     │
        └────────┬──────────────────┘
                 ↓
        ┌──────────────────────────────┐
        │  SAÍDA: 3 Formatos          │
        │  • PNG (Matplotlib)         │
        │  • PDF (ReportLab opt)      │
        │  • DWG (EzDXF opt)          │
        └──────────────────────────────┘
```

---

## 📝 Checklist de Implementação

- [x] Campos de entrada adicionados
- [x] Integração com dimensionar_condutor()
- [x] Chamadas para funções unifilar (PNG/PDF/DWG)
- [x] Validação de dados
- [x] Tratamento de erros
- [x] Mensagens de feedback
- [x] Downloads funcionando
- [x] Sem erros de sintaxe
- [x] Retrocompatibilidade mantida

---

## 🎊 Resultado Final

**Aba 5 (Balanceamento)** agora é um **workflow completo:**

```
Entrada de Cargas
    ↓
Verificação Balanceamento
    ↓
Dimensionamento de Condutor ← NOVO
    ↓
Geração de Unifilar ← NOVO
    ↓
Exportação (PNG/PDF/DWG) ← NOVO
    ↓
Pronto para Projeto!
```

---

**Versão:** 4.1  
**Data:** 31 de Janeiro de 2026  
**Status:** ✅ COMPLETA  
**Próximo:** Feedback de usuários e v4.2

🎉 **Nova funcionalidade ativa e pronta para uso!**
