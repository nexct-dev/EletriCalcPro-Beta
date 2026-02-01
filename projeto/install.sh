#!/bin/bash
# Script de Instalação - EletriCalcPro v3.0
# Execute: bash install.sh

echo "╔════════════════════════════════════════════════════════════╗"
echo "║         EletriCalcPro v3.0 - Script de Instalação         ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""

# Verificar Python
echo "🔍 Verificando Python..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version)
    echo "✅ Python encontrado: $PYTHON_VERSION"
else
    echo "❌ Python 3 não encontrado! Instale Python 3.7 ou superior."
    exit 1
fi

echo ""
echo "📦 Instalando dependências..."
echo ""

# Criar ambiente virtual (opcional)
if [ ! -d "venv" ]; then
    echo "🔧 Criando ambiente virtual..."
    python3 -m venv venv
    echo "✅ Ambiente virtual criado!"
    echo ""
    echo "🔌 Ativando ambiente virtual..."
    source venv/bin/activate
    echo "✅ Ambiente virtual ativado!"
else
    echo "✅ Ambiente virtual já existe"
    source venv/bin/activate
fi

echo ""
echo "📥 Instalando pacotes de requirements.txt..."
pip install --upgrade pip
pip install -r requirements.txt

echo ""
echo "✅ Instalação completa!"
echo ""
echo "╔════════════════════════════════════════════════════════════╗"
echo "║            Para executar o software:                       ║"
echo "║                                                            ║"
echo "║  1. Ative o ambiente virtual:                             ║"
echo "║     source venv/bin/activate  (Linux/Mac)                 ║"
echo "║     venv\\Scripts\\activate     (Windows)                   ║"
echo "║                                                            ║"
echo "║  2. Execute:                                              ║"
echo "║     streamlit run app.py                                  ║"
echo "║                                                            ║"
echo "║  3. Abra no navegador:                                    ║"
echo "║     http://localhost:8501                                 ║"
echo "║                                                            ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""
echo "📚 Documentação:"
echo "  • START_HERE.md - Comece por aqui!"
echo "  • GUIA_USO.md - Como usar o software"
echo "  • EXEMPLOS_PRATICOS.md - Casos reais"
echo ""
echo "🎉 Boa sorte com seus projetos elétricos!"
echo ""
