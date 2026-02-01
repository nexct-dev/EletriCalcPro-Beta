# 🚀 Guia de Instalação e Execução - EletriCalcPro v4.2

## Visão Geral

EletriCalcPro é um software profissional para dimensionamento de projetos elétricos conforme normas brasileiras (NBR 5410, NBR 5356, NBR 5419, IEC 60909).

**Versão:** 4.2  
**Compatibilidade:** Linux, macOS, Windows  
**Linguagem:** Python 3.8+  
**Interface:** Streamlit

---

## 📋 Pré-requisitos

### Obrigatório
- **Python 3.8 ou superior** - [Baixar aqui](https://www.python.org/downloads/)
- **pip** (gerenciador de pacotes Python) - Instalado automaticamente com Python
- **Git** (opcional, para clonar o repositório)

### Recomendado
- **Terminal/Console** - cmd (Windows), Terminal (Linux/macOS), PowerShell (Windows)
- **Editor de Código** - VS Code, PyCharm ou similar (opcional)
- **Navegador Web Moderno** - Chrome, Firefox, Edge (para acessar a interface)

---

## 🔧 Instalação

### Opção 1: Linux / macOS (Recomendado)

#### 1. Clone ou baixe o repositório
```bash
# Via Git
git clone https://github.com/nexct-dev/EletriCalcPro-Beta.git
cd EletriCalcPro-Beta/projeto

# Ou baixe o ZIP e extraia
unzip EletriCalcPro-Beta.zip
cd EletriCalcPro-Beta/projeto
```

#### 2. Execute o script de instalação
```bash
bash install.sh
```

#### 3. Ative o ambiente virtual (se não ativado automaticamente)
```bash
source venv/bin/activate
```

#### 4. Execute o software
```bash
streamlit run app.py
```

#### 5. Acesse no navegador
- URL padrão: `http://localhost:8501`
- Deve abrir automaticamente

---

### Opção 2: Windows (PowerShell)

#### 1. Clone ou baixe o repositório
```powershell
# Via Git
git clone https://github.com/nexct-dev/EletriCalcPro-Beta.git
cd EletriCalcPro-Beta\projeto

# Ou extraia o ZIP manualmente
```

#### 2. Execute o script de instalação
```powershell
# Pode ser necessário permitir scripts (execute como Admin):
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Depois execute:
.\install.ps1
```

#### 3. Ative o ambiente virtual (se não ativado automaticamente)
```powershell
.\venv\Scripts\Activate.ps1
```

#### 4. Execute o software
```powershell
streamlit run app.py
```

#### 5. Acesse no navegador
- URL padrão: `http://localhost:8501`
- Deve abrir automaticamente

---

### Opção 3: Windows (Linha de Comando - cmd.exe)

#### 1. Clone ou baixe o repositório
```cmd
cd EletriCalcPro-Beta\projeto
```

#### 2. Criar ambiente virtual
```cmd
python -m venv venv
```

#### 3. Ativar ambiente virtual
```cmd
venv\Scripts\activate.bat
```

#### 4. Instalar pacotes
```cmd
pip install --upgrade pip
pip install -r requirements.txt
```

#### 5. Executar software
```cmd
streamlit run app.py
```

#### 6. Acessar no navegador
- URL: `http://localhost:8501`

---

## 📦 Instalação Manual (Sem Scripts)

Se os scripts não funcionarem:

### Linux / macOS
```bash
# 1. Criar ambiente virtual
python3 -m venv venv

# 2. Ativar ambiente
source venv/bin/activate

# 3. Instalar dependências
pip install --upgrade pip
pip install -r requirements.txt

# 4. Executar
streamlit run app.py
```

### Windows
```cmd
# 1. Criar ambiente virtual
python -m venv venv

# 2. Ativar ambiente
venv\Scripts\activate.bat

# 3. Instalar dependências
pip install --upgrade pip
pip install -r requirements.txt

# 4. Executar
streamlit run app.py
```

---

## ✨ Funcionalidades Disponíveis

### ✅ Módulo de Condutores
- Dimensionamento conforme NBR 5410
- Seleção de seção mínima
- Verificação de queda de tensão
- Cálculo de ampacidade

### ✅ Módulo de Transformadores
- Seleção conforme NBR 5356
- Cálculo com margem de crescimento
- Verificação de correntes
- Análise comparativa de opções

### ✅ Módulo de Disjuntores
- Seleção de corrente nominal
- Verificação de padrão (B, C, D)
- Coordenação com condutores
- Validação de proteção

### ✅ Módulo de Curto-Circuito
- Cálculo conforme IEC 60909
- Determinação de Ik no ponto
- Análise de impedâncias
- Relatórios técnicos

### ✅ Módulo de Balanceamento
- Análise de cargas trifásicas
- Cálculo de desbalanceamento
- Sugestões de redistribuição
- Gráficos de visualização

### ✅ Módulo de Esquema Unifilar
- Geração de diagramas
- Exportação em PDF/DWG
- Símbolos normalizados
- Editável e profissional

### ✅ Módulo SPDA
- Proteção contra descargas (NBR 5419)
- Dimensionamento de hastes
- Cálculo de corrente de descarga
- Verificação de equipotencialização

### ✅ Sistema de Projetos
- Criar e gerenciar projetos
- Salvar cálculos
- Exportar relatórios
- Histórico de operações

---

## 🎯 Primeiro Uso - Passo a Passo

### 1. Criar um Projeto
1. Abra a aplicação
2. Na barra lateral esquerda, vá para a aba "Novo"
3. Preencha:
   - **Nome do Projeto** (ex: "Edifício Comercial - Andar 5")
   - **Cliente** (ex: "Empresa XYZ")
   - **Local** (ex: "São Paulo - SP")
4. Clique em "✅ Criar Projeto"

### 2. Usar um Módulo (Exemplo: Condutores)
1. Clique na aba "📦 Condutores"
2. Preencha os dados:
   - Corrente do circuito (A)
   - Tensão nominal (V)
   - Comprimento (m)
   - Material (Cobre/Alumínio)
3. Clique em "🔄 Calcular Dimensionamento"
4. Visualize os resultados
5. Clique em "💾 Salvar no Projeto" para armazenar

### 3. Exportar Resultados
1. Após calcular, clique em uma das opções:
   - "📊 Excel" - Planilha com dados
   - "📄 Relatório" - Documento de texto
2. O arquivo será baixado automaticamente

### 4. Consultar Histórico
1. Na barra lateral, vá para "Ferramentas"
2. Clique em "💾 Exportar" para baixar histórico em CSV

---

## 🔧 Troubleshooting (Solução de Problemas)

### Problema: "Python não encontrado"
**Solução:**
- Instale Python de https://www.python.org
- Marque a opção "Add Python to PATH" durante instalação
- Reinicie o terminal/PowerShell

### Problema: "pip: comando não encontrado"
**Solução:**
```bash
# Use:
python -m pip install -r requirements.txt
# Em vez de:
pip install -r requirements.txt
```

### Problema: "ModuleNotFoundError: No module named 'streamlit'"
**Solução:**
```bash
# Certifique-se de que o ambiente virtual está ativado
source venv/bin/activate  # Linux/macOS
# ou
venv\Scripts\activate  # Windows

# Depois instale:
pip install -r requirements.txt
```

### Problema: "Porta 8501 já está em uso"
**Solução:**
```bash
# Execute em porta diferente:
streamlit run app.py --server.port 8502
```

### Problema: "Erro de permissão no PowerShell"
**Solução:**
```powershell
# Execute como Administrador e digite:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Depois execute o install.ps1 novamente
```

### Problema: "Aplicação muito lenta"
**Solução:**
1. Feche abas desnecessárias do navegador
2. Limpe cache: Ctrl+Shift+Del
3. Reinicie o servidor Streamlit

---

## 📊 Requisitos do Sistema

| Componente | Mínimo | Recomendado |
|-----------|---------|-------------|
| RAM | 4 GB | 8 GB |
| Processador | 2 GHz | 2.5 GHz+ |
| Armazenamento | 500 MB | 1 GB |
| Conexão | Não necessária* | Banda larga |
| Navegador | Chrome 90+ | Chrome/Firefox/Edge recentes |

*Funciona totalmente offline

---

## 🌐 Acesso Remoto (Opcional)

Para acessar a aplicação de outro computador na rede:

```bash
# Inicie assim:
streamlit run app.py --server.address 0.0.0.0

# Acesse de outro PC usando:
http://[IP_DO_SERVIDOR]:8501
```

Para descobrir o IP:
- **Linux/macOS:** `ifconfig` ou `hostname -I`
- **Windows:** `ipconfig` e procure por "IPv4"

---

## 📞 Suporte e Documentação

### Documentos Disponíveis
- **START_HERE.md** - Comece aqui!
- **GUIA_USO.md** - Manual completo
- **EXEMPLOS_PRATICOS.md** - Casos de uso reais
- **TABELAS_NBR5410.md** - Tabelas de referência
- **GUIA_RAPIDO_SPDA.md** - Proteção contra surtos

### Links Úteis
- [Streamlit Documentação](https://docs.streamlit.io)
- [NBR 5410 - Instalações Elétricas](https://www.abnt.org.br)
- [Python Documentação](https://docs.python.org)

---

## 📝 Licença e Uso

EletriCalcPro é software de código aberto para fins educacionais e profissionais.

Use conforme as normas técnicas brasileiras e regulamentações locais.

---

## 🎉 Pronto!

Sua instalação está completa! Comece a usar o EletriCalcPro para seus projetos elétricos.

**Dúvidas?** Consulte a documentação ou abra uma issue no repositório.

**Boa sorte com seus projetos! ⚡**
