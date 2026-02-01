# ✨ Novas Funcionalidades v3.0

## 🎯 Balanceamento de Fases

### O que é?
Sistema para verificar o equilíbrio de carga entre as três fases de um circuito trifásico, conforme exigências da NBR 5410.

### Por que é importante?
- ✅ Evita sobrecarga em uma única fase
- ✅ Reduz aquecimento e perdas
- ✅ Aumenta eficiência energética
- ✅ Melhora qualidade de energia
- ✅ Conformidade com normas (máximo 3% desbalanceamento)

### Como usar?

#### Passo 1: Acesse a aba "⚖️ Balanceamento de Fases"

#### Passo 2: Defina as cargas
```
Fase A: Carga A1 (2.0 kW) + Carga A2 (2.5 kW) + ...
Fase B: Carga B1 (2.0 kW) + Carga B2 (2.5 kW) + ...
Fase C: Carga C1 (2.0 kW) + Carga C2 (2.5 kW) + ...
```

#### Passo 3: Selecione a tensão (padrão: 380V trifásico)

#### Passo 4: Clique em "Calcular Balanceamento"

### Resultados Fornecidos

#### Por Fase:
- **Carga Total (kW)** - Soma de todas as cargas
- **Corrente Calculada (A)** - I = P / (√3 × V × FP)

#### Visão Geral:
- **Desbalanceamento (%)** - Percentual de desvio (máx 3%)
- **Corrente Média (A)** - Média das 3 fases
- **Carga Média (kW)** - Média das 3 fases

#### Sugestões:
- Quanto (kW) retirar ou adicionar em cada fase
- Gráfico visual mostrando distribuição atual

### Cálculo do Desbalanceamento

```
Desbalanceamento (%) = (I_max - I_min) / I_média × 100

Onde:
- I_max = Maior corrente entre as 3 fases
- I_min = Menor corrente entre as 3 fases
- I_média = Média das 3 correntes
```

### Conformidade NBR 5410

- ✅ **Máximo permitido:** 3%
- ⚠️ **Entre 1-3%:** Aceitável, mas considere balanceamento melhor
- ❌ **Acima de 3%:** Não conforme, redistribuição necessária

### Exemplo Prático

**Cenário Inicial (Desbalanceado):**
```
Fase A: 10 kW → I = 15.2 A
Fase B: 5 kW  → I = 7.6 A
Fase C: 15 kW → I = 22.8 A

Desbalanceamento = (22.8 - 7.6) / 15.2 × 100 = 100% ❌ (MUITO BEM!)
```

**Após Balanceamento (Sugerido):**
```
Fase A: 10 kW → I = 15.2 A
Fase B: 10 kW → I = 15.2 A
Fase C: 10 kW → I = 15.2 A

Desbalanceamento = (15.2 - 15.2) / 15.2 × 100 = 0% ✅ (PERFEITO!)
```

---

## 📐 Esquema Unifilar

### O que é?
Gerador automático de diagramas unifilares em múltiplos formatos (PNG, PDF, DWG).

### Por que é importante?
- ✅ Documentação visual do projeto
- ✅ Fácil compartilhamento
- ✅ Compatível com CAD
- ✅ Exportação profissional
- ✅ Reduz tempo de desenho

### Formatos Suportados

#### 1. **PNG** (Raster/Imagem)
- ✅ Compatível com todos os sistemas
- ✅ Pronto para impressão (300 DPI)
- ✅ Fácil compartilhamento por email
- ❌ Não editável

#### 2. **PDF** (Documento)
- ✅ Preserva formatação
- ✅ Pronto para impressão
- ✅ Pode incluir múltiplas páginas
- ✅ Segurança (protegido)
- ❌ Não facilmente editável

#### 3. **DWG** (AutoCAD)
- ✅ Totalmente editável
- ✅ Compatível com CAD, Revit, etc
- ✅ Segue padrões de desenho técnico
- ✅ Integração com outros projetos
- ✅ Ideal para arquivamento profissional

### Como usar?

#### Passo 1: Acesse a aba "📐 Esquema Unifilar"

#### Passo 2: Preencha os dados
```
Nome do Circuito: "Circuito de Iluminação - Sala 101"
Seção: 2.5 mm²
Material: Cobre
Método: B1 (Eletroduto Embutido)
Ampacidade: 18.5 A
Corrente: 15 A
Queda: 1.8%
```

#### Passo 3: Gere no formato desejado
- Clique "📊 Gerar PNG" para imagem
- Clique "📄 Gerar PDF" para documento
- Clique "🎨 Gerar DWG" para CAD

#### Passo 4: Baixe o arquivo

### Elementos do Unifilar

#### Componentes Principais:

1. **Trafo (Transformador)**
   - Representa fonte de alimentação
   - Tensão: 380V (padrão trifásico)

2. **Barramento Principal**
   - Linha grossa horizontal
   - Distribui energia

3. **Fases (A, B, C)**
   - Código de cores:
     - 🔴 **Fase A:** Vermelho
     - 🟡 **Fase B:** Amarelo
     - 🔵 **Fase C:** Azul
   - 🟢 **Neutro:** Verde/Branco
   - 🟤 **Terra:** Marrom/Preto

4. **Disjuntor**
   - Proteção do circuito
   - Corrente nominal indicada

5. **Condutor**
   - Seção e material especificados
   - Cores conforme fases

6. **Carga**
   - Ponto de consumo
   - Símbolos conforme tipo

7. **Aterramento**
   - Representado por linhas cruzadas
   - Referência de segurança

### Dados Inclusos no Diagrama

```
┌─────────────────────────────────┐
│ DIAGRAMA UNIFILAR               │
├─────────────────────────────────┤
│ Seção: 2.5 mm² (Cobre)          │
│ Ampacidade: 18.5 A              │
│ Corrente Ajustada: 15.0 A       │
│ Queda Tensão: 1.8%              │
│ Método Instalação: B1           │
│ Data: 31/01/2026                │
└─────────────────────────────────┘
```

### Exemplo PNG Gerado

```
              TRAFO 380V
                  |
    ──────────────────────────────
    |          |          |
   [ ]        [ ]        [ ]
   Disj       Disj       Disj
    |          |          |
  ─ ─        ─ ─        ─ ─
   │          │          │
┌──┴──┐    ┌──┴──┐    ┌──┴──┐
│CARG │    │CARG │    │CARG │
└─────┘    └─────┘    └─────┘

    |
   GND (Aterramento)
```

### Configurações de Exportação

#### PNG (Matplotlib)
- Resolução: 300 DPI (alta qualidade)
- Formato: RGB
- Fundo: Branco
- Tamanho: ~14x8 polegadas

#### PDF (ReportLab)
- Página: A4
- Margens: 50mm
- Fonte: Helvetica
- Compressão: Padrão

#### DWG (EzDXF)
- Versão: AutoCAD 2010 R2
- Camadas: Fases, Disjuntores, Condutores, Texto
- Unidades: mm
- Escala: 1:50 (típica)

### Requisitos de Instalação

Para funcionalidade completa, instale:

```bash
pip install -r requirements.txt
```

Ou manualmente:

```bash
# Básico (sempre necessário)
pip install streamlit numpy pandas openpyxl matplotlib

# Para PDF (opcional)
pip install reportlab

# Para DWG (opcional)
pip install ezdxf
```

---

## 📊 Comparação de Funcionalidades

| Recurso | PNG | PDF | DWG |
|---------|-----|-----|-----|
| Visualização | ✅ | ✅ | ✅ |
| Impressão | ✅ | ✅ | ✅ |
| Edição | ❌ | ⚠️ | ✅ |
| CAD | ❌ | ❌ | ✅ |
| Tamanho arquivo | 📄 | 📄 | 📄 |
| Compatibilidade | 🌐 | 🌐 | 🏗️ |
| Instalação obrigatória | ✅ | ⚠️ | ⚠️ |

---

## 🔧 Troubleshooting

### "ReportLab não instalado"
**Solução:**
```bash
pip install reportlab
```

### "EzDXF não instalado"
**Solução:**
```bash
pip install ezdxf
```

### "DWG não abre no AutoCAD"
**Solução:**
- Versão AutoCAD 2010 ou superior
- Tente converter: `ezdxf` compatível com R2010+
- Verifique se arquivo não está corrompido

### "PDF vem em branco"
**Solução:**
- Verificar se ReportLab está instalado
- Tentar novamente
- Clicar no botão "Gerar PDF" novamente

---

## 💡 Dicas de Uso

### Balanceamento:
1. Sempre que possível, balanceie para 0% de desbalanceamento
2. Circuitos trifásicos críticos: máximo 1-2%
3. Residências: 3% é aceitável
4. Use gráfico para visualizar distribuição

### Unifilar:
1. Exporte PNG para apresentações e emails
2. Exporte PDF para documentação e arquivo
3. Exporte DWG para integração com outros projetos
4. Sempre inclua data no nome do arquivo
5. Mantenha versões em histórico

---

## 📈 Próximas Melhorias

Funcionalidades planejadas para v4.0:

- [ ] Geração de múltiplos circuitos em um unifilar
- [ ] Proteção equipotencial automática
- [ ] Cálculo de corrente de falta por fase
- [ ] Sugestões de balanceamento automáticas
- [ ] Exportação para BIM (Revit)
- [ ] QR code com dados do projeto
- [ ] Histórico de versões
- [ ] Assinatura digital

---

## 📝 Normas Consultadas

- **NBR 5410** - Desbalanceamento máximo 3%
- **NBR 5356** - Seleção de transformadores
- **IEC 60909** - Correntes de falta
- **ISO 1219-1** - Símbolos de diagrama hidráulico
- **EN 60617-12** - Símbolos elétricos

---

**Versão:** 3.0  
**Data:** Janeiro 2026  
**Status:** ✅ COMPLETO
