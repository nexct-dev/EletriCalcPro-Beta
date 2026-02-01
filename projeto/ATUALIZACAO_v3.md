# 🚀 ATUALIZAÇÃO v3.0 - Balanceamento de Fases e Esquema Unifilar

## ✨ O que foi adicionado

### 1. **⚖️ ABA 5: Balanceamento de Fases**

#### Funcionalidades:
- ✅ Inserção de cargas por fase (A, B, C)
- ✅ Cálculo automático de correntes por fase
- ✅ Cálculo de desbalanceamento percentual
- ✅ Validação conforme NBR 5410 (máximo 3%)
- ✅ Sugestão de redistribuição de cargas
- ✅ Gráfico visual de distribuição
- ✅ Alertas inteligentes

#### Fórmulas Implementadas:
```python
I_fase = P_fase / (√3 × V_nominal × FP)
Desbalanceamento % = (I_max - I_min) / I_média × 100
```

#### Critério de Conformidade:
- Desbalanceamento ≤ 3.0% → ✅ CONFORME
- Desbalanceamento > 3.0% → ❌ NÃO CONFORME

---

### 2. **📐 ABA 6: Esquema Unifilar**

#### Funcionalidades:
- ✅ Geração de diagrama unifilar em PNG
- ✅ Exportação para PDF (relatório)
- ✅ Exportação para DWG (CAD)
- ✅ Suporte a 3 fases com cores padrão
- ✅ Inclusão de dados técnicos no diagrama
- ✅ Aterramento representado
- ✅ Disjuntores com correntes nominal
- ✅ Informações do condutor integradas

#### Elementos Desenhados:

**PNG (Matplotlib):**
- Trafo (Transformador 380V)
- Barramento principal
- 3 Fases (cores: vermelho, amarelo, azul)
- Disjuntores com proteção
- Condutores
- Cargas
- Aterramento
- Legenda completa

**PDF (ReportLab):**
- Layout profissional A4
- Informações técnicas formatadas
- Tabelas de dados
- Representação de fases
- Rodapé com data e normas

**DWG (EzDXF):**
- Formato AutoCAD 2010 R2
- Camadas organizadas (Fases, Disjuntores, Condutores, Texto)
- Elementos em escala
- Dimensionamentos técnicos
- Totalmente editável

---

## 🔧 Novas Funções Criadas

### 1. `balancear_fases(cargas_fase_a, cargas_fase_b, cargas_fase_c, tensao=380)`

**Parâmetros:**
- `cargas_fase_a` (list): Potências em kW da fase A
- `cargas_fase_b` (list): Potências em kW da fase B
- `cargas_fase_c` (list): Potências em kW da fase C
- `tensao` (float): Tensão nominal em V (padrão 380V)

**Retorna:**
```python
{
    "cargas_a": float,              # Soma potências fase A (kW)
    "cargas_b": float,              # Soma potências fase B (kW)
    "cargas_c": float,              # Soma potências fase C (kW)
    "correntes_a": float,           # Corrente fase A (A)
    "correntes_b": float,           # Corrente fase B (A)
    "correntes_c": float,           # Corrente fase C (A)
    "corrente_media": float,        # Média das 3 correntes (A)
    "desbalanceamento": float,      # Percentual de desbalanceamento (%)
    "carga_media": float,           # Média das 3 cargas (kW)
    "desvio_a": float,              # Desvio recomendado fase A (kW)
    "desvio_b": float,              # Desvio recomendado fase B (kW)
    "desvio_c": float,              # Desvio recomendado fase C (kW)
    "conforme": bool,               # Conforme NBR 5410?
    "alertas": list                 # Lista de avisos
}
```

---

### 2. `gerar_unifilar_matplotlib(resultado_condutor, nome_circuito="Circuito")`

**Retorna:**
- Figura matplotlib com diagrama unifilar
- Salva em PNG via Streamlit

**Elementos:**
- Trafo com tensão
- Barramento principal
- 3 Fases com cores
- Disjuntores e proteção
- Condutores
- Cargas
- Aterramento
- Caixa de informações

---

### 3. `gerar_pdf_unifilar(resultado_condutor, nome_circuito="Circuito")`

**Retorna:**
- Buffer BytesIO contendo PDF

**Conteúdo:**
- Cabeçalho com nome do circuito
- Informações técnicas tabuladas
- Representação de fases
- Rodapé com data e normas

**Requisito:**
- `pip install reportlab`

---

### 4. `gerar_dwg_unifilar(resultado_condutor, nome_circuito="Circuito")`

**Retorna:**
- Buffer BytesIO contendo DWG

**Recursos:**
- Camadas: Fases, Disjuntores, Condutores, Texto
- Trafo com coordenadas
- Barramento e fases
- Disjuntores posicionados
- Texto técnico
- Aterramento com símbolo padrão

**Requisito:**
- `pip install ezdxf`

---

## 📊 Dados Inclusos em Cada Formato

### PNG:
```
Seção do Condutor: X mm² (Material)
Ampacidade: X A
Corrente Ajustada: X A
Queda de Tensão: X%
Método de Instalação: XX
Data: DD/MM/YYYY
NBR 5410
```

### PDF:
- Seção do Condutor
- Ampacidade
- Corrente Ajustada
- Queda de Tensão
- Método de Instalação
- Data
- Normas aplicadas

### DWG:
- Camadas técnicas
- Coordenadas em escala
- Dimensionamentos
- Anotações técnicas
- Símbolos padrão CAD

---

## 🎨 Cores Utilizadas

### Fases (Padrão IEC/ABNT):
- **Fase A:** 🔴 Vermelho (RGB: 255, 0, 0)
- **Fase B:** 🟡 Amarelo (RGB: 255, 255, 0)
- **Fase C:** 🔵 Azul (RGB: 0, 0, 255)
- **Neutro:** ⚪ Branco/Cinza
- **Terra:** 🟢 Verde (RGB: 0, 128, 0)

---

## 📋 Interface por Aba

### Aba 5 - Balanceamento de Fases:

```
┌─ Fase A ──┐  ┌─ Fase B ──┐  ┌─ Fase C ──┐
│ Carga A1  │  │ Carga B1  │  │ Carga C1  │
│ Carga A2  │  │ Carga B2  │  │ Carga C2  │
│   ...     │  │   ...     │  │   ...     │
└───────────┘  └───────────┘  └───────────┘

[Calcular Balanceamento]

Resultados:
┌──────────┬──────────┬──────────┐
│ Fase A   │ Fase B   │ Fase C   │
├──────────┼──────────┼──────────┤
│ 10 kW    │ 10 kW    │ 10 kW    │
│ 15.2 A   │ 15.2 A   │ 15.2 A   │
└──────────┴──────────┴──────────┘

Desbalanceamento: 0.0% ✅

[Gráfico de barras com distribuição]
```

### Aba 6 - Esquema Unifilar:

```
Nome: ___________________
Seção: [dropdown]
Material: [Cobre/Alumínio]
Método: [A1/B1/B2/C/D/E]
Ampacidade: _____ A
Corrente: _____ A
Queda: _____ %

[📊 PNG] [📄 PDF] [🎨 DWG]

Informações do Esquema:
- Seção: X mm² (Material)
- Ampacidade: X A
- Corrente: X A
- Queda: X%
```

---

## 🔌 Requisitos de Dependências

### Atualizações em `requirements.txt`:

```
streamlit>=1.28.0       # Interface web
numpy>=1.24.0          # Cálculos numéricos
pandas>=2.0.0          # Manipulação de dados
openpyxl>=3.1.0        # Exportação Excel
matplotlib>=3.7.0      # Gráficos e diagramas (NOVO)
reportlab>=4.0.0       # Geração de PDF (NOVO)
ezdxf>=1.0.0           # Geração de DWG (NOVO)
```

### Instalação:
```bash
pip install -r requirements.txt
```

### Instalação Seletiva:
```bash
# Apenas essencial (sem PDF/DWG)
pip install streamlit numpy pandas openpyxl matplotlib

# Com PDF
pip install reportlab

# Com DWG
pip install ezdxf
```

---

## ✅ Verificações Realizadas

- [x] Sintaxe Python correta
- [x] Importações disponíveis
- [x] Funções sem erros
- [x] Interface Streamlit funcionando
- [x] Gráficos matplotlib gerados
- [x] Cálculos de balanceamento corretos
- [x] Fórmulas de desbalanceamento validadas
- [x] Documentação completa
- [x] Compatibilidade com versões anteriores
- [x] Tratamento de erros (bibliotecas opcionais)

---

## 🎯 Cobertura de Casos

### Balanceamento de Fases:
- ✅ Até 20 cargas por fase
- ✅ Qualquer combinação de potências
- ✅ Tensões de 127V até 1000V
- ✅ Cálculos trifásicos
- ✅ Sugestões automáticas

### Esquema Unifilar:
- ✅ Qualquer seção de condutor
- ✅ Cobre e alumínio
- ✅ 6 métodos de instalação
- ✅ 3 formatos diferentes
- ✅ Dados técnicos integrados

---

## 📈 Melhorias Implementadas

### Versus v2.0:
- ✨ +2 novas abas
- ✨ +4 novas funções
- ✨ +3 formatos de exportação (PNG, PDF, DWG)
- ✨ +1 gráfico de distribuição (Matplotlib)
- ✨ Validação NBR 5410 para balanceamento
- ✨ Interface mais intuitiva
- ✨ Documentação expandida

### Total Software:
- 📊 6 abas funcionais
- 📐 4 formatos de exportação (Excel, TXT, PNG, PDF, DWG)
- 📋 10+ funções de cálculo
- 📚 6 documentos de referência

---

## 🚀 Como Começar

### Primeiro Uso:

1. **Instale dependências:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Execute o software:**
   ```bash
   streamlit run app.py
   ```

3. **Teste o balanceamento:**
   - Abra aba 5
   - Insira cargas em cada fase
   - Clique "Calcular"
   - Veja sugestões

4. **Gere unifilar:**
   - Abra aba 6
   - Preencha dados
   - Clique em PNG/PDF/DWG
   - Baixe arquivo

---

## 💡 Casos de Uso

### Engenheiros:
- Balanceamento de painéis trifásicos
- Documentação de projetos
- Exportação para CAD

### Eletricistas:
- Verificação de carga por fase
- Distribuição equilibrada
- Diagnóstico rápido

### Fornecedores:
- Documentação técnica
- Propostas com diagrama
- Conformidade com normas

### Educadores:
- Ensino de balanceamento
- Demonstração de diagramas
- Material didático prático

---

## 📞 Suporte

### Problemas Comuns:

**"Matplotlib não funciona"**
→ Já incluído em requirements.txt

**"PDF não gera"**
→ Execute: `pip install reportlab`

**"DWG não abre"**
→ Execute: `pip install ezdxf`
→ Use AutoCAD 2010 ou superior

**"Desbalanceamento incorreto"**
→ Verifique FP (fator de potência) = 0.92
→ Verifique tensão inserida

---

## 🔄 Próximas Versões

### v3.1 (Previsto):
- [ ] Importar cargas de Excel
- [ ] Histórico de cálculos
- [ ] Múltiplos circuitos em um unifilar

### v4.0 (Previsto):
- [ ] Integração BIM (Revit)
- [ ] QR code com dados
- [ ] Assinatura digital
- [ ] Cloud storage

---

## 📝 Versão

- **Versão Anterior:** 2.0
- **Versão Atual:** 3.0 com Balanceamento e Unifilar
- **Novas Abas:** 2 (⚖️ Balanceamento, 📐 Unifilar)
- **Novas Funções:** 4
- **Data:** Janeiro 2026
- **Status:** ✅ COMPLETO E TESTADO

---

**Parabéns! 🎉 Seu software agora é muito mais completo!**

Próximo passo: Leia [NOVAS_FUNCIONALIDADES.md](NOVAS_FUNCIONALIDADES.md) para detalhes técnicos.
