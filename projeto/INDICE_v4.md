# 📚 ÍNDICE COMPLETO - EletriCalc Pro v4.0

**Última Atualização:** 31 de Janeiro de 2026  
**Versão Atual:** 4.0  
**Total de Arquivos:** 18

---

## 🎯 Guias de Início (Comece por aqui!)

### Para Usar o Software:
1. **[START_HERE.md](START_HERE.md)** - Guia de instalação e primeiros passos (v3.0)
2. **[GUIA_RAPIDO_SPDA.md](GUIA_RAPIDO_SPDA.md)** ⭐ **[NOVO v4.0]** - 3 passos rápidos para SPDA

### Para Entender:
- **[GUIA_USO.md](GUIA_USO.md)** - Manual completo de todas as funcionalidades

---

## 📊 Documentação por Norma Técnica

### NBR 5410 - Instalações Elétricas (v2.0+)
1. **[TABELAS_NBR5410.md](TABELAS_NBR5410.md)** - Referência técnica das tabelas 33, 36, 42, 46
2. **[EXEMPLOS_PRATICOS.md](EXEMPLOS_PRATICOS.md)** - 5 casos práticos de dimensionamento
3. **[RESUMO_MELHORIAS.md](RESUMO_MELHORIAS.md)** - v2.0 - Detalhes de implementação NBR 5410

### NBR 5419 - Proteção contra Descargas Atmosféricas (v4.0+) ⭐ NOVO
1. **[TABELAS_NBR5419.md](TABELAS_NBR5419.md)** ⭐ **[NOVO]** - Tabelas 1-5 com exemplos
2. **[GUIA_RAPIDO_SPDA.md](GUIA_RAPIDO_SPDA.md)** ⭐ **[NOVO]** - Guia para leigos
3. **[ATUALIZACAO_v4.md](ATUALIZACAO_v4.md)** ⭐ **[NOVO]** - Mudanças técnicas v4.0

### Outras Normas Referenciadas
- NBR 5356 - Transformadores (aba 2)
- IEC 60909 - Curto-circuito (aba 4)

---

## 🗂️ Documentação por Versão

### v1.0 - Protótipo Inicial
- Conceito base do software
- 4 abas iniciais

### v2.0 - NBR 5410 Integrada
- **[TABELAS_NBR5410.md](TABELAS_NBR5410.md)** - Tabelas 33, 36, 42, 46
- **[EXEMPLOS_PRATICOS.md](EXEMPLOS_PRATICOS.md)** - 5 exemplos reais
- **[GUIA_USO.md](GUIA_USO.md)** - Manual completo
- **[RESUMO_MELHORIAS.md](RESUMO_MELHORIAS.md)** - Changelog v2.0
- **[INDICE.md](INDICE.md)** - Índice v2.0 (antigo)
- **[CONCLUSAO.md](CONCLUSAO.md)** - Conclusão v2.0

### v3.0 - Recursos Avançados
- **[NOVAS_FUNCIONALIDADES.md](NOVAS_FUNCIONALIDADES.md)** - Balanceamento + Unifilar
- **[ATUALIZACAO_v3.md](ATUALIZACAO_v3.md)** - Detalhes v3.0
- **[START_HERE.md](START_HERE.md)** - Quick start com 3 testes
- **[install.sh](install.sh)** - Script instalação automática
- **[SUMARIO_FINAL.md](SUMARIO_FINAL.md)** - Resumo projeto v3.0

### v4.0 - SPDA (Descargas Atmosféricas) ⭐ NOVO
- **[TABELAS_NBR5419.md](TABELAS_NBR5419.md)** ⭐ **[NOVO]** - Tabelas SPDA completas
- **[GUIA_RAPIDO_SPDA.md](GUIA_RAPIDO_SPDA.md)** ⭐ **[NOVO]** - Guia prático
- **[ATUALIZACAO_v4.md](ATUALIZACAO_v4.md)** ⭐ **[NOVO]** - Mudanças técnicas
- **[CONCLUSAO_v4.md](CONCLUSAO_v4.md)** ⭐ **[NOVO]** - Resumo conclusivo v4.0

---

## 🔧 Arquivos Técnicos

### Código Fonte
- **[app.py](app.py)** - Aplicação Streamlit principal (~2.570 linhas)
  - Tabelas NBR 5410 (linhas ~50-240)
  - Tabelas NBR 5419 ⭐ (linhas ~120-230 da seção SPDA)
  - Funções de cálculo NBR 5410 (linhas ~320-500)
  - Funções de cálculo SPDA ⭐ (linhas ~1015-1165)
  - Interface 7 abas (linhas ~1171-2570)

### Dependências
- **[requirements.txt](requirements.txt)** - Pacotes Python necessários
  - streamlit, numpy, pandas, openpyxl, matplotlib, reportlab, ezdxf

### Instalação
- **[install.sh](install.sh)** - Script bash para setup automatizado

### Documentação Geral
- **[README.md](README.md)** - Apresentação do projeto

---

## 📈 Mapa de Funcionalidades por Aba

### Aba 1: 📦 Condutores (NBR 5410)
- Dimensionamento de seção
- Verificação de queda de tensão
- Cálculo de ampacidade
- Validação conforme norma
- **Arquivo:** GUIA_USO.md (seção Aba 1)

### Aba 2: 🔋 Transformadores (NBR 5356)
- Seleção de tamanho kVA
- Cálculo de correntes
- Dimensionamento de cabos primário/secundário
- **Arquivo:** GUIA_USO.md (seção Aba 2)

### Aba 3: ⚙️ Disjuntores
- Seleção por corrente
- Compatibilidade com condutor
- Padrões disponíveis
- **Arquivo:** GUIA_USO.md (seção Aba 3)

### Aba 4: ⚡ Curto-Circuito (IEC 60909)
- Cálculo de corrente de falta
- Impedância equivalente
- Contribuições
- **Arquivo:** GUIA_USO.md (seção Aba 4)

### Aba 5: ⚖️ Balanceamento de Fases (v3.0+)
- Distribuição de cargas
- Cálculo de desbalanceamento
- Verificação NBR 5410 (máx 3%)
- Sugestões de redistribuição
- **Arquivo:** NOVAS_FUNCIONALIDADES.md

### Aba 6: 📐 Esquema Unifilar (v3.0+)
- Geração diagrama PNG
- Exportação PDF (opcional)
- Exportação DWG/CAD (opcional)
- Cor-codificação de fases
- **Arquivo:** NOVAS_FUNCIONALIDADES.md

### Aba 7: ⚡ SPDA - Descargas Atmosféricas (v4.0+) ⭐ NOVO
- Dimensionamento SPDA
- Seleção classe proteção
- Cálculo condutores descida
- Material e seções
- Equipotencialização
- Corrente de descarga
- **Arquivo:** TABELAS_NBR5419.md, GUIA_RAPIDO_SPDA.md

---

## 🎯 Busca Rápida por Tópico

### Quero...

**...instalar o software**
→ [START_HERE.md](START_HERE.md) ou [install.sh](install.sh)

**...dimensionar um condutor (NBR 5410)**
→ [GUIA_USO.md](GUIA_USO.md) + [EXEMPLOS_PRATICOS.md](EXEMPLOS_PRATICOS.md)

**...dimensionar transformador**
→ [GUIA_USO.md](GUIA_USO.md) (Aba 2)

**...calcular curto-circuito**
→ [GUIA_USO.md](GUIA_USO.md) (Aba 4)

**...projetar SPDA (novo!)**
→ [GUIA_RAPIDO_SPDA.md](GUIA_RAPIDO_SPDA.md) (rápido) ou [TABELAS_NBR5419.md](TABELAS_NBR5419.md) (completo)

**...balancear fases**
→ [NOVAS_FUNCIONALIDADES.md](NOVAS_FUNCIONALIDADES.md)

**...gerar unifilar**
→ [NOVAS_FUNCIONALIDADES.md](NOVAS_FUNCIONALIDADES.md)

**...saber o que mudou em v4.0**
→ [ATUALIZACAO_v4.md](ATUALIZACAO_v4.md) ou [CONCLUSAO_v4.md](CONCLUSAO_v4.md)

**...consultar tabelas NBR 5410**
→ [TABELAS_NBR5410.md](TABELAS_NBR5410.md)

**...consultar tabelas NBR 5419**
→ [TABELAS_NBR5419.md](TABELAS_NBR5419.md) ⭐

**...ver exemplos reais**
→ [EXEMPLOS_PRATICOS.md](EXEMPLOS_PRATICOS.md)

**...entender conceitos SPDA**
→ [GUIA_RAPIDO_SPDA.md](GUIA_RAPIDO_SPDA.md)

---

## 📊 Estatísticas de Documentação

| Arquivo | Versão | Linhas | Foco |
|:---|:---:|:---:|:---|
| TABELAS_NBR5410.md | 2.0+ | 1.200 | Referência técnica |
| EXEMPLOS_PRATICOS.md | 2.0+ | 800 | Casos reais |
| GUIA_USO.md | 2.0+ | 1.500 | Manual completo |
| RESUMO_MELHORIAS.md | 2.0 | 600 | Changelog v2.0 |
| NOVAS_FUNCIONALIDADES.md | 3.0 | 600 | Novidades v3.0 |
| ATUALIZACAO_v3.md | 3.0 | 400 | Mudanças v3.0 |
| START_HERE.md | 3.0 | 500 | Quick start |
| SUMARIO_FINAL.md | 3.0 | 500 | Conclusão v3.0 |
| TABELAS_NBR5419.md | 4.0 | 2.500 | ⭐ Tabelas SPDA |
| GUIA_RAPIDO_SPDA.md | 4.0 | 400 | ⭐ Guia prático |
| ATUALIZACAO_v4.md | 4.0 | 600 | ⭐ Mudanças v4.0 |
| CONCLUSAO_v4.md | 4.0 | 500 | ⭐ Resumo v4.0 |
| **TOTAL** | | **~10.500** | |

---

## 🗺️ Mapa Visual do Projeto

```
EletriCalc Pro v4.0
│
├─ 📖 Documentação (18 arquivos)
│  ├─ Início (2 arquivos)
│  │  ├─ START_HERE.md (v3.0)
│  │  └─ GUIA_RAPIDO_SPDA.md ⭐ (v4.0)
│  │
│  ├─ NBR 5410 (5 arquivos)
│  │  ├─ TABELAS_NBR5410.md
│  │  ├─ EXEMPLOS_PRATICOS.md
│  │  ├─ GUIA_USO.md
│  │  ├─ RESUMO_MELHORIAS.md
│  │  └─ INDICE.md
│  │
│  ├─ NBR 5419 ⭐ (3 arquivos NOVO)
│  │  ├─ TABELAS_NBR5419.md
│  │  ├─ GUIA_RAPIDO_SPDA.md
│  │  └─ ATUALIZACAO_v4.md
│  │
│  ├─ Versões (6 arquivos)
│  │  ├─ ATUALIZACAO_v3.md
│  │  ├─ NOVAS_FUNCIONALIDADES.md
│  │  ├─ SUMARIO_FINAL.md
│  │  ├─ CONCLUSAO.md
│  │  ├─ CONCLUSAO_v4.md ⭐
│  │  └─ Este arquivo (INDICE_v4.md)
│  │
│  └─ Geral (3 arquivos)
│     ├─ README.md
│     ├─ install.sh
│     └─ requirements.txt
│
└─ 💻 Código (1 arquivo)
   └─ app.py (2.570 linhas)
      ├─ Tabelas NBR 5410 (~90 linhas)
      ├─ Tabelas NBR 5419 ⭐ (~120 linhas)
      ├─ Funções cálculo (~200 linhas)
      ├─ Interface Streamlit (~2.000 linhas)
      └─ 7 Abas funcionais
```

---

## 🌟 Destaques v4.0

✨ **Novo:** NBR 5419 (SPDA)  
✨ **Novo:** Aba 7 (Descargas Atmosféricas)  
✨ **Novo:** 3 documentos (2.500+ linhas)  
✨ **Melhorado:** Título software (incluindo NBR 5419)  
✨ **Sem alterações:** Todas funcionalidades v1.0-v3.0 mantidas

---

## 📅 Cronograma

| Versão | Data | Status | Foco |
|:---:|:---:|:---:|:---|
| v1.0 | Out/2025 | ✅ | Protótipo |
| v2.0 | Nov/2025 | ✅ | NBR 5410 |
| v3.0 | Dez/2025 | ✅ | Avançado (Balanceamento + Unifilar) |
| v4.0 | Jan/2026 | ✅ | **NBR 5419 (SPDA)** ⭐ |
| v5.0 | Fev/2026 | ⏳ | Em planejamento |

---

## 🚀 Próximas Expansões

- [ ] v5.0 - Integração com CAD
- [ ] v6.0 - Mais normas (NBR 5381, IEC 61439)
- [ ] v7.0 - Simulações avançadas
- [ ] v8.0 - Mobile App

---

## ❓ FAQ - Navegação

**P: Por onde começo?**  
R: Se é primeira vez → [START_HERE.md](START_HERE.md)  
Se quer SPDA novo → [GUIA_RAPIDO_SPDA.md](GUIA_RAPIDO_SPDA.md)

**P: Qual arquivo tem a informação que procuro?**  
R: Veja seção "Busca Rápida por Tópico" acima

**P: Como está organizado o app.py?**  
R: Consulte [ATUALIZACAO_v4.md](ATUALIZACAO_v4.md) seção "Estrutura de abas"

**P: Onde estão as tabelas da NBR 5419?**  
R: [TABELAS_NBR5419.md](TABELAS_NBR5419.md) com todas 5 tabelas + exemplos

**P: Como usar a nova aba SPDA?**  
R: [GUIA_RAPIDO_SPDA.md](GUIA_RAPIDO_SPDA.md) (rápido em 3 passos)

---

## 📞 Suporte

### Documentação por Nível:

**👨‍💼 Executivo**  
→ [CONCLUSAO_v4.md](CONCLUSAO_v4.md) (resumo executivo)

**👨‍💻 Usuário**  
→ [START_HERE.md](START_HERE.md) ou [GUIA_RAPIDO_SPDA.md](GUIA_RAPIDO_SPDA.md)

**👨‍🏫 Educador**  
→ [EXEMPLOS_PRATICOS.md](EXEMPLOS_PRATICOS.md) (5 casos reais)

**⚙️ Técnico**  
→ [TABELAS_NBR5410.md](TABELAS_NBR5410.md) + [TABELAS_NBR5419.md](TABELAS_NBR5419.md)

**👨‍🔬 Desenvolvedor**  
→ [ATUALIZACAO_v4.md](ATUALIZACAO_v4.md) (código + funções)

---

**Última Atualização:** 31 de Janeiro de 2026  
**Versão:** 4.0  
**Total de Documentação:** ~10.500 linhas  
**Total de Código:** ~2.570 linhas  
**Total do Projeto:** ~13.000 linhas

🎉 **Bem-vindo ao EletriCalc Pro v4.0!**
