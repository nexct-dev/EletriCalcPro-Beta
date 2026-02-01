# 🚀 Guia Rápido - Workflows Profissionais v5.0

## 📍 O que é novo?

A versão 5.0 transforma o EletriCalcPro em um **sistema profissional de projetos** onde:

✅ **Cada cálculo é parte de um projeto**  
✅ **Todas as abas seguem o mesmo padrão**  
✅ **Histórico completo é mantido automaticamente**  
✅ **Exportação em múltiplos formatos**  

---

## 🎯 Começar em 3 Passos

### Passo 1: Criar um Projeto

1. Abra o app na barra lateral à esquerda
2. Selecione **\"📝 Novo Projeto\"**
3. Preencha:
   - **Nome:** Ex: \"Edifício Comercial - Andar 5\"
   - **Cliente:** Ex: \"Empresa ABC\"
   - **Local:** Ex: \"São Paulo - SP\"
   - **Descrição:** (opcional)
4. Clique **\"✅ Criar Projeto\"**

### Passo 2: Usar uma Aba (ex: Condutores)

1. Vá até a aba **\"📦 Condutores\"**
2. Preencha as 3 seções:
   - **Identificação:** Nome do circuito, tipo, local
   - **Parâmetros Elétricos:** Corrente, tensão, queda máxima
   - **Instalação:** Método, comprimento, agrupamento
3. Clique **\"🔄 Calcular\"**
4. Veja os **resultados em tempo real**
5. Clique **\"💾 Salvar no Projeto\"**

### Passo 3: Exportar Resultados

1. Após calcular, clique em:
   - **\"📊 Excel\"** → Baixa arquivo .xlsx profissional
   - **\"📄 Relatório\"** → Baixa texto formatado
   - **\"👁️ Visualizar\"** → Abre visualização

---

## 📊 Estrutura de Cada Aba

Todas as 4 abas seguem este padrão:

```
┌─────────────────────────────────────────┐
│  SEÇÃO 1: IDENTIFICAÇÃO                 │
│  ├─ Nome, tipo, número, local           │
├─────────────────────────────────────────┤
│  SEÇÃO 2-3: PARÂMETROS E OPÇÕES         │
│  ├─ Dados técnicos do projeto           │
├─────────────────────────────────────────┤
│  SEÇÃO 4: PROCESSAMENTO                 │
│  ├─ Calcular | Salvar                   │
├─────────────────────────────────────────┤
│  SEÇÃO 5: RESULTADO                     │
│  ├─ ✅ Status                            │
│  ├─ 📊 Métricas principais              │
│  ├─ ⚠️  Alertas técnicos                 │
├─────────────────────────────────────────┤
│  SEÇÃO 6: ANÁLISE (opcional)            │
│  ├─ Tabela comparativa                  │
├─────────────────────────────────────────┤
│  SEÇÃO 7: EXPORTAÇÃO                    │
│  ├─ 📊 Excel | 📄 Relatório | 👁️ Ver   │
└─────────────────────────────────────────┘
```

---

## 🎨 Cores e Ícones

| Cor | Significado |
|-----|------------|
| 🟢 ✅ | Conforme (OK) |
| 🟡 ⚠️ | Atenção (verificar) |
| 🔴 ❌ | Erro (não conforme) |
| 🔵 ℹ️ | Informação (dica) |

---

## 📥 Exemplo Completo

### Cenário: Dimensionar condutor para iluminação de corredor

**Dados:**
- Corrente: 15 A
- Comprimento: 30 m
- Tensão: 380 V
- Queda máxima: 3%

**Procedimento:**

```
1. Sidebar → Criar projeto "Prédio Comercial"
   ✅ Projeto criado

2. Aba 1 → Identificação
   Nome: "Iluminação Corredor"
   Tipo: "Iluminação"
   Nº: "1"
   Local: "Corredor"

3. Aba 1 → Parâmetros Elétricos
   Corrente: 15 A
   Tensão: 380 V
   Queda: 3%
   Material: Cobre

4. Aba 1 → Instalação
   Método: Eletroduto Embutido
   Comprimento: 30 m
   Agrupamento: 1 circuito
   Temperatura: 100%

5. Clique \"Calcular\"

   📊 RESULTADO:
   ├─ ✅ Conforme
   ├─ Seção: 2.5 mm²
   ├─ Ampacidade: 18.5 A
   ├─ Queda Real: 2.1%
   ├─ Margem: 23%
   └─ Status: OK

6. Clique \"Salvar no Projeto\"
   ✅ Circuito \"Iluminação Corredor\" salvo!

7. Clique \"Excel\" para exportar
   ✅ Arquivo baixado: \"condutor_Iluminacao_Corredor_15122024.xlsx\"
```

---

## 🔧 Dicas Profissionais

### Dica 1: Identificação Clara
Use nomes descritivos para facilitar depois:
- ❌ Errado: \"C1\", \"Circuito 1\"
- ✅ Correto: \"Iluminação Corredor 5º Andar\", \"Tomada Escritório\"

### Dica 2: Margens de Segurança
Use valores conservadores:
- **Condutores:** Queda máxima 3% (até 50 m)
- **Transformadores:** Margem 20-30% de crescimento
- **Disjuntores:** Padrão C para circuitos comuns

### Dica 3: Conformidade Normativa
Todos os cálculos seguem:
- **NBR 5410** (Condutores, Disjuntores)
- **NBR 5356** (Transformadores)
- **IEC 60909** (Curto-circuito)

### Dica 4: Histórico de Cálculos
Vá em **\"💾 Ferramentas\"** e **\"💾 Exportar Histórico\"** para obter:
- CSV com todos os 100+ cálculos
- Timestamp de cada operação
- Status de conformidade

### Dica 5: Seletividade em Disjuntores
Na **Aba 3 (Disjuntores)**:
- Ative \"Seletividade\" para proteção coordenada
- Insira corrente de proteção montante
- Sistema verifica automaticamente

---

## 📊 Cada Aba Explicada

### Aba 1: Condutores (NBR 5410)

**Para:** Dimensionar cabos/condutores  
**Entrada:** Corrente, comprimento, tensão  
**Saída:** Seção recomendada, queda de tensão, margem  
**Novo:** Identificação do circuito + histórico  

**Exemplo:**
```
15 A, 30 m, 380 V, Queda 3%
     → Seção: 2.5 mm² ✅
```

---

### Aba 2: Transformadores (NBR 5356)

**Para:** Selecionar transformador  
**Entrada:** Potência, tensão primária/secundária, fator de demanda  
**Saída:** kVA recomendado, correntes, margem disponível  
**Novo:** Tabela comparativa de opções (100/150/200/250 kVA)  

**Exemplo:**
```
45 kW, 13.8kV→380V, Fator 0.8, Crescimento 20%
     → Trafo: 75 kVA, Margem: 37.5% ✅
```

---

### Aba 3: Disjuntores (NBR 5410)

**Para:** Selecionar protetor  
**Entrada:** Corrente, tipo, padrão, corrente de falta  
**Saída:** Corrente nominal, padrão, tipo, margem de trip  
**Novo:** Seletividade, análise de capacidade de ruptura  

**Exemplo:**
```
20 A, Geral, Padrão C, Falta 5 kA
     → Disjuntor: 25 A, Padrão C ✅
     → Margem Trip: 20%
```

---

### Aba 4: Curto-Circuito (IEC 60909)

**Para:** Calcular correntes de falta  
**Entrada:** kVA trafo, impedância, comprimento cabo  
**Saída:** Ik secundário, Ik no ponto, análise de sensibilidade  
**Novo:** 3 cenários (pior/nominal/melhor caso)  

**Exemplo:**
```
300 kVA, Uk 5%, Cabo 50m, 35mm² Cobre
     → Ik secundário: 21.8 kA
     → Ik no ponto: 14.2 kA
     → Análise: Cenários 0.85x-1.00x-0.65x ✅
```

---

## 🎓 Workflow Recomendado para Projeto Completo

1. **CRIAR PROJETO** (Sidebar)
   ```
   Nome: "Prédio Comercial Andar 5"
   Cliente: "Empresa ABC"
   ```

2. **DIMENSIONAR CONDUTORES** (Aba 1)
   ```
   Circuito 1: Iluminação 15A → 2.5 mm²
   Circuito 2: Tomadas 32A → 4 mm²
   Circuito 3: Motor 5 kW → 6 mm²
   ```

3. **SELECIONAR TRANSFORMADOR** (Aba 2)
   ```
   Potência Total: 45 kW
   Trafo: 75 kVA ✅
   ```

4. **SELECIONAR PROTEÇÃO** (Aba 3)
   ```
   Proteção Geral: 63 A
   Proteção Circuito 1: 16 A
   Proteção Circuito 2: 40 A
   ```

5. **ANALISAR CURTO-CIRCUITO** (Aba 4)
   ```
   Ik secundário: 21.8 kA
   Proteção adequada: ✅
   ```

6. **EXPORTAR RELATÓRIO**
   ```
   Arquivo: Prédio_Comercial_Andar5.xlsx
   Contém: Todos os 4 módulos com cálculos
   ```

---

## ❓ FAQ - Perguntas Frequentes

**P: Posso ter múltiplos projetos?**  
R: Sim! Na sidebar, mude para \"📂 Carregar Projeto\" para abrir outro.

**P: Onde ficam salvos os projetos?**  
R: Na memória da sessão Streamlit. Para salvar permanente, use \"Excel\".

**P: Posso modificar um cálculo já salvo?**  
R: Sim, os dados ficam em session_state durante a sessão. Para próxima sessão, reimporte o Excel.

**P: Como acessar o histórico?**  
R: Sidebar → \"💾 Ferramentas\" → \"💾 Exportar Histórico\" → CSV com todos os cálculos.

**P: As normas são as mais recentes?**  
R: Sim! Utilizamos NBR 5410:2004, NBR 5356:2017, IEC 60909:2016.

---

## 🆘 Suporte Técnico

**Problema:** Campo de entrada não funciona  
**Solução:** Pressione Tab ou clique em outro campo

**Problema:** Resultado diz \"Não Conforme\"  
**Solução:** Veja \"⚠️ Alertas Técnicos\" abaixo do resultado

**Problema:** Não consigo salvar no projeto  
**Solução:** Crie/selecione um projeto na sidebar primeiro

**Problema:** Exportação em Excel falha  
**Solução:** Certifique-se de ter espaço em disco e permissões

---

## 📞 Contato

**Versão:** 5.0 (Workflows Profissionais)  
**Data:** Dezembro 2024  
**Status:** ✅ Pronto para produção  

---

**Bem-vindo ao EletriCalcPro 5.0! 🚀**

