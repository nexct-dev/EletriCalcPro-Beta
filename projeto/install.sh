#!/bin/bash
# Script de Instalação - EletriCalcPro v4.2
# Suporte: Linux, macOS e WSL
# Execute: bash install.sh

echo "╔════════════════════════════════════════════════════════════╗"
echo "║       EletriCalcPro v4.2 - Script de Instalação          ║"
echo "║    Dimensionamento Elétrico Profissional com Projetos    ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""

# Verificar Python
echo "🔍 Verificando Python..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version)
    echo "✅ Python encontrado: $PYTHON_VERSION"
else
    echo "❌ Python 3 não encontrado!"
    echo "   Instale Python 3.8 ou superior em https://www.python.org"
    exit 1
fi

echo ""
echo "📦 Preparando ambiente..."
echo ""

# Criar ambiente virtual (opcional)
if [ ! -d "venv" ]; then
    echo "🔧 Criando ambiente virtual..."
    python3 -m venv venv
    echo "✅ Ambiente virtual criado!"
    echo ""
else
    echo "✅ Ambiente virtual encontrado"
fi

echo "🔌 Ativando ambiente virtual..."
source venv/bin/activate
echo "✅ Ambiente virtual ativado!"

echo ""
echo "📥 Atualizando pip..."
pip install --upgrade pip setuptools wheel > /dev/null 2>&1
echo "✅ pip atualizado"

echo ""
echo "📥 Instalando pacotes do requirements.txt..."
echo "   (Isso pode levar alguns minutos na primeira instalação)"
echo ""

# Instalar com feedback visual
pip install -r requirements.txt

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Instalação bem-sucedida!"
else
    echo ""
    echo "❌ Erro durante instalação!"
    echo "   Tente: pip install --upgrade -r requirements.txt"
    exit 1
fi

echo ""
echo "╔════════════════════════════════════════════════════════════╗"
echo "║           Próximos Passos - Para Executar:                ║"
echo "║                                                            ║"
echo "║  1️⃣  Ative o ambiente virtual:                            ║"
echo "║     source venv/bin/activate                              ║"
echo "║                                                            ║"
echo "║  2️⃣  Inicie a aplicação:                                  ║"
echo "║     streamlit run app.py                                  ║"
echo "║                                                            ║"
echo "║  3️⃣  Abra no navegador:                                   ║"
echo "║     http://localhost:8501                                 ║"
echo "║                                                            ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""
echo "📚 Documentação Disponível:"
echo "  • START_HERE.md - Comece por aqui!"
echo "  • GUIA_USO.md - Como usar o software"
echo "  • EXEMPLOS_PRATICOS.md - Casos de uso reais"
echo "  • TABELAS_NBR5410.md - Referência NBR 5410"
echo "  • GUIA_RAPIDO_SPDA.md - Proteção contra descargas"
echo ""
echo "✨ Funcionalidades v4.2:"
echo "  ✅ Sistema de Projetos com salvamento"
echo "  ✅ Dimensionamento de Condutores (NBR 5410)"
echo "  ✅ Seleção de Transformadores (NBR 5356)"
echo "  ✅ Proteção contra Surtos (SPDA - NBR 5419)"
echo "  ✅ Cálculo de Curto-Circuito (IEC 60909)"
echo "  ✅ Balanceamento de Fases"
echo "  ✅ Exportação em múltiplos formatos"
echo ""
echo "🎉 Bom trabalho com seus projetos elétricos!"
echo ""
