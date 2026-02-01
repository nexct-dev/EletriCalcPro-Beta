# ⚡ GUIA RÁPIDO - SPDA (NBR 5419)

## O que é SPDA?

**SPDA** = Sistema de Proteção contra Descargas Atmosféricas

É um sistema que protege estruturas e pessoas contra descargas de raio, consistindo em:
1. **Capta-raios** (na cobertura)
2. **Condutores de descida** (pelas paredes)
3. **Aterramento** (na terra)
4. **Equipotencialização** (conexão de estruturas metálicas)

---

## 3 Passos Rápidos

### Passo 1: Determinar a Classe de Proteção

| Tipo de Estrutura | Classe | Eficiência | Quando Usar |
|:---|:---:|:---:|:---|
| 🏥 Hospitais, Datacenters, Estruturas Críticas | **I** | 98% | Máxima proteção |
| 🏢 Prédios altos, Indústrias especializadas | **II** | 95% | Alta proteção |
| 🏠 Residências, Edifícios comerciais | **III** | 90% | Média proteção |
| 🏗️ Estruturas temporárias, Galpões | **IV** | 80% | Proteção básica |

**👉 Dica:** Na dúvida, escolha **Classe III** (mais comum em residências/comércios)

---

### Passo 2: Medir as Dimensões da Estrutura

```
        ┌─────────── Comprimento (L) ──────────┐
        │                                       │
        │    ┌──────────────────────────┐      │
        │    │                          │      │
        │    │   Cobertura da           │      │
        ├────│   Estrutura              │      │ Largura
        │    │                          │ Altura
        │    │ (onde colocamos capta)   │      │
        │    │                          │      │
        │    └──────────────────────────┘      │
        │                                       │
        └───────────────────────────────────────┘
```

**Medidas necessárias:**
- **Altura** = do solo até a cobertura (em metros)
- **Comprimento** = dimensão maior da base (em metros)
- **Largura** = dimensão menor da base (em metros)

**Exemplo prático:**
- Residência: 10m altura, 20m comprimento, 15m largura
- Edifício: 25m altura, 80m comprimento, 50m largura

---

### Passo 3: Executar o Cálculo

1. Abrir o software: `streamlit run app.py`
2. Acessar: `http://localhost:8501`
3. Clicar na aba: **"⚡ SPDA (Descargas Atmosféricas)"**
4. Preencher campos:
   - Classe: Selecionar (I-IV)
   - Altura: Inserir valor em metros
   - Comprimento: Inserir valor em metros
   - Largura: Inserir valor em metros
   - Material: Selecionar (Cobre, Alumínio, Aço Galvanizado, Aço Inox)
   - Método: Selecionar (Esfera Rolante ou Malha)
5. Clicar: **"🔧 Dimensionar SPDA"**
6. Visualizar resultados

---

## 📊 Entendendo os Resultados

### Exemplo 1: Residência (Classe III)

**Entrada:**
```
Classe: III
Altura: 10m
Comprimento: 20m
Largura: 15m
Material: Cobre
```

**Saída:**
```
✅ CONFORME NBR 5419

Parâmetros de Proteção:
- Nível: III
- Eficiência: 90%
- Raio Esfera: 45m
- Malha: 15×15m

Componentes:
- Condutores de Descida: 4 unidades
- Distância entre eles: 20m
- Anéis de Aterramento: 1 unidade
- Altura de Captação: 12m

Materiais:
- Material: Cobre
- Espessura mínima: 2,0mm
- Seção mínima: 50mm²
- Comprimento total: 110m
- Massa estimada: 48,7kg
- Resistência aterramento: <10Ω
```

**O que significa?**
- ✅ Sistema conforme norma
- 🔩 Precisa 4 condutores (um em cada canto, com 1 intermediário)
- 📏 110m de fio de cobre 50mm²
- ⚖️ ~49kg de material
- 🌍 Eletrodos de terra com resistência menor que 10 Ohms

---

### Exemplo 2: Edifício Comercial (Classe II)

**Entrada:**
```
Classe: II
Altura: 25m
Comprimento: 80m
Largura: 50m
Material: Aço Galvanizado
```

**Saída:**
```
✅ CONFORME NBR 5419

Parâmetros de Proteção:
- Nível: II
- Eficiência: 95%
- Raio Esfera: 30m
- Malha: 10×10m

Componentes:
- Condutores de Descida: 18 unidades
- Distância entre eles: 15m
- Anéis de Aterramento: 2 unidades
- Altura de Captação: 27m

Materiais:
- Material: Aço Galvanizado
- Espessura mínima: 4,0mm
- Seção mínima: 95mm²
- Comprimento total: 970m
- Massa estimada: 574kg
- Resistência aterramento: <10Ω
```

**O que significa?**
- 🔩 Precisa 18 condutores distribuídos (proteção mais densa)
- 2️⃣ 2 anéis de aterramento (um a cada 12m de altura)
- 🔗 970m de material (malha + descidas)
- ⚖️ Mais pesado (~574kg) mas mais econômico que cobre
- ✅ Eficiência de 95% (proteção muito boa)

---

## 🎓 Conceitos Importantes

### Raio da Esfera Rolante

Imagine uma esfera gigante rolando sobre o telhado:
- **Classe I:** Esfera de 20m de raio (protege estruturas até 20m)
- **Classe III:** Esfera de 45m de raio (protege estruturas maiores)

Se sua estrutura for mais alta que o raio, **precisa de capta-raios adicionais** no topo.

### Tamanho da Malha

É o espaçamento entre os fios na cobertura:
- **Classe I:** Fios a cada 5m (proteção densa)
- **Classe III:** Fios a cada 15m (proteção média)

**Menor espaçamento = Melhor proteção = Mais material**

### Anéis Condutores

São fios "horizontais" nas paredes, a cada certa altura:
- Ligam os condutores de descida
- Distribuem a corrente do raio
- Reduzem diferença de potencial

---

## 💡 Dicas Práticas

### Residência Típica
```
✅ Use Classe III
✅ Capta-raios em todos os picos do telhado
✅ 4-6 condutores de descida (um em cada canto + intermediários)
✅ Material: Cobre ou Alumínio (custo-benefício)
✅ Custo estimado: R$ 1.500 - 2.500
```

### Edifício Comercial
```
✅ Use Classe II ou III
✅ Malha densa na cobertura
✅ Muitos condutores de descida (a cada 15m)
✅ Material: Aço Galvanizado (melhor custo)
✅ Anéis intermediários para estruturas altas
✅ Custo estimado: R$ 5.000 - 15.000
```

### Estrutura Crítica (Hospital/Datacentre)
```
✅ Sempre Classe I
✅ Material: Cobre (máxima condutividade)
✅ Redundância (múltiplos caminhos para terra)
✅ DPS em todos os equipamentos
✅ Aterramento com resistência < 2Ω
✅ Inspeção anual obrigatória
✅ Custo estimado: R$ 20.000 - 100.000+
```

---

## 🔧 Materiais: Como Escolher?

### Cobre 🟠
- **Melhor:** Condutividade, durabilidade
- **Pior:** Preço, risco de roubo
- **Use em:** Hospitais, datacenters, estruturas críticas

### Alumínio 🟤
- **Melhor:** Leve, custo moderado
- **Pior:** Menos durável, mais conexões
- **Use em:** Residências, comercial, estruturas leves

### Aço Galvanizado ⚪
- **Melhor:** Custo-benefício, robusto
- **Pior:** Resistência menor
- **Use em:** Indústrias, galpões, estruturas industriais

### Aço Inoxidável 🟦
- **Melhor:** Ambientes agressivos (marítimo)
- **Pior:** Muito caro, instalar complexo
- **Use em:** Laboratórios químicos, plataformas, estruturas especiais

---

## ⚙️ Equipotencialização: O Que É?

É conectar TUDO que é metal da estrutura ao sistema de SPDA:

```
🔗 Conectar:
├─ Estrutura de aço do edifício
├─ Tubulações de água/gás
├─ Ar condicionado (estrutura metálica)
├─ Ventilação (dutos metálicos)
├─ Painéis solares (se houver)
├─ Antenas e telecomunicações
└─ Equipamentos no telhado

Objetivo:
→ Evitar diferenças de potencial
→ Proteger pessoas de choques
→ Evitar danos a equipamentos
```

**Regra importante:**
- Tensão de toque segura: **50V** (ambiente seco)
- Tempo máximo de exposição: **5 segundos**
- Se alguém tocar estrutura energizada por raio → <50V = SEGURO

---

## 📋 Verificação: Sua Estrutura Precisa de SPDA?

Responda as perguntas:

1. **Localização?**
   - Em zona de descarga frequente? (muitos raios por ano)
   - Próximo ao topo de uma encosta? (aumento de risco)
   - Isolada em campo aberto?
   - **SIM em qualquer → Provavelmente precisa**

2. **Altura?**
   - Mais alta que estruturas vizinhas?
   - Prédio > 15m?
   - Torre ou antena?
   - **SIM → Risco aumentado**

3. **Ocupação?**
   - Pessoas vivem/trabalham?
   - Equipamentos eletrônicos críticos?
   - Dados importante a proteger?
   - **SIM → Mais critério de proteção**

4. **Legislação local?**
   - Município exige SPDA?
   - Norma técnica obriga?
   - Seguro exige?
   - **SIM → Precisa implementar**

**Resultado:**
- Se respondeu SIM em 2 ou mais: **Contratar engenheiro para avaliação**

---

## 📞 Próximas Ações

### Após usar o software:

1. **Obter relatório** → Exportar em TXT do software
2. **Validar com engenheiro** → Mostrar dimensionamento
3. **Orçar materiais** → Fornecedores SPDA locais
4. **Contratar instalação** → Empresa especializada
5. **Agendar inspeção** → Anual conforme NBR 5419
6. **Manter documentação** → Arquivo em local seguro

---

## ❓ FAQ - Perguntas Frequentes

**P: Quanto custa instalar SPDA?**  
R: Varia muito (R$ 1.500 a R$ 100.000+). Use o relatório do software para orçar.

**P: Quando fazer inspeção?**  
R: Anualmente. Profissionais vão verificar oxidação, conexões, aterramento.

**P: Pode instalar sozinho?**  
R: Não recomendado. Contratar empresa especializada garante conformidade.

**P: SPDA protege de tudo?**  
R: Protege a estrutura de danos diretos. Use DPS para equipamentos eletrônicos.

**P: Qual a vida útil?**  
R: 20-50 anos. Depende do material e manutenção.

---

**Última atualização:** 31 Janeiro 2026  
**Versão:** 4.0  
**Software:** EletriCalc Pro Beta
