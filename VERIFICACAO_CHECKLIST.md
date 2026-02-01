# ✅ Checklist de Verificação - EletriCalcPro v4.2

## 🔧 Pré-Instalação

- [ ] Python 3.8+ instalado
  - Verificar: `python --version` ou `python3 --version`
  - Deve mostrar: Python 3.8.0 ou superior

- [ ] pip disponível
  - Verificar: `pip --version`
  - Deve mostrar: pip X.X.X

- [ ] Git instalado (opcional mas recomendado)
  - Verificar: `git --version`

---

## 📦 Instalação

### Windows (PowerShell)
- [ ] Abri PowerShell como Administrador
- [ ] Naveguei até: `EletriCalcPro-Beta\projeto`
- [ ] Executei: `.\install.ps1`
- [ ] Sem erros durante instalação
- [ ] Vejo: "✅ Instalação bem-sucedida!"

### Linux / macOS
- [ ] Naveguei até: `EletriCalcPro-Beta/projeto`
- [ ] Executei: `bash install.sh`
- [ ] Sem erros durante instalação
- [ ] Vejo: "✅ Instalação bem-sucedida!"

---

## 🧪 Testes Pós-Instalação

### 1. Testar Ambiente Virtual
```bash
# Windows:
venv\Scripts\activate.bat

# Linux/macOS:
source venv/bin/activate
```
- [ ] Prompt do terminal mudou (agora mostra `(venv)`)
- [ ] Nenhum erro

### 2. Testar Imports
```bash
python -c "import streamlit; import pandas; import matplotlib; print('✅ OK')"
```
- [ ] Saída: `✅ OK`
- [ ] Nenhum ModuleNotFoundError

### 3. Iniciar Aplicação
```bash
streamlit run app.py
```
- [ ] Mensagem: "You can now view your Streamlit app in your browser"
- [ ] URL: `http://localhost:8501`
- [ ] Navegador abriu automaticamente (ou abre manual)

---

## 🌐 Teste da Interface

### Sidebar (Barra Lateral Esquerda)
- [ ] Título "📁 Sistema de Projetos" visível
- [ ] 3 abas: "Novo", "Carregador", "Ferramentas"
- [ ] Sem erros JavaScript no console

### Aba Principal
- [ ] Título: "⚡ Software Profissional para Projetos Elétricos"
- [ ] Aviso inicial: "Selecione ou crie um projeto"
- [ ] 7 abas: Condutores, Transformadores, Disjuntores, etc.

### Criar Projeto
- [ ] Clique na aba "Novo" do sidebar
- [ ] Preencha: Nome, Cliente, Local
- [ ] Clique "✅ Criar Projeto"
- [ ] Mensagem: "✅ Projeto 'XXX' criado!"
- [ ] Projeto aparece no sidebar como ativo

### Usar um Módulo (Condutores)
- [ ] Clique em "📦 Condutores"
- [ ] Preencha campos (ex: 20A, 380V, 50m)
- [ ] Clique "🔄 Calcular Dimensionamento"
- [ ] Resultados aparecem com métricas
- [ ] Status mostra "✅ DIMENSIONAMENTO CONFORME"
- [ ] Botões de exportação aparecem

### Exportar
- [ ] Clique "📊 Excel"
- [ ] Arquivo é baixado
- [ ] Salve e abra em Excel ou LibreOffice
- [ ] Dados estão corretos

- [ ] Clique "📄 Relatório"
- [ ] Arquivo é baixado
- [ ] Conteúdo é legível

### Salvar no Projeto
- [ ] Após calcular, clique "💾 Salvar no Projeto"
- [ ] Mensagem: "✅ Circuito 'XXX' salvo no projeto!"

---

## 🔍 Verificação Técnica

### Console JavaScript (F12 ou Ctrl+Shift+I)
- [ ] Aba "Console"
- [ ] ❌ NÃO deve conter erros vermelhos
- [ ] ❌ Especialmente: "NotFoundError" ou "removeChild"
- [ ] ⚠️ Avisos (amarelos) são aceitáveis

### Network (Aba Network do Developer Tools)
- [ ] ❌ Nenhuma requisição em vermelho (erros)
- [ ] Status 200 ou 304 para respostas

### Performance
- [ ] Aplicação responde em < 2 segundos
- [ ] Sem travamentos
- [ ] Gráficos renderizam corretamente

---

## 📊 Testes de Funcionalidade

### Módulo de Condutores ✅
- [ ] Campo "Corrente" aceita números
- [ ] Campo "Tensão" funciona
- [ ] Cálculo retorna resultado
- [ ] Exportação Excel funciona

### Módulo de Transformadores ✅
- [ ] Campos de entrada funcionam
- [ ] Tabela comparativa aparece
- [ ] Recomendação está correta
- [ ] Status conforme é mostrado

### Sidebar - Ferramentas ✅
- [ ] Botão "Exportar" baixa CSV
- [ ] Histórico contém operações

---

## 🚨 Problemas Conhecidos (Resolvidos em v4.2)

### ❌ Problema: "No module named 'matplotlib'"
- **Status:** ✅ RESOLVIDO
- **Verificação:** Se vir este erro, requirements.txt não foi aplicado
- **Solução:** `pip install matplotlib`

### ❌ Problema: "NotFoundError removeChild"
- **Status:** ✅ RESOLVIDO
- **Verificação:** Se vir isto em F12, é v4.1 antiga
- **Solução:** Atualize para v4.2

### ❌ Problema: "Porta 8501 em uso"
- **Status:** ✅ ESPERADO
- **Verificação:** Rodou Streamlit e agora não sai?
- **Solução:** `streamlit run app.py --server.port 8502`

---

## 📋 Verificação Final

### Checklist de Produção
- [ ] ✅ Todos os testes passaram
- [ ] ✅ Sem erros JavaScript
- [ ] ✅ Performance satisfatória
- [ ] ✅ Documentação lida (INICIO_RAPIDO.md)
- [ ] ✅ Primeira execução testada
- [ ] ✅ Pode começar a usar!

---

## 🎓 Próximos Passos

1. **Ler documentação:** INICIO_RAPIDO.md
2. **Criar projeto:** Seguir passo-a-passo no sidebar
3. **Fazer um cálculo:** Usar um módulo (ex: Condutores)
4. **Exportar resultado:** Excel ou Relatório
5. **Guardar no projeto:** Botão Salvar

---

## 💬 Se Algo Não Funcionar

1. **Verifique a documentação:**
   - INSTALACAO_EXECUCAO.md (seção Troubleshooting)
   - INICIO_RAPIDO.md (FAQ)

2. **Passos de troubleshooting:**
   - [ ] Feche a aplicação (Ctrl+C)
   - [ ] Desative/reative ambiente virtual
   - [ ] Delete pasta `__pycache__` se existir
   - [ ] Reinstale: `pip install -r requirements.txt`
   - [ ] Inicie novamente: `streamlit run app.py`

3. **Se persistir:**
   - Consulte console de erro completo
   - Verifique versão Python (deve ser 3.8+)
   - Verifique que está na pasta certa

---

## 🏆 Status de Verificação

| Item | Status | Observação |
|------|--------|-----------|
| Instalação | ✅ | Scripts funcionam |
| Imports | ✅ | Todos disponíveis |
| Interface | ✅ | Sem erros DOM |
| Módulos | ✅ | 7 abas operacionais |
| Projeto | ✅ | Sistema funcional |
| Exportação | ✅ | 3 formatos |
| Documentação | ✅ | Completa em português |
| Produção | ✅ | Pronto para usar |

---

## 🎉 Parabéns!

Se todos os itens foram marcados como ✅, sua instalação está **100% funcional**!

**Agora você pode começar a usar EletriCalcPro v4.2 para seus projetos elétricos profissionais!**

---

**Dúvidas?** Consulte a documentação completa em:
- INSTALACAO_EXECUCAO.md
- INICIO_RAPIDO.md
- GUIA_USO.md

**Boa sorte! ⚡**
