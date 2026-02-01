# 📚 Índice de Documentação - EletriCalcPro v2.0

Bem-vindo ao EletriCalcPro! Este arquivo te ajudará a navegar pela documentação e começar a usar o software.

---

## 🚀 Comece Aqui

### Primeiro acesso?
1. Leia: [GUIA_USO.md](GUIA_USO.md) - 📘 Manual completo da interface
2. Veja: [EXEMPLOS_PRATICOS.md](EXEMPLOS_PRATICOS.md) - 💡 Casos reais de uso
3. Execute: `streamlit run app.py` - ▶️ Inicialize o software

### Quer entender as tabelas?
1. Leia: [TABELAS_NBR5410.md](TABELAS_NBR5410.md) - 📋 Explicação técnica completa
2. Consulte: [EXEMPLOS_PRATICOS.md](EXEMPLOS_PRATICOS.md) - 🧮 Cálculos passo-a-passo

### Buscando informações rápidas?
1. Ver [RESUMO_MELHORIAS.md](RESUMO_MELHORIAS.md) - ✨ O que foi implementado

---

## 📋 Arquivos da Documentação

### 1. **GUIA_USO.md** - 📘 Guia Completo
**Para:** Usuários finais, engenheiros, técnicos  
**Conteúdo:**
- Interface explicada em detalhes
- Cada parâmetro de entrada descrito
- Como interpretar resultados
- Dicas e boas práticas
- Passo-a-passo de cálculo

**Quando usar:**
- Primeira vez usando o software
- Dúvida sobre um parâmetro
- Entender um resultado

---

### 2. **TABELAS_NBR5410.md** - 📋 Referência Técnica
**Para:** Engenheiros, projetistas, formadores  
**Conteúdo:**
- Explicação teórica de cada tabela
- Tabela 33 (métodos de instalação)
- Tabela 36 (capacidade de condução)
- Tabela 42 (fatores de agrupamento)
- Tabela 46 (condutores carregados)
- Exemplo completo passo-a-passo
- Limitações e considerações

**Quando usar:**
- Entender a fundamentação das tabelas
- Verificar ampacidades de referência
- Ensinar sobre NBR 5410

---

### 3. **EXEMPLOS_PRATICOS.md** - 💡 Casos de Uso Reais
**Para:** Todos os usuários  
**Conteúdo:**
- 5 exemplos práticos completos
- Circuito de iluminação
- Tomada especial (ar condicionado)
- Circuito trifásico
- Cabo enterrado
- Comparação cobre vs alumínio
- Dicas práticas
- Checklist

**Quando usar:**
- Procurando inspiração para um problema
- Quer ver um cálculo completo
- Necessita validar seus resultados

---

### 4. **RESUMO_MELHORIAS.md** - ✨ O que foi Implementado
**Para:** Gerentes de projeto, desenvolvedores, usuários técnicos  
**Conteúdo:**
- Resumo das 4 tabelas NBR 5410 integradas
- Funções novas e melhoradas
- Mudanças na interface
- Documentação criada
- Dados inclusos
- Validações implementadas
- Próximos passos sugeridos

**Quando usar:**
- Entender as mudanças da versão 2.0
- Ver o escopo do projeto
- Planejar futuras melhorias

---

### 5. **app.py** - 💻 Código Principal
**Para:** Desenvolvedores  
**Conteúdo:**
- Implementação em Python/Streamlit
- Tabelas NBR 5410 integradas
- Funções de cálculo
- Interface web

**Como usar:**
```bash
streamlit run app.py
```

---

## 🎯 Fluxo de Aprendizagem Recomendado

### Iniciante:
```
GUIA_USO.md 
    ↓
EXEMPLOS_PRATICOS.md (Ex. 1 - Iluminação)
    ↓
Usar o software
    ↓
EXEMPLOS_PRATICOS.md (Ex. 2-5)
    ↓
TABELAS_NBR5410.md
```

### Engenheiro/Projetista:
```
TABELAS_NBR5410.md
    ↓
EXEMPLOS_PRATICOS.md
    ↓
Usar o software
    ↓
GUIA_USO.md (referência)
```

### Desenvolvedor:
```
RESUMO_MELHORIAS.md
    ↓
app.py
    ↓
TABELAS_NBR5410.md (referência técnica)
```

---

## 🔍 Encontrar Informações Rápidas

### "Como uso o software?"
→ [GUIA_USO.md](GUIA_USO.md) - Seção: Interface Principal

### "O que é Tabela 36?"
→ [TABELAS_NBR5410.md](TABELAS_NBR5410.md) - Seção: Tabela 36

### "Qual fator aplicar para 4 circuitos?"
→ [TABELAS_NBR5410.md](TABELAS_NBR5410.md) - Seção: Tabela 42  
Resposta: **0.65**

### "Como calcular seção?"
→ [TABELAS_NBR5410.md](TABELAS_NBR5410.md) - Seção: Cálculo Prático  
ou  
→ [EXEMPLOS_PRATICOS.md](EXEMPLOS_PRATICOS.md) - Exemplo 1

### "Qual seção para 20A em 30m?"
→ [EXEMPLOS_PRATICOS.md](EXEMPLOS_PRATICOS.md) - Exemplo 1: Iluminação Residencial

### "O que mudou na versão 2.0?"
→ [RESUMO_MELHORIAS.md](RESUMO_MELHORIAS.md) - Início do documento

### "Quais parâmetros preciso fornecer?"
→ [GUIA_USO.md](GUIA_USO.md) - Seção: Parâmetros de Entrada

---

## 📊 Tabelas de Referência Rápida

### Métodos de Instalação (Tabela 33)
| Código | Nome | Quando Usar |
|--------|------|-----------|
| A1 | Condutor Visível | Áreas abertas |
| B1 | Eletroduto Embutido | **Padrão residencial** |
| B2 | Eletroduto Superfície | Áreas molhadas |
| C | Eletrocalha | Painéis |
| D | Bandeja | Múltiplos circuitos |
| E | Enterrado | Externo, subterrâneo |

### Fatores de Agrupamento (Tabela 42)
| Circuitos | Fator | Redução |
|-----------|-------|---------|
| 1 | 1.00 | 0% |
| 2 | 0.80 | 20% |
| 3 | 0.70 | 30% |
| 4 | 0.65 | 35% |
| 9+ | 0.50 | 50% |

### Seções Padrão
**Cobre:** 1.5 | 2.5 | 4 | 6 | 10 | 16 | 25 | 35 | 50 | 70 | 95 | 120 | 150 | 185 | 240 mm²  
**Alumínio:** 2.5 | 4 | 6 | 10 | 16 | 25 | 35 | 50 | 70 | 95 | 120 | 150 | 185 | 240 mm²

### Queda de Tensão Recomendada
| Tipo | Máximo | Recomendado |
|------|--------|-------------|
| Geral | 3% | 2.5% |
| Iluminação | 3% | 2% |
| Força | 3% | 3% |
| Críticos | - | 1-2% |

---

## 💻 Requisitos Técnicos

### Instalação:
```bash
pip install streamlit numpy pandas openpyxl
```

### Executar:
```bash
cd projeto
streamlit run app.py
```

### Requisitos:
- Python 3.7+
- Streamlit 1.0+
- NumPy
- Pandas
- OpenPyXL

---

## 📞 Dúvidas e Suporte

### Questão: "O resultado está correto?"
**Passos de verificação:**
1. Verifique o cálculo em [EXEMPLOS_PRATICOS.md](EXEMPLOS_PRATICOS.md)
2. Consulte [GUIA_USO.md](GUIA_USO.md) - Seção: Validação de Resultados
3. Verifique se há alertas no software

### Questão: "Como entendo uma tabela?"
**Solução:**
1. Leia [TABELAS_NBR5410.md](TABELAS_NBR5410.md)
2. Veja o exemplo na mesma seção
3. Teste no software com valores diferentes

### Questão: "Que seção usar em meu caso?"
**Solução:**
1. Encontre um caso similar em [EXEMPLOS_PRATICOS.md](EXEMPLOS_PRATICOS.md)
2. Use o software com seus dados
3. Verifique o resultado
4. Exporte para documentação

---

## ✅ Verificação Antes de Usar

Antes de usar o software em produção, verifique:

- [ ] Leu [GUIA_USO.md](GUIA_USO.md)
- [ ] Viu [EXEMPLOS_PRATICOS.md](EXEMPLOS_PRATICOS.md)
- [ ] Entendeu as tabelas em [TABELAS_NBR5410.md](TABELAS_NBR5410.md)
- [ ] Testou com exemplo conhecido
- [ ] Comparou resultado com cálculo manual
- [ ] Verificou conformidade com NBR 5410
- [ ] Tem certificação/preparação adequada
- [ ] Entendeu limitações do software

---

## 📈 Nível de Profundidade

### Nível 1 - Uso Básico
- Tempo: 30 minutos
- Arquivo: [GUIA_USO.md](GUIA_USO.md)
- Resultado: Consegue usar a interface

### Nível 2 - Uso Prático
- Tempo: 2 horas
- Arquivos: [GUIA_USO.md](GUIA_USO.md) + [EXEMPLOS_PRATICOS.md](EXEMPLOS_PRATICOS.md)
- Resultado: Consegue dimensionar cabos

### Nível 3 - Entendimento Técnico
- Tempo: 4 horas
- Arquivos: Todos
- Resultado: Entende a fundamentação técnica

### Nível 4 - Desenvolvimento
- Tempo: 1 dia
- Arquivos: Todos + código
- Resultado: Consegue estender o software

---

## 🎓 Para Ensino/Treinamento

### Aula 1 - Introdução (50 min)
- [GUIA_USO.md](GUIA_USO.md) - Primeiras seções
- Demonstração do software

### Aula 2 - Tabelas NBR 5410 (90 min)
- [TABELAS_NBR5410.md](TABELAS_NBR5410.md)
- Explicação de cada tabela
- Exemplo de cálculo

### Aula 3 - Prática (90 min)
- [EXEMPLOS_PRATICOS.md](EXEMPLOS_PRATICOS.md)
- Casos 1-3 (simples)
- Exercícios

### Aula 4 - Avançado (90 min)
- [EXEMPLOS_PRATICOS.md](EXEMPLOS_PRATICOS.md)
- Casos 4-5 (complexos)
- Projeto prático

---

## 📝 Manutenção da Documentação

Última atualização: **Janeiro 2026**

### Versão: 2.0
- ✅ Tabelas NBR 5410 integradas
- ✅ Documentação completa
- ✅ Exemplos práticos
- ✅ Guia de uso

### Próximas versões
- 🔄 Melhorias na interface
- 🔄 Mais tabelas
- 🔄 Integração com CAD

---

## 🙏 Créditos

**Software:** EletriCalcPro  
**Versão:** 2.0  
**Norma:** NBR 5410:2004  
**Última atualização:** Janeiro 2026

---

**Pronto para começar? 👉 [Abra o GUIA_USO.md](GUIA_USO.md)**
