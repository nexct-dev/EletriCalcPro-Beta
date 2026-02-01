# 📚 TABELAS E NORMAS - NBR 5419:2015

## Proteção de Estruturas contra Descargas Atmosféricas (SPDA)

**NBR 5419:2015** (ABNT) estabelece os requisitos para proteção de estruturas contra descargas atmosféricas. Este documento referencia as partes principais da norma com as tabelas essenciais para dimensionamento de SPDA.

---

## 📋 Índice

1. [Tabela 1 - Relação entre Níveis de Proteção](#tabela-1)
2. [Tabela 2 - Parâmetros de Proteção](#tabela-2)
3. [Tabela 3 - Espessura Mínima de Materiais](#tabela-3)
4. [Tabela 4 - Distâncias entre Condutores](#tabela-4)
5. [Tabela 5 - Materiais para SPDA](#tabela-5)
6. [Exemplos Práticos](#exemplos-praticos)
7. [Métodos de Proteção](#metodos-de-protecao)
8. [Cálculos de Aterramento](#calculos-de-aterramento)

---

## Tabela 1 - Relação entre Níveis de Proteção e Classes de SPDA {#tabela-1}

### NBR 5419-3:2015, Seção 4.1

Define a correspondência entre o nível de proteção desejado (I a IV) e a classe do SPDA correspondente.

| **Nível de Proteção** | **Classe de SPDA** | **Eficiência Mínima** | **Aplicação Recomendada** |
|:---:|:---:|:---:|:---|
| **I** | **I** | 98% | Hospitais, data centers, estruturas críticas |
| **II** | **II** | 95% | Prédios altos, indústrias especializadas |
| **III** | **III** | 90% | Residências, edifícios comerciais |
| **IV** | **IV** | 80% | Estruturas temporárias, galpões |

### Interpretação:
- **Nível I (Máxima)**: Estruturas onde falhas podem causar perdas críticas (vidas, dados)
- **Nível II (Alta)**: Estruturas com risco moderado a alto
- **Nível III (Média)**: Estruturas comuns com ocupação normal
- **Nível IV (Básica)**: Estruturas de baixo risco ou temporárias

---

## Tabela 2 - Valores de Raio da Esfera Rolante e Parâmetros {#tabela-2}

### NBR 5419-3:2015, Seção 5.1

Parâmetros fundamentais para aplicação dos métodos de proteção (esfera rolante e malha).

| **Classe SPDA** | **Raio da Esfera Rolante (m)** | **Tamanho da Malha (m)** | **Distância Condutores (m)** | **Distância Anéis (m)** |
|:---:|:---:|:---:|:---:|:---:|
| **I** | 20 | 5 × 5 | 10 | 10 |
| **II** | 30 | 10 × 10 | 15 | 15 |
| **III** | 45 | 15 × 15 | 20 | 20 |
| **IV** | 60 | 20 × 20 | 25 | 25 |

### Detalhamento:

#### Método da Esfera Rolante
- **Princípio**: Uma esfera imaginária de raio definido "rola" sobre a estrutura
- **Proteção**: Qualquer ponto tocado pela esfera está protegido
- **Aplicação**: Estruturas complexas, telhados irregulares
- **Vantagem**: Proteção máxima em geometrias complexas

#### Método da Malha
- **Princípio**: Condutores dispostos em malha regular sobre a cobertura
- **Espaçamento**: Definido conforme classe (5m a 20m)
- **Aplicação**: Estruturas simples, telhados planos
- **Vantagem**: Custo menor, instalação mais simples

#### Exemplo de Raio da Esfera Rolante
```
Para Classe III (Malha 15m × 15m):
Raio = 45 m

Isso significa que:
- Capta-raios devem estar posicionados tal que
- Uma esfera de 45 m de raio toque toda cobertura
- Qualquer ponto não tocado fica desprotegido
```

---

## Tabela 3 - Espessura Mínima de Chapas ou Tubulações Metálicas {#tabela-3}

### NBR 5419-3:2015, Seção 5.3

Define a espessura mínima necessária para garantir resistência mecânica e durabilidade.

| **Material** | **Espessura Mínima (mm)** | **Seção Mínima Condutor (mm²)** | **Resistividade (Ω·m)** | **Observações** |
|:---|:---:|:---:|:---:|:---|
| **Cobre** | 2,0 | 50 | 1,68×10⁻⁸ | Excelente condutividade, alto custo |
| **Alumínio** | 2,5 | 70 | 2,65×10⁻⁸ | Mais leve, custo moderado |
| **Aço Galvanizado** | 4,0 | 95 | 1,1×10⁻⁷ | Resistente à corrosão, baixo custo |
| **Aço Inoxidável** | 2,0 | 50 | 7,2×10⁻⁷ | Ambientes agressivos, custo alto |

### Cálculo de Resistência de um Condutor:

$$R = \rho \cdot \frac{L}{A}$$

Onde:
- **R** = Resistência (Ω)
- **ρ** = Resistividade (Ω·m)
- **L** = Comprimento (m)
- **A** = Área da seção (mm²)

#### Exemplo Prático:
```
Condutor de cobre de 50mm² e 100m:
R = 1,68×10⁻⁸ × (100 / 50×10⁻⁶)
R = 1,68×10⁻⁸ × 2×10⁶
R = 0,0336 Ω

Aço galvanizado equivalente (para L=100m):
R = 1,1×10⁻⁷ × (100 / 95×10⁻⁶)
R ≈ 0,116 Ω

O cobre tem ~3,4× melhor condutividade
```

---

## Tabela 4 - Distâncias Típicas entre Condutores {#tabela-4}

### NBR 5419-3:2015, Seção 5.2

Espaçamentos necessários para garantir distribuição adequada da corrente de descarga.

| **Classe de SPDA** | **Distância entre Condutores de Descida (m)** | **Distância entre Anéis Condutores (m)** | **Espaçamento Lateral (m)** |
|:---:|:---:|:---:|:---:|
| **I** | 10 | 10 | 1,0 |
| **II** | 15 | 15 | 1,5 |
| **III** | 20 | 20 | 2,0 |
| **IV** | 25 | 25 | 2,5 |

### Aplicação Prática:

#### Cálculo do Número de Condutores de Descida:
$$n_{condutores} = \left\lceil \frac{Perímetro}{Distância\_Permitida} \right\rceil$$

#### Exemplo:
```
Estrutura 40m × 30m, Classe III (distância 20m):
Perímetro = 2 × (40 + 30) = 140 m
Número mínimo = ⌈140 / 20⌉ = 7 condutores

Distribuição ótima:
- 2 condutores no comprimento (40m) → espaçados 20m
- 2 condutores na largura (30m) → espaçados 15m
- 3 condutores adicionais estrategicamente
```

---

## Tabela 5 - Materiais para SPDA e Condições de Utilização {#tabela-5}

### NBR 5419-3:2015, Seção 5.3

Guia de seleção de materiais baseado em aplicação e ambiente.

### Cobre

| **Propriedade** | **Valor** |
|:---|:---|
| Condutividade | ⭐⭐⭐⭐⭐ Excelente |
| Resistência à Corrosão | ⭐⭐⭐⭐ Muito boa |
| Custo | ⭐⭐ Elevado |
| Densidade | 8,9 g/cm³ |
| Ponto de Fusão | 1.083°C |

**Vantagens:**
- Melhor condutividade elétrica
- Durabilidade excepcional
- Baixa resistência de contato
- Não requer revestimento

**Desvantagens:**
- Custo muito elevado
- Alvo de furtos em algumas regiões

**Ambientes Recomendados:**
- Hospitais e clínicas
- Data centers
- Estruturas críticas
- Ambientes agressivos

---

### Alumínio

| **Propriedade** | **Valor** |
|:---|:---|
| Condutividade | ⭐⭐⭐⭐ Boa |
| Resistência à Corrosão | ⭐⭐⭐ Moderada |
| Custo | ⭐⭐⭐ Moderado |
| Densidade | 2,7 g/cm³ (3× mais leve que cobre) |
| Ponto de Fusão | 660°C |

**Vantagens:**
- Leve e fácil de instalar
- Custo razoável
- Boa condutividade

**Desvantagens:**
- Menor durabilidade que cobre
- Requer anodização em ambientes corrosivos
- Conexões mais críticas

**Ambientes Recomendados:**
- Residências
- Edifícios comerciais
- Estruturas leves
- Zonas rurais

---

### Aço Galvanizado

| **Propriedade** | **Valor** |
|:---|:---|
| Condutividade | ⭐⭐ Menor |
| Resistência à Corrosão | ⭐⭐⭐⭐ Excelente |
| Custo | ⭐⭐⭐⭐ Baixo |
| Densidade | 7,85 g/cm³ |
| Espessura Galvanização | 85 μm (ISO 1461) |

**Vantagens:**
- Custo-benefício excelente
- Resistência à corrosão comprovada
- Estrutura robusta
- Adequado para ambientes industriais

**Desvantagens:**
- Condutividade reduzida
- Peso elevado
- Requer cálculos mais precisos

**Ambientes Recomendados:**
- Indústrias
- Galpões e armazéns
- Estruturas expostas
- Ambientes marítimos

---

### Aço Inoxidável

| **Propriedade** | **Valor** |
|:---|:---|
| Condutividade | ⭐⭐ Baixa |
| Resistência à Corrosão | ⭐⭐⭐⭐⭐ Excepcional |
| Custo | ⭐ Muito alto |
| Densidade | 7,5 g/cm³ |
| Graus Típicos | AISI 304, 316 |

**Vantagens:**
- Resistência química excepcional
- Aparência profissional
- Manutenção reduzida

**Desvantagens:**
- Custo muito elevado
- Complexo de instalar e conectar
- Necessário para casos específicos

**Ambientes Recomendados:**
- Laboratórios químicos
- Indústria alimentícia
- Ambientes marítimos agressivos
- Edifícios de arquitetura especial

---

## Exemplos Práticos {#exemplos-praticos}

### Exemplo 1: Residência (Classe III)

**Dados da Estrutura:**
- Altura: 10 m
- Comprimento: 20 m
- Largura: 15 m
- Material: Cobre

**Dimensionamento:**

1. **Classe e Parâmetros:**
   - Classe: III (eficiência 90%)
   - Raio esfera: 45 m
   - Tamanho malha: 15 × 15 m
   - Distância condutores: 20 m

2. **Número de Condutores de Descida:**
   - Perímetro = 2(20 + 15) = 70 m
   - Número = ⌈70 / 20⌉ = 4 condutores

3. **Anéis Condutores:**
   - Número = ⌈10 / 20⌉ = 1 anel (na base)
   - Comprimento anel = 70 m

4. **Materiais Necessários:**
   - Comprimento condutores descida = 10 m × 4 = 40 m
   - Comprimento malha/anel = 70 m
   - **Total = 110 m de condutor de cobre 50mm²**
   - **Massa aproximada = 110 m × 0,443 kg/m = 48,7 kg**

5. **Aterramento:**
   - Eletrodos de terra em paralelo
   - Resistência alvo: < 10 Ω
   - Profundidade recomendada: 2,5 m

---

### Exemplo 2: Edifício Industrial (Classe II)

**Dados da Estrutura:**
- Altura: 25 m
- Comprimento: 80 m
- Largura: 50 m
- Material: Aço galvanizado

**Dimensionamento:**

1. **Classe e Parâmetros:**
   - Classe: II (eficiência 95%)
   - Raio esfera: 30 m
   - Tamanho malha: 10 × 10 m
   - Distância condutores: 15 m

2. **Número de Condutores de Descida:**
   - Perímetro = 2(80 + 50) = 260 m
   - Número = ⌈260 / 15⌉ = 18 condutores

3. **Anéis Condutores:**
   - Número = ⌈25 / 20⌉ = 2 anéis
   - Comprimento total anéis = 2 × 260 = 520 m

4. **Materiais Necessários:**
   - Comprimento condutores descida = 25 m × 18 = 450 m
   - Comprimento malha = 520 m
   - **Total = 970 m de condutor aço galvanizado 95mm²**
   - **Massa aproximada = 970 m × 0,592 kg/m ≈ 574 kg**

5. **Capta-raios:**
   - Dispostos em malha 10m × 10m
   - Altura de instalação: 27 m (acima da cobertura 2m)

---

### Exemplo 3: Torre de Telecomunicação (Classe I)

**Dados da Estrutura:**
- Altura: 60 m
- Base quadrada: 6m × 6m
- Material: Cobre

**Dimensionamento:**

1. **Classe e Parâmetros:**
   - Classe: I (eficiência 98%)
   - Raio esfera: 20 m
   - Tamanho malha: 5 × 5 m
   - Distância condutores: 10 m

2. **Número de Condutores de Descida:**
   - Perímetro = 4 × 6 = 24 m
   - Número = ⌈24 / 10⌉ = 3 (mínimo 2, então 3)

3. **Anéis Condutores:**
   - Número = ⌈60 / 20⌉ = 3 anéis
   - Espaçamento: 20 m
   - Comprimento total = 3 × 24 = 72 m

4. **Materiais Necessários:**
   - Comprimento condutores descida = 60 m × 3 = 180 m
   - Comprimento anéis = 72 m
   - **Total = 252 m de condutor de cobre 50mm²**
   - **Massa = 252 m × 0,443 kg/m ≈ 112 kg**

5. **Aterramento Crítico:**
   - Múltiplos eletrodos paralelos
   - Resistência: < 2 Ω
   - Profundidade: até 3 m
   - Gel condutor para melhor contato

---

## Métodos de Proteção {#metodos-de-protecao}

### 1. Método da Esfera Rolante

**Princípio Físico:**
- Simula uma esfera imaginária rolando sobre a estrutura
- Todo ponto tocado pela esfera está protegido
- Pontos não tocados ficam desprotegidos

**Aplicação:**
- Estruturas com geometria complexa
- Telhados irregulares
- Estruturas com múltiplos níveis

**Algoritmo de Verificação:**
```
Para cada ponto P na estrutura:
  Distância mínima ao capta-raios = ?
  SE distância > raio da esfera:
    Ponto não está protegido
    → Adicionar capta-raios
```

**Vantagens:**
- Proteção máxima em geometrias complexas
- Fácil visualizar cobertura

**Desvantagens:**
- Requer mais capta-raios
- Custo maior
- Complexo calcular manualmente

---

### 2. Método da Malha

**Princípio:**
- Condutores em malha regular sobre cobertura
- Espaçamento conforme classe de SPDA

**Aplicação:**
- Estruturas com telhado plano
- Coberturas regulares
- Instalação mais simples

**Especificação:**
- Malha 5×5 m (Classe I) até 20×20 m (Classe IV)
- Condutores longitudinais e transversais
- Ligação nas intersecções

**Vantagens:**
- Custo menor
- Instalação simples
- Cálculos diretos

**Desvantagens:**
- Menos eficiente em geometrias complexas
- Pontos de sombra em estruturas irregulares

---

### 3. Método do Ângulo de Proteção (Não aplicável ao Brasil - Classes I-IV)

**Nota:** Segundo NBR 5419 brasileira, este método não é recomendado para os níveis de proteção I-IV aplicáveis na proteção de estruturas.

---

## Cálculos de Aterramento {#calculos-de-aterramento}

### Resistência de Aterramento

**Fórmula para eletrodo vertical:**
$$R = \frac{\rho}{2\pi L} \left( \ln\left(\frac{4L}{d}\right) - 1 \right)$$

Onde:
- **R** = Resistência (Ω)
- **ρ** = Resistividade do solo (Ω·m)
- **L** = Comprimento eletrodo (m)
- **d** = Diâmetro eletrodo (m)

**Resistividade Típica do Solo:**
- Solo muito seco: 1.000 a 10.000 Ω·m
- Solo seco: 100 a 1.000 Ω·m
- Solo úmido: 10 a 100 Ω·m
- Solo muito úmido: 1 a 10 Ω·m
- Solo com argila: 5 a 50 Ω·m

**Exemplo de Cálculo:**
```
Eletrodo de cobre:
- L = 2,5 m (profundidade)
- d = 0,025 m (diâmetro 25 mm)
- ρ = 50 Ω·m (solo com argila úmida)

R = 50 / (2π × 2,5) × [ln(4 × 2,5 / 0,025) - 1]
R = 50 / 15,708 × [ln(400) - 1]
R = 3,183 × [5,99 - 1]
R = 3,183 × 4,99
R ≈ 15,9 Ω

Resultado: Necessários múltiplos eletrodos em paralelo
```

### Configurações Comuns

#### 1. Eletrodo Único
- **Resistência típica:** 20-50 Ω
- **Profundidade:** 2,0-2,5 m
- **Uso:** Estruturas pequenas

#### 2. Eletrodos em Paralelo
- **Fórmula:** $R_{total} = \frac{R_1 \times R_2}{R_1 + R_2}$ (para 2 eletrodos)
- **Uso:** Estruturas médias e grandes
- **Exemplo:** 3 eletrodos de 20 Ω em paralelo:
  - Resistência total ≈ 6,7 Ω ✓ (< 10 Ω)

#### 3. Anel de Aterramento
- **Perímetro:** Envolta da estrutura
- **Profundidade:** 0,8-1,0 m
- **Uso:** Estruturas com perímetro regular
- **Resistência típica:** 5-15 Ω

---

## Equipotencialização (NBR 5419-6:2015)

### Objetivo:
Reduzir diferenças de potencial entre condutores e estruturas metálicas para evitar choques elétricos e danos a equipamentos.

### Componentes a Equipotencializar:
1. Estrutura metálica da construção
2. Instalações metálicas (água, gás)
3. Estruturas de ar condicionado
4. Condutas de ventilação
5. Sistemas de telecomunicações
6. Painéis solares (se houver)

### Tensão de Toque Segura:
- **Ambiente seco:** 50 V
- **Ambiente úmido:** 24 V
- **Ambiente molhado:** 12 V

### Corrente Segura (Curva de Dalziel):
$$I_{segura} = \frac{0.165}{\sqrt{t}}$$

Onde t = tempo de exposição em segundos (máx. 5s)

---

## Verificação de Conformidade

### Checklist de Conformidade (NBR 5419:2015)

- [ ] Avaliação de risco realizada (Parte 2 - NBR 5419-2)
- [ ] Classe de SPDA adequada ao risco
- [ ] Capta-raios instalados conforme classe
- [ ] Condutores de descida espaçados corretamente
- [ ] Anéis condutores nas profundidades corretas
- [ ] Aterramento com resistência < 10 Ω
- [ ] Equipotencialização completa
- [ ] DPS (Proteção contra Surtos) instalado
- [ ] Inspeção periódica planejada
- [ ] Documentação de projeto arquivada

---

## Manutenção e Inspeção

### Inspeção Visual (Anual)
- Verificar integridade de conexões
- Checar oxidação de componentes
- Inspecionar aterramento

### Teste de Resistência (A cada 5 anos)
- Medir resistência de aterramento
- Verificar continuidade de condutores
- Testar equipamentos DPS

### Manutenção Preventiva
- Limpeza de contatos
- Reapertamento de conexões soltas
- Reposição de componentes danificados

---

## Referências Normativas

1. **NBR 5419-1:2015** - Princípios gerais
2. **NBR 5419-2:2015** - Avaliação de risco
3. **NBR 5419-3:2015** - Danos físicos e perigos à vida
4. **NBR 5419-4:2015** - Sistemas elétricos e eletrônicos
5. **NBR 5419-5:2015** - Serviços internos
6. **NBR 5419-6:2015** - Equipotencialização e ligações
7. **NBR 5419-7:2015** - Conceitos históricos

---

## Contato e Suporte

Para dúvidas sobre aplicação:
- Consulte engenheiro especializado em SPDA
- Verifique normas atualizadas junto à ABNT
- Considere certificação técnica de fornecedores

**Última atualização:** Janeiro 2026  
**Versão:** 1.0  
**Software:** EletriCalc Pro Beta
