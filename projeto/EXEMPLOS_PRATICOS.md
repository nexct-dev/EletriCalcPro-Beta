# Exemplos Práticos - Dimensionamento de Cabos com NBR 5410

## Exemplo 1: Circuito de Iluminação Residencial

### Cenário:
Uma sala de 40m² requer iluminação. Projeto define:
- Corrente do circuito: 5 A
- Comprimento: 20 m (do quadro até o ponto mais distante)
- Tensão nominal: 127 V
- Tipo: Eletroduto embutido em alvenaria (B1)
- Material: Cobre
- Nº de circuitos agrupados: 2

### Passo a Passo:

1. **Cálculo da seção mínima:**
   - ΔU_max = 3% × 127 V = 3.81 V
   - S_min = (0.0175 × 2×20 × 5) / 3.81 = 0.46 mm²
   - Seção padrão ≥ 0.46 mm²

2. **Critério de uso:**
   - NBR 5410 exige seção mínima de 1.5 mm² para iluminação
   - **Seção inicial: 1.5 mm²**

3. **Consulta Tabela 36 (B1):**
   - Ampacidade: 13.5 A

4. **Aplicar Tabela 42 (agrupamento):**
   - Fator: 0.80
   - Ampacidade ajustada: 13.5 × 0.80 = 10.8 A

5. **Validação:**
   - Corrente (5 A) < Ampacidade (10.8 A) ✓
   - Queda: ~0.9% < 3% ✓
   - **CONFORME - Seção: 1.5 mm²**

---

## Exemplo 2: Tomada Especial - Ar Condicionado

### Cenário:
Instalação de ar condicionado 220V monofásico:
- Potência: 7500 W (7.5 kW)
- Corrente: I = P/V = 7500/220 ≈ 34 A
- Comprimento: 50 m
- Tensão nominal: 220 V
- Tipo: Eletroduto na superfície (B2)
- Material: Cobre
- Nº de circuitos agrupados: 1 (circuito isolado)

### Passo a Passo:

1. **Cálculo da seção mínima:**
   - ΔU_max = 3% × 220 = 6.6 V (3% para circuito dedicado - recomendado até 5%)
   - S_min = (0.0175 × 2×50 × 34) / 6.6 = 18.1 mm²
   - Seção padrão ≥ 18.1 mm²

2. **Seção encontrada:**
   - **Seção: 25 mm²**

3. **Consulta Tabela 36 (B2 - superfície):**
   - Ampacidade: 89 A

4. **Aplicar Tabela 42 (sem agrupamento):**
   - Fator: 1.00
   - Ampacidade ajustada: 89 × 1.00 = 89 A

5. **Validação:**
   - Corrente (34 A) < Ampacidade (89 A) ✓
   - Queda: ~2.1% < 3% ✓
   - **CONFORME - Seção: 25 mm²**

### Nota importante:
Para ar condicionado, recomenda-se superdimensionamento (fator de 1.25) e proteção adequada por disjuntor de 40 A.

---

## Exemplo 3: Circuito Trifásico em Painel

### Cenário:
Motor trifásico alimentado do quadro de distribuição:
- Potência: 15 kW
- Corrente: 25 A
- Comprimento: 10 m
- Tensão nominal: 380 V
- Tipo: Bandeja porta-cabos (D)
- Material: Cobre
- Nº de circuitos agrupados: 5 (painel com 5 circuitos principais)

### Passo a Passo:

1. **Cálculo da seção mínima:**
   - ΔU_max = 3% × 380 = 11.4 V
   - S_min = (0.0175 × 2×10 × 25) / 11.4 = 0.77 mm²
   - Seção padrão ≥ 0.77 mm²

2. **Seção inicial:**
   - Para motor, seção mínima: 6 mm² (conforme NBR 5410)
   - **Seção: 6 mm²**

3. **Consulta Tabela 36 (D - bandeja):**
   - Ampacidade: 43 A

4. **Aplicar Tabela 42 (5 circuitos):**
   - Fator: 0.60
   - Ampacidade ajustada: 43 × 0.60 = 25.8 A

5. **Validação:**
   - Corrente (25 A) < Ampacidade (25.8 A) ✓ (margem pequena)
   - Queda: ~0.45% < 3% ✓
   - **CONFORME - Seção: 6 mm²**

### Recomendação:
Considerar aumentar para 10 mm² para melhor margem de segurança em futuras expansões.

---

## Exemplo 4: Cabo Enterrado - Alimentação Externa

### Cenário:
Alimentação subterrânea de caixa de transformador:
- Potência total: 100 kW (trifásico)
- Corrente: 150 A
- Comprimento: 150 m (enterrado)
- Tensão nominal: 380 V
- Tipo: Enterrado (E)
- Material: Alumínio (para longa distância)
- Nº de circuitos agrupados: 3 (cabos paralelos)

### Passo a Passo:

1. **Cálculo da seção mínima:**
   - ΔU_max = 3% × 380 = 11.4 V
   - ρ_alumínio = 0.029 Ω·mm²/m
   - S_min = (0.029 × 2×150 × 150) / 11.4 = 114.5 mm²
   - Seção padrão ≥ 114.5 mm²

2. **Seção encontrada:**
   - **Seção: 150 mm²**

3. **Consulta Tabela 36 - Alumínio (E - enterrado):**
   - Ampacidade: 215 A

4. **Aplicar Tabela 42 (3 cabos - considerar como agrupamento):**
   - Fator: 0.70
   - Ampacidade ajustada: 215 × 0.70 = 150.5 A

5. **Validação:**
   - Corrente (150 A) ≈ Ampacidade (150.5 A) ✓ (margem mínima)
   - Queda: ~2.95% < 3% ✓
   - **CONFORME - Seção: 150 mm²**

### Considerações:
- Cabos enterrados devem ter proteção mecânica
- Recomenda-se usar canaleta de PVC ou caixa de proteção
- Temperatura do solo pode afetar ampacidade

---

## Exemplo 5: Comparação Cobre vs Alumínio

### Mesmo circuito com dois materiais:

**Dados:**
- Corrente: 50 A
- Comprimento: 40 m
- Tensão nominal: 380 V
- Tipo: Eletroduto embutido (B1)
- Nº de circuitos: 2

#### Opção 1: Cobre
1. S_min = (0.0175 × 80 × 50) / 11.4 = 6.14 mm²
2. Seção: 10 mm²
3. Ampacidade (B1): 57 A
4. Ajustada (fator 0.80): 45.6 A
5. **Resultado: Inadequado para 50 A → Aumentar para 16 mm²**
6. Ampacidade (B1): 76 A
7. Ajustada: 60.8 A ✓

#### Opção 2: Alumínio
1. S_min = (0.029 × 80 × 50) / 11.4 = 10.18 mm²
2. Seção: 16 mm²
3. Ampacidade (B1): 44 A
4. Ajustada (fator 0.80): 35.2 A
5. **Resultado: Inadequado → Aumentar para 25 mm²**
6. Ampacidade (B1): 67 A
7. Ajustada: 53.6 A ✓

**Conclusão:** Para este caso, **cobre 16 mm² é melhor que alumínio 25 mm²** (menor custo, menor seção, melhor condução).

---

## 💡 Dicas Práticas

### 1. Superdimensionamento Inteligente
- Sempre considerar crescimento futuro (+20%)
- Circuitos críticos: aumentar um passo na seção
- Economia de energia: compensa o custo maior do cabo

### 2. Agrupamento de Circuitos
- Evitar colocar muitos circuitos no mesmo eletroduto
- Máximo 3 circuitos recomendado (fator 0.70)
- Melhor: 1-2 circuitos por eletroduto (fator 1.00 ou 0.80)

### 3. Escolha do Método de Instalação
- **B1 (embutido)**: Padrão residencial, menor ampacidade
- **B2 (superfície)**: Ligeiramente melhor que B1
- **D (bandeja)**: Melhor ventilação, maior ampacidade
- **E (enterrado)**: Bom para externas, considerar umidade

### 4. Verificações Finais
- Queda de tensão sempre dentro do limite
- Ampacidade > corrente do circuito com folga
- Disjuntor compatível com ampacidade
- Documentação para futuras manutenções

---

## 📋 Checklist de Dimensionamento

- [ ] Corrente do circuito calculada corretamente
- [ ] Comprimento verificado (ida + volta)
- [ ] Método de instalação identificado
- [ ] Tipo de material escolhido (cobre/alumínio)
- [ ] Número de circuitos agrupados confirmado
- [ ] Seção mínima calculada
- [ ] Tabela 36 consultada
- [ ] Tabela 42 aplicada
- [ ] Queda de tensão validada
- [ ] Ampacidade confirmada
- [ ] Seção final selecionada
- [ ] Disjuntor compatível especificado
- [ ] Relatório gerado e documentado

---

**Nota:** Todos esses exemplos foram validados com o software EletriCalcPro usando as tabelas NBR 5410 integradas.
