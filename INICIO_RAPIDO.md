# ⚡ EletriCalcPro v4.2 - Guia de Início Rápido

## 🚀 Instalação Rápida (3 Passos)

### Windows (PowerShell)
```powershell
# 1. Entre na pasta do projeto
cd EletriCalcPro-Beta\projeto

# 2. Execute a instalação
.\install.ps1

# 3. Inicie a aplicação
streamlit run app.py
```

### Linux / macOS
```bash
# 1. Entre na pasta do projeto
cd EletriCalcPro-Beta/projeto

# 2. Execute a instalação
bash install.sh

# 3. Inicie a aplicação
streamlit run app.py
```

---

## 📖 Modo de Uso Rápido

### 1️⃣ Criar Projeto
- Abra a aplicação
- Sidebar esquerda → Aba "Novo"
- Preencha nome, cliente e local
- Clique "✅ Criar Projeto"

### 2️⃣ Usar um Módulo
**Exemplo: Dimensionar um Condutor**

1. Clique em "📦 Condutores"
2. Preencha:
   - Corrente: 20 A
   - Tensão: 380 V
   - Comprimento: 50 m
   - Material: Cobre
3. Clique "🔄 Calcular Dimensionamento"
4. Veja resultado e clique "💾 Salvar no Projeto"

### 3️⃣ Exportar Resultado
- Após calcular, clique "📊 Excel" ou "📄 Relatório"
- O arquivo será baixado automaticamente

---

## 📊 Módulos Disponíveis

| Módulo | Funcionalidade | Norma |
|--------|----------------|-------|
| 📦 Condutores | Dimensionamento de fios | NBR 5410 |
| 🔋 Transformadores | Seleção e cálculo | NBR 5356 |
| ⚙️ Disjuntores | Seleção de proteção | NBR 5410 |
| ⚡ Curto-Circuito | Cálculo de falta | IEC 60909 |
| ⚖️ Balanceamento | Distribuição de cargas | NBR 5410 |
| 📐 Unifilar | Esquema elétrico | NBR 5087 |
| 🌩️ SPDA | Proteção contra surtos | NBR 5419 |

---

## ❓ FAQ - Perguntas Frequentes

### P: A aplicação funciona sem internet?
**R:** Sim! Funciona totalmente offline.

### P: Como ativar o ambiente virtual depois?
**R:** Use:
- **Windows:** `venv\Scripts\activate.bat`
- **Linux/macOS:** `source venv/bin/activate`

### P: Posso usar em produção?
**R:** Sim! V4.2 é versão profissional com validações completas.

### P: Como salvar projetos?
**R:** Tudo é salvo na sessão automaticamente. Use "Ferramentas" para exportar histórico em CSV.

### P: Qual navegador usar?
**R:** Qualquer moderno: Chrome, Firefox, Edge, Safari.

---

## 🔍 Verificação de Instalação

Após instalar, verifique se tudo está correto:

```bash
# Ativar ambiente virtual
source venv/bin/activate  # Linux/macOS
# ou
venv\Scripts\activate.bat  # Windows

# Testar importações
python -c "import streamlit; import pandas; import matplotlib; print('✅ OK')"

# Iniciar aplicação
streamlit run app.py
```

Se tudo funcionar, verá:
```
✅ OK
You can now view your Streamlit app in your browser.
Local URL: http://localhost:8501
```

---

## 🛠️ Comando útil

### Reiniciar servidor
```bash
# Ctrl+C para parar
# Depois execute novamente:
streamlit run app.py
```

### Porta diferente
```bash
streamlit run app.py --server.port 8502
```

### Executar com host externo
```bash
streamlit run app.py --server.address 0.0.0.0
```

---

## 📚 Próximas Leituras

1. **INSTALACAO_EXECUCAO.md** - Guia completo
2. **GUIA_USO.md** - Manual detalhado
3. **EXEMPLOS_PRATICOS.md** - Casos reais
4. **TABELAS_NBR5410.md** - Referências técnicas

---

## 💡 Dicas de Uso

✅ **Use nomes descritivos** para projetos
✅ **Salve frequentemente** cada cálculo
✅ **Exporte** resultados para documentação
✅ **Consulte normas** para validar dados
✅ **Reutilize projetos** como templates

---

## 🎯 Próximas Versões

### v4.3 (Planejado)
- [ ] API REST para integração
- [ ] Banco de dados de projetos
- [ ] Sincronização em nuvem
- [ ] Aplicativo mobile

---

**Pronto para começar? Execute `streamlit run app.py` e aproveite! ⚡**

Dúvidas? Consulte a documentação completa em INSTALACAO_EXECUCAO.md
