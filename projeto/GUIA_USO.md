# Guia de Uso - Software Dimensionamento de Condutores v2.0

## 🎯 Objetivo

Este software calcula a seção correta de cabos elétricos conforme **NBR 5410**, utilizando as tabelas oficiais para garantir:
- ✓ Segurança da instalação
- ✓ Conformidade com normas
- ✓ Eficiência energética
- ✓ Proteção contra sobrecarga

---

## 📋 Interface Principal

O software possui 4 abas principais:

### 1. **📦 Condutores** (NOVA VERSÃO COM TABELAS NBR 5410)
Dimensionamento de cabos com tabelas reais

### 2. **🔋 Transformadores**
Seleção de potência de transformadores

### 3. **⚙️ Disjuntores**
Proteção de circuitos por corrente

### 4. **⚡ Curto-Circuito**
Cálculo de correntes de falta

---

## 🔌 ABA 1: DIMENSIONAMENTO DE CONDUTORES

### Parâmetros de Entrada

#### 1. **Corrente do Circuito (A)** ⚡
- **Descrição:** Corrente que circulará no circuito
- **Como calcular:**
  - Monofásico: I = P / V
  - Trifásico: I = P / (√3 × V × FP)
- **Exemplos:**
  - Iluminação 1500W em 127V: 1500/127 = 11.8 A
  - Motor 7.5kW em 380V trifásico: 7500/(1.732×380×0.92) ≈ 13 A
- **Intervalo:** 0.1 a 500 A

#### 2. **Comprimento do Circuito (m)** 📏
- **Descrição:** Distância do quadro até o ponto de consumo
- **Importante:** Use apenas a distância de uma via
  - O software automaticamente considera ida e volta (×2)
  - Exemplo: parede com 25m = inserir 25m (não 50m)
- **Intervalo:** 0 a 1000 m

#### 3. **Queda de Tensão Máxima (%)** 📉
- **Descrição:** Percentual máximo de redução de tensão permitido
- **Recomendações NBR 5410:**
  - **Geral:** 3%
  - **Iluminação:** 2% (recomendado)
  - **Força (motores):** 3%
  - **Circuitos críticos:** 1-2%
- **Padrão:** 3%
- **Intervalo:** 0.1 a 10%

#### 4. **Tensão Nominal (V)** 🔋
- **Descrição:** Tensão de operação do circuito
- **Opções comuns:**
  - **127 V** - Circuitos monofásicos residenciais
  - **220 V** - Circuitos monofásicos industriais
  - **380 V** - Circuitos trifásicos (padrão)
  - **440 V** - Alternativa em algumas regiões
- **Intervalo:** 100 a 1000 V

#### 5. **Material do Condutor** 🧱
- **Opções:**
  - **Cobre** (recomendado)
    - Melhor condução (17.5 μΩ·cm)
    - Maior custo
    - Menor seção necessária
    - Mais durável
  - **Alumínio**
    - Condução inferior (29 μΩ·cm)
    - Menor custo
    - Maior seção necessária
    - Usar em longas distâncias

#### 6. **Tipo de Instalação (Tabela 33)** 📍
- **Descrição:** Onde e como o cabo será instalado
- **Opções:**
  
  | Código | Tipo | Melhor Ampacidade | Quando Usar |
  |--------|------|------------------|-----------|
  | **A1** | Condutor Visível | Alta | Áreas abertas, fácil manutenção |
  | **B1** | Eletroduto Embutido | Média (Padrão) | Paredes, padrão residencial/comercial |
  | **B2** | Eletroduto Superfície | Média-Alta | Paredes externas, áreas molhadas |
  | **C** | Eletrocalha | Alta | Painéis, quadros de distribuição |
  | **D** | Bandeja | Alta | Painéis, múltiplos circuitos |
  | **E** | Enterrado | Média | Alimentações externas, subterrâneas |

- **Recomendação:** B1 é o padrão mais seguro para residências

#### 7. **Nº de Circuitos Agrupados (Tabela 42)** 🔗
- **Descrição:** Quantos circuitos compartilham o mesmo eletroduto
- **Efeito:** Aumenta aquecimento, reduz ampacidade
- **Fatores Aplicados:**
  - 1 circuito: 1.00 (sem redução)
  - 2 circuitos: 0.80 (20% redução)
  - 3 circuitos: 0.70 (30% redução)
  - 4 circuitos: 0.65 (35% redução)
  - 5+ circuitos: 0.50-0.60 (até 50% redução)
- **Dica:** Maximizar 2-3 circuitos por eletroduto

#### 8. **Fator de Temperatura** 🌡️
- **Descrição:** Ajuste para temperatura ambiente
- **Valores:**
  - 1.0 (100%): 30°C - Padrão, temperatura ambiente normal
  - 0.9 (90%): ~35°C - Ambiente quente
  - 0.8 (80%): ~40°C - Ambiente muito quente
  - 0.7 (70%): ~45°C - Condições extremas
- **Padrão:** 1.0
- **Nota:** A maioria dos projetos usa 1.0

---

### Parâmetros de Saída

#### 📊 **Seção Mínima (mm²)**
- Seção calculada apenas pelo critério de queda de tensão
- Pode ser insuficiente para ampacidade
- O software aumentará se necessário

#### 📦 **Seção Selecionada (mm²)**
- **Seção FINAL recomendada**
- Atende simultaneamente:
  - Queda de tensão máxima
  - Ampacidade do condutor
  - Fatores de correção (agrupamento, temperatura)
- **Esta é a seção que deve ser ESPECIFICADA no projeto**

#### ⚡ **Ampacidade (Tabela 36)**
- Capacidade máxima de corrente do cabo selecionado
- Consultada da tabela NBR 5410 oficial
- Inclui o método de instalação

#### 🔌 **Corrente Ajustada (A)**
- Corrente máxima após aplicar fatores de correção
- Fórmula: I_ajustada = I_tabela / (fator_temp × fator_agrp)
- Deve ser ≥ corrente do circuito

#### 📉 **Queda Real (%)**
- Queda de tensão real com seção selecionada
- Deve estar ≤ Queda de tensão máxima
- Fórmula: ΔU% = (R × I × L × 100) / V

#### 🏷️ **Método Instalação**
- Código da Tabela 33 utilizado (A1, B1, B2, C, D, E)

#### 🧱 **Material**
- Material selecionado (Cobre ou Alumínio)

---

### ✓ Status de Conformidade

#### 🟢 **Conforme NBR 5410**
Todos os critérios foram atendidos:
- ✓ Queda de tensão dentro do limite
- ✓ Ampacidade suficiente
- ✓ Fatores de correção aplicados
- ✓ Seção dentro do padrão

**Ação:** Especificar a seção indicada no projeto

#### 🟠 **Alertas**
Um ou mais critérios podem não estar 100% atendidos.

**Exemplos de alertas:**
- "Queda 3.5% > máximo 3%. Aumentar seção."
- "Corrente 50A > Ampacidade 45A. Aumentar seção."
- "In 50A > 1.25×Iz. Verificar seleção."

**Ação:** Aumentar seção conforme recomendação

---

## 📥 Exportação de Resultados

O software oferece dois formatos de exportação:

### 1. **📥 Baixar Excel**
- Arquivo profissional com formatação
- Tabelas com dados de entrada e saída
- Fácil compartilhamento com cliente/obra
- Pronto para impressão
- Formato: `condutor_DDMMYYYY_HHMMSS.xlsx`

### 2. **📄 Baixar Relatório**
- Arquivo texto com memorial descritivo
- Referência às normas aplicadas (Tabelas 33, 36, 42, 46)
- Cálculos realizados
- Alertas e observações
- Formato: `condutor_DDMMYYYY_HHMMSS.txt`

### 3. **📋 Visualizar Relatório**
- Lê o relatório direto na tela
- Sem necessidade de download
- Útil para verificação rápida

---

## 🧮 Fórmulas Internas

### 1. Seção mínima pela queda de tensão
```
S = (ρ × L_r × I) / ΔU_max

Onde:
- S = Seção em mm²
- ρ = Resistividade do material (Ω·mm²/m)
- L_r = 2 × Comprimento (ida + volta)
- I = Corrente em A
- ΔU_max = Queda máxima em V (3% × V_nominal)
```

### 2. Queda de tensão real
```
ΔU% = (R × I × L_r × 100) / V

Onde:
- R = Resistência do condutor = (ρ × L_r) / S
- I = Corrente em A
- V = Tensão nominal em V
```

### 3. Corrente ajustada
```
I_ajustada = I_circuito / (fator_temperatura × fator_agrupamento)
```

---

## 📋 Passo-a-Passo Recomendado

### Para dimensionar um circuito:

1. **Levante os dados:**
   - Potência ou corrente do circuito
   - Comprimento até o ponto de consumo
   - Local de instalação (tipo de eletroduto)
   - Quantos circuitos no mesmo tubo

2. **Abra o software**
   - Clique na aba "📦 Condutores"

3. **Preencha os parâmetros:**
   - Comece com os valores obrigatórios (corrente, comprimento)
   - Use os padrões recomendados (queda 3%, método B1)
   - Ajuste conforme necessário

4. **Clique em "Calcular Dimensionamento"**

5. **Analise os resultados:**
   - Se conforme: use a seção indicada
   - Se alertas: analise a recomendação e aumentar seção

6. **Exporte:**
   - Excel para documentação completa
   - Relatório para justificativas técnicas

7. **Especifique no projeto:**
   - Use a "Seção Selecionada" indicada
   - Justifique com referência às tabelas NBR 5410

---

## ⚠️ Dicas Importantes

### 1. Sempre verifique:
- [ ] A corrente foi calculada corretamente
- [ ] O comprimento inclui toda a trajetória
- [ ] O tipo de instalação está correto
- [ ] O número de circuitos está preciso

### 2. Margem de segurança:
- Considere aumentar um passo na seção se:
  - Expansão futura é provável
  - Circuito é crítico
  - Diferença entre corrente e ampacidade é pequena

### 3. Comparar alternativas:
- Teste cobre vs alumínio
- Teste diferentes métodos de instalação
- Compare custo vs segurança

### 4. Documentação:
- Sempre guarde os relatórios
- Facilita futuras manutenções
- Justifica as escolhas feitas
- Necessário em auditoria de segurança

---

## 🔍 Validação de Resultados

### Seção está correta se:
- ✓ Queda real ≤ Queda máxima
- ✓ Ampacidade ≥ Corrente ajustada
- ✓ Status = "Conforme"
- ✓ Sem alertas (ou alertas aceitáveis)

### Exemplo de resultado correto:
```
Corrente do Circuito: 20 A
Seção Selecionada: 2.5 mm²
Ampacidade: 24 A
Queda Real: 1.8% < 3% ✓
Status: ✓ Conforme
```

---

## 📞 Suporte e Dúvidas

### Erros comuns:
- **"Queda > máximo"** → Aumentar seção
- **"Corrente > Ampacidade"** → Aumentar seção
- **"Fora da faixa"** → Seção muito grande, consultar especialista

### Para mais informações:
- Consulte o arquivo [TABELAS_NBR5410.md](TABELAS_NBR5410.md)
- Veja [EXEMPLOS_PRATICOS.md](EXEMPLOS_PRATICOS.md)
- Refira-se à norma NBR 5410:2004

---

**Versão:** 2.0  
**Última atualização:** Janeiro 2026  
**Software:** EletriCalcPro Beta  
**Compatibilidade:** NBR 5410:2004
