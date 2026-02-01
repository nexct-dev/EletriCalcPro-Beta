# ⚡ GUIA RÁPIDO - ABA 5 EXPANDIDA (v4.1)

**Nova Funcionalidade:** Dimensionamento de Condutor + Geração de Unifilar

---

## 3 Passos Rápidos

### Passo 1️⃣: Balanceamento de Fases (Como Antes)

```
1. Abra a Aba 5: "⚖️ Balanceamento de Fases"

2. Insira as cargas em kW:
   ├─ Fase A: [2.0] [1.5] [2.5]  (3 cargas)
   ├─ Fase B: [2.0] [2.0] [2.0]  (3 cargas)
   └─ Fase C: [2.5] [1.5] [2.0]  (3 cargas)

3. Clique "Calcular Balanceamento"

4. Verifique resultado:
   ✓ Se desbalanceamento < 3% → OK
   ⚠️ Se > 3% → Use sugestões para rebalancear
```

### Passo 2️⃣: Dimensionamento de Condutor (NOVO v4.1)

```
1. Após calcular balanceamento, role para baixo

2. Você verá a seção: "🔧 Dimensionamento e Unifilar"

3. Preencha os dados:
   ├─ Nome do Circuito: "Principal"
   ├─ Tipo de Circuito: "Trifásico Com Neutro"
   ├─ Comprimento (m): 30
   └─ Queda de Tensão Máxima (%): 3.0

4. Clique "📊 Dimensionar Condutor (NBR 5410)"

5. Aparecem campos adicionais:
   ├─ Material: "Cobre" (ou Alumínio)
   └─ Tipo Instalação: "Eletroduto Embutido (B1)"

6. Visualize o resultado:
   ├─ Seção: 6 mm² ✓
   ├─ Ampacidade: 41 A
   ├─ Queda Real: 2.8%
   └─ Status: ✓ Conforme NBR 5410
```

### Passo 3️⃣: Gerar Diagrama Unifilar (NOVO v4.1)

```
1. Na seção "📐 Gerar Esquema Unifilar", você verá 3 botões:

   [🖼️ PNG]   [📄 PDF]   [🔧 DWG]

2. Clique no formato desejado:

   PNG:
   ├─ ✓ Sempre funciona
   ├─ Resolução: 300 DPI
   └─ Baixar e usar em presentations

   PDF:
   ├─ ⚠️ Requer: pip install reportlab
   ├─ Formato: A4 profissional
   └─ Ideal para impressão

   DWG:
   ├─ ⚠️ Requer: pip install ezdxf
   ├─ Formato: AutoCAD
   └─ Editar em CAD profissional

3. Download automático do arquivo

4. Use no seu projeto!
```

---

## 📊 O Que Muda na Aba 5

### Antes (v4.0):
```
Cargas por Fase
    ↓
Calcular Balanceamento
    ↓
Ver Sugestões
    ↓ FIM
```

### Depois (v4.1):
```
Cargas por Fase
    ↓
Calcular Balanceamento
    ↓
Ver Sugestões
    ↓
✨ Inserir Dados Circuito
    ↓
✨ Dimensionar Condutor NBR 5410
    ↓
✨ Gerar Unifilar (PNG/PDF/DWG)
    ↓
✨ Baixar Arquivos
    ↓ TUDO EM UMA ABA!
```

---

## 💡 Exemplos Rápidos

### Exemplo 1: Residência Simples

**Entrada:**
```
Fase A: 3.0 kW
Fase B: 3.0 kW
Fase C: 3.0 kW
Perfeitamente balanceado!

Circuito:
├─ Nome: "Distribuição Residencial"
├─ Tipo: "Trifásico Com Neutro"
├─ Comprimento: 20m
└─ Queda Máx: 3%
```

**Resultado:**
```
✓ Desbalanceamento: 0% (OK!)
✓ Condutor: 4 mm² Cobre
✓ Ampacidade: 32 A
✓ Queda: 1.5%
✓ Conforme NBR 5410

↓ Download
├─ residencial.png (PNG)
├─ residencial.pdf (PDF)
└─ residencial.dwg (DWG)
```

### Exemplo 2: Edifício Comercial

**Entrada:**
```
Fase A: 15.0 kW
Fase B: 12.0 kW
Fase C: 14.0 kW
Desbalanceamento: 8% ⚠️

Sugestão gerada:
├─ Mover 1.5 kW de A → B
└─ Mover 0.5 kW de C → B

Após rebalancear:
Fase A: 13.5 kW
Fase B: 13.5 kW
Fase C: 14.0 kW
Desbalanceamento: 1.9% ✓ OK!

Circuito:
├─ Nome: "Distribuição Comercial"
├─ Tipo: "Trifásico Com Neutro"
├─ Comprimento: 50m
└─ Queda Máx: 3%
```

**Resultado:**
```
✓ Condutor: 25 mm² Cobre
✓ Ampacidade: 99 A
✓ Queda: 2.8%
✓ Conforme NBR 5410

↓ Download 3 formatos
```

---

## 🎯 Tipos de Circuito Disponíveis

| Tipo | Uso | Exemplo |
|:---|:---|:---|
| **Monofásico 2 Fios** | Circuito simples | Tomada 127V |
| **Monofásico 3 Fios** | Com fase e neutro | Iluminação 127V |
| **Trifásico Sem Neutro** | Motor industrial | Motor 3 fases |
| **Trifásico Com Neutro** | Distribuição geral | Quadro principal |
| **Iluminação** | Luzes em geral | Lâmpadas |
| **Tomada** | Pontos de tomada | Tomadas 220V |

---

## 📥 Formatos de Saída Explicados

### PNG (Recomendado para Início)
```
✓ Quando usar:
  • Apresentações
  • Relatórios digital
  • Documentação rápida
  • Visualização na tela

✓ Vantagens:
  • Sempre funciona (sem dependências)
  • Qualidade: 300 DPI (profissional)
  • Tamanho pequeno

✓ Desvantagem:
  • Rasterizado (não edita fácil)
```

### PDF (Recomendado para Impressão)
```
⚠️ Requer instalação: pip install reportlab

✓ Quando usar:
  • Impressão em papel
  • Documentação formal
  • Arquivo permanente
  • Apresentação ao cliente

✓ Vantagens:
  • Profissional (A4)
  • Vetorial (zooma sem perder qualidade)
  • Padrão universal

✗ Se não funcionar:
  • Execute: pip install reportlab
  • Tente novamente
```

### DWG (Recomendado para Edição em CAD)
```
⚠️ Requer instalação: pip install ezdxf

✓ Quando usar:
  • Editar em AutoCAD
  • Projeto técnico completo
  • Integrar com outros desenhos
  • Alterações futuras

✓ Vantagens:
  • Abra em qualquer CAD
  • Edita facilmente
  • Camadas organizadas

✗ Se não funcionar:
  • Execute: pip install ezdxf
  • Tente novamente
```

---

## ⚙️ Instalação de Dependências (se faltar)

Se algum formato não funcionar, execute no terminal:

```bash
# Para PDF (ReportLab)
pip install reportlab

# Para DWG (EzDXF)
pip install ezdxf

# Ambos
pip install reportlab ezdxf

# Após instalar, atualize requirements.txt
pip freeze > requirements.txt
```

---

## ⚠️ Dicas Importantes

### 1️⃣ **Use Sempre Balanceamento Primeiro**
```
❌ Errado:
└─ Preencher dados circuito com cargas desbalanceadas

✅ Correto:
├─ Equilibrar fases primeiro
└─ Depois dimensionar condutor
```

### 2️⃣ **Comprimento Realista**
```
❌ Valores muito baixos (< 5m):
└─ Resultado pode ser sub-dimensionado

❌ Valores muito altos (> 200m):
└─ Condutor pode ficar muito grande

✅ Verificar:
├─ Comprimento real da instalação
└─ Incluir ida E volta
```

### 3️⃣ **Queda de Tensão**
```
NBR 5410 Recomenda:
├─ Alimentação geral: até 3%
└─ Ramais terminais: até 5% (total até 8%)

✅ Use 3% se em dúvida
```

### 4️⃣ **Material do Condutor**
```
Cobre:
├─ ✓ Melhor condutividade
├─ ✓ Menor seção necessária
└─ ✗ Mais caro

Alumínio:
├─ ✓ Mais barato
├─ ✗ Seção maior
└─ ✗ Menos condutor

Recomendação: Cobre para projetos normais
```

---

## 🔍 Como Verificar Resultado

### Checklist de Validação

```
□ Desbalanceamento < 3%?
  └─ Se SIM → continua
  └─ Se NÃO → rebalancear

□ Seção conforme NBR 5410?
  └─ Aparecer "✓ Conforme"

□ Queda Real < Máxima?
  └─ Ex: 2.8% < 3.0% ✓

□ Ampacidade > Corrente Ajustada?
  └─ Ex: 41 A > 20 A ✓

□ Sem alertas ou avisos?
  └─ Se houver, ler e validar

□ Downloads funcionaram?
  └─ Verificar pasta Downloads
```

---

## 🚀 Próximas Ações Após Gerar Unifilar

### Com o PNG:
```
1. Abrir em visualizador (foto, paint)
2. Usar em relatório/apresentação
3. Compartilhar com cliente
4. Anexar a documentação
```

### Com o PDF:
```
1. Abrir em leitor PDF
2. Imprimir se necessário
3. Salvar em arquivo de projeto
4. Enviar por email
5. Arquivar permanentemente
```

### Com o DWG:
```
1. Abrir em AutoCAD ou similar
2. Editar/adicionar detalhes
3. Integrar com outros desenhos
4. Gerar desenho final do projeto
5. Usar em licitação/orçamento
```

---

## ❓ FAQ - Dúvidas Frequentes

**P: Qual formato devo usar?**
R: PNG para rápido. PDF para profissional. DWG para CAD.

**P: Posso editar o PNG gerado?**
R: Rasterizado, difícil editar. Melhor usar PDF ou DWG.

**P: PDF não funciona, por quê?**
R: ReportLab não está instalado. Execute: `pip install reportlab`

**P: DWG não funciona, por quê?**
R: EzDXF não está instalado. Execute: `pip install ezdxf`

**P: O condutor está muito grande, está certo?**
R: Verificar: comprimento grande? queda pequena? Ambos aumentam seção.

**P: Posso usar diferentes materiais para cada fase?**
R: Não. O software usa um material para o circuito todo.

**P: Como salvou o arquivo PNG?**
R: Download automático. Verifique pasta Downloads do seu PC.

---

## 🎯 Checklist de Uso

- [ ] Aba 5 aberta
- [ ] Cargas inseridas (3 fases)
- [ ] Balanceamento calculado
- [ ] Desbalanceamento < 3% ✓
- [ ] Nome circuito preenchido
- [ ] Tipo circuito selecionado
- [ ] Comprimento inserido
- [ ] Queda máxima definida
- [ ] Botão "Dimensionar" clicado
- [ ] Material selecionado
- [ ] Instalação selecionada
- [ ] Resultado validado
- [ ] Formato desejado clicado
- [ ] Arquivo baixado
- [ ] Pronto para usar! 🎉

---

**Versão:** 4.1  
**Data:** 31 de Janeiro de 2026  
**Status:** ✅ PRONTO PARA USO

🎉 **Aproveite a nova funcionalidade!**
