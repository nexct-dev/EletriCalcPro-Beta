# Software para Projetos Elétricos ⚡

Interface Streamlit para dimensionamento de componentes elétricos conforme normas brasileiras.

## 🎯 Funcionalidades

- **Condutores**: Dimensionamento por queda de tensão (NBR 5410)
- **Transformadores**: Seleção por potência e margens (NBR 5356)  
- **Disjuntores**: Proteção conforme corrente do circuito
- **Curto-Circuito**: Cálculo de Ik (IEC 60909 / NBR 5410)

Cada cálculo gera um **memorial descritivo** automático conforme as normas.

## 📦 Instalação

```bash
pip install -r requirements.txt
```

## 🚀 Execução

```bash
streamlit run app.py
```

A aplicação abrirá em `http://localhost:8501`

## 📋 Normas Aplicadas

- **NBR 5410**: Instalações Elétricas de Baixa Tensão
- **NBR 5356**: Transformadores de Potência  
- **IEC 60909**: Correntes de Curto-Circuito em Sistemas Trifásicos

## 🔧 Estrutura

```
├── app.py              # Aplicação principal Streamlit
├── requirements.txt    # Dependências Python
└── README.md          # Este arquivo
```

## 📊 Entrada/Saída

### Entrada
- Parâmetros elétricos (corrente, tensão, comprimento, etc.)
- Normas e critérios

### Saída  
- Dimensionamentos selecionados
- Verificações de conformidade
- Alertas (se houver)
- Memorial descritivo em PDF (texto)

## ⚙️ Parâmetros Padrão

- **Queda de Tensão**: 3% (máximo recomendado)
- **Fator de Demanda**: 0.8 (80%)
- **Margem de Crescimento**: 20%
- **Impedância Trafo**: 5% (Uk)
- **Material**: Cobre

---

Desenvolvido para projetos elétricos em conformidade com normas técnicas brasileiras.
