# Tabelas NBR 5410 - Integradas no Software

Este documento descreve as tabelas da NBR 5410 que foram integradas ao software de dimensionamento de condutores elétricos.

## 📋 Tabela 33 - Métodos de Instalação

Define os diferentes métodos de instalação de condutores e seus respectivos códigos de referência utilizados para consultar a Tabela 36.

| Código | Método | Descrição |
|--------|--------|-----------|
| **A1** | Condutor Visível | Condutor isolado fixado diretamente em alvenaria ou superfície |
| **B1** | Eletroduto Embutido | Condutor em eletroduto embutido em alvenaria (padrão recomendado) |
| **B2** | Eletroduto Superfície | Condutor em eletroduto na superfície de parede ou estrutura |
| **C** | Eletrocalha | Condutores em eletrocalha aberta ou fechada |
| **D** | Bandeja | Condutores em bandeja porta-cabos ou similares |
| **E** | Enterrado | Condutores enterrados diretos no solo |

### Utilização:
1. Selecione o método de instalação mais adequado ao projeto
2. O software mapeará automaticamente para o código de referência
3. Este código será usado para consultar a Tabela 36

---

## ⚡ Tabela 36 - Capacidade de Condução de Corrente

Fornece a ampacidade (capacidade máxima de condução) dos condutores em função de:
- **Bitola (mm²)**: Seção transversal do condutor
- **Material**: Cobre ou Alumínio
- **Isolação**: PVC (temperatura de referência 70°C)
- **Temperatura ambiente**: 30°C ar (padrão)
- **Método de instalação**: Código de referência (A1, B1, B2, C, D, E)

### Formato da tabela integrada:
```python
tabela_36_cobre = {
    1.5:   {'A1': 17.5, 'B1': 13.5, 'B2': 15.5, 'C': 17.5, 'D': 18, 'E': 17},
    2.5:   {'A1': 24,   'B1': 18.5, 'B2': 21,   'C': 24,   'D': 25, 'E': 23},
    4:     {'A1': 32,   'B1': 25,   'B2': 28,   'C': 32,   'D': 33, 'E': 31},
    # ... demais bitolas
}
```

### Bitolas Disponíveis (mm²):
1.5 | 2.5 | 4 | 6 | 10 | 16 | 25 | 35 | 50 | 70 | 95 | 120 | 150 | 185 | 240

### Observações importantes:
- Para **alumínio**, há uma tabela separada com valores menores
- A ampacidade **diminui** conforme aumenta a temperatura ambiente
- Condutores em eletroduto (B1/B2) têm ampacidade menor que condutor visível (A1)
- Condutores enterrados (E) têm ampacidade intermediária

---

## 🔗 Tabela 42 - Fatores de Correção por Agrupamento

Quando múltiplos circuitos compartilham o mesmo eletroduto ou canaleta, o aquecimento mútuo reduz a ampacidade. Esta tabela define fatores de correção.

### Fatores por Número de Circuitos Agrupados:

| Nº Circuitos | Fator de Correção | Observação |
|-------------|------------------|-----------|
| 1           | 1.00             | Nenhuma redução |
| 2           | 0.80             | 20% de redução |
| 3           | 0.70             | 30% de redução |
| 4           | 0.65             | 35% de redução |
| 5           | 0.60             | 40% de redução |
| 6           | 0.57             | 43% de redução |
| 7           | 0.54             | 46% de redução |
| 8           | 0.52             | 48% de redução |
| 9+          | 0.50             | 50% de redução |

### Fórmula de Correção:
```
Ampacidade Ajustada = Ampacidade Tabela 36 × Fator de Agrupamento
```

### Exemplo:
- Condutor 2.5mm² em eletroduto embutido (B1) = 18.5 A
- Se houver 4 circuitos no mesmo eletroduto:
  - Fator = 0.65
  - Ampacidade ajustada = 18.5 × 0.65 = **12.025 A**

---

## 👥 Tabela 46 - Número de Condutores Carregados

Define quantos condutores de um circuito são considerados "carregados" para fins de cálculo de agrupamento e aquecimento.

| Tipo de Circuito | Condutores Carregados |
|-----------------|----------------------|
| Monofásico 2 fios | 2 |
| Monofásico 3 fios | 3 |
| Trifásico sem neutro | 3 |
| Trifásico com neutro | 4 |

### Importância:
- Circuitos trifásicos com neutro carregado (4 condutores) geram mais aquecimento
- O fator de agrupamento considerará todos os condutores carregados

---

## 📐 Cálculo Prático - Exemplo Completo

### Dados:
- Corrente do circuito: **20 A**
- Comprimento: **30 m**
- Queda de tensão máxima: **3%**
- Tensão nominal: **380 V**
- Material: **Cobre**
- Tipo instalação: **Eletroduto embutido (B1)**
- Nº de circuitos agrupados: **3**

### Passo 1: Calcular seção mínima pela queda de tensão
```
S_min = (ρ × L_r × I) / ΔU_max

Onde:
- ρ = 0.0175 Ω·mm²/m (cobre)
- L_r = 60 m (ida e volta: 2 × 30)
- I = 20 A
- ΔU_max = 11.4 V (3% de 380 V)

S_min = (0.0175 × 60 × 20) / 11.4 = 1.84 mm²
```

### Passo 2: Encontrar seção da Tabela 36
- Seção mínima = 1.84 mm²
- Seção padrão = **2.5 mm²**

### Passo 3: Verificar ampacidade (Tabela 36)
- Seção: 2.5 mm²
- Material: Cobre
- Método: B1 (eletroduto embutido)
- Ampacidade: **18.5 A**

### Passo 4: Aplicar fator de agrupamento (Tabela 42)
- Nº circuitos: 3
- Fator: 0.70
- Ampacidade ajustada = 18.5 × 0.70 = **12.95 A**

### Passo 5: Validação
- Corrente do circuito (20 A) **>** Ampacidade ajustada (12.95 A)
- **ALERTA:** Aumentar seção para 4 mm²

### Novo cálculo com 4 mm²:
- Ampacidade (B1): **25 A**
- Ampacidade ajustada: 25 × 0.70 = **17.5 A**
- Corrente (20 A) > Ampacidade (17.5 A)
- **ALERTA:** Aumentar seção para 6 mm²

### Seção final: 6 mm²
- Ampacidade (B1): **32 A**
- Ampacidade ajustada: 32 × 0.70 = **22.4 A**
- Corrente (20 A) ≤ Ampacidade (22.4 A) ✓
- Queda real: ~1.5% (dentro de 3%) ✓
- **CONFORME!**

---

## 🔧 Integração no Software

### Funções Principais:

#### `obter_ampacidade(secao, material='cobre', metodo='A1')`
Retorna a ampacidade da Tabela 36.

#### `obter_fator_agrupamento(num_circuitos)`
Retorna o fator de correção da Tabela 42.

#### `calcular_corrente_ajustada(corrente_calculada, num_circuitos=1, fator_temperatura=1.0, fator_agrupamento_manual=1.0)`
Calcula a corrente ajustada com fatores de correção:
```
Iz' = I / (fator_temperatura × fator_agrupamento)
```

#### `dimensionar_condutor(...)`
Função principal que:
1. Calcula seção mínima pela queda de tensão
2. Consulta Tabela 36 para ampacidade
3. Aplica fatores da Tabela 42
4. Valida conforme normas
5. Retorna seção selecionada e alertas

---

## 📊 Limitações e Considerações

### Não cobertas por este software:
- Fatores de temperatura ambiente diferente de 30°C
- Múltiplos métodos de correção simultâneos
- Ampacidades com diferentes temperaturas de isolação
- Cabos com diferentes isolações (não-PVC)
- Proteção contra sobrecargas dinâmicas

### Para cálculos avançados:
Consulte a norma NBR 5410 completa ou um engenheiro especializado em projetos elétricos.

---

## 📚 Referências Normativas

- **NBR 5410:2004** - Instalações Elétricas de Baixa Tensão
- **NBR 5356:2017** - Transformadores de Potência
- **IEC 60909:2016** - Short-circuit currents in three-phase AC systems

---

**Última atualização:** Janeiro 2026  
**Software:** EletriCalcPro Beta  
**Versão:** 2.0 com tabelas NBR 5410
