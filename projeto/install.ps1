# Script de Instalação - EletriCalcPro v4.2
# Para: Windows (PowerShell)
# Execute: .\install.ps1

Write-Host "╔════════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║       EletriCalcPro v4.2 - Script de Instalação          ║" -ForegroundColor Cyan
Write-Host "║    Dimensionamento Elétrico Profissional com Projetos    ║" -ForegroundColor Cyan
Write-Host "╚════════════════════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""

# Verificar Python
Write-Host "🔍 Verificando Python..." -ForegroundColor Yellow
$pythonPath = Get-Command python -ErrorAction SilentlyContinue
if ($pythonPath) {
    $pythonVersion = python --version 2>&1
    Write-Host "✅ Python encontrado: $pythonVersion" -ForegroundColor Green
} else {
    Write-Host "❌ Python 3 não encontrado!" -ForegroundColor Red
    Write-Host "   Instale em https://www.python.org" -ForegroundColor Red
    Write-Host "   Certifique-se de marcar 'Add Python to PATH'" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "📦 Preparando ambiente..." -ForegroundColor Yellow
Write-Host ""

# Criar ambiente virtual
if (-not (Test-Path "venv")) {
    Write-Host "🔧 Criando ambiente virtual..." -ForegroundColor Yellow
    python -m venv venv
    Write-Host "✅ Ambiente virtual criado!" -ForegroundColor Green
    Write-Host ""
} else {
    Write-Host "✅ Ambiente virtual encontrado" -ForegroundColor Green
}

Write-Host "🔌 Ativando ambiente virtual..." -ForegroundColor Yellow
& ".\venv\Scripts\Activate.ps1"
Write-Host "✅ Ambiente virtual ativado!" -ForegroundColor Green

Write-Host ""
Write-Host "📥 Atualizando pip..." -ForegroundColor Yellow
python -m pip install --upgrade pip setuptools wheel | Out-Null
Write-Host "✅ pip atualizado" -ForegroundColor Green

Write-Host ""
Write-Host "📥 Instalando pacotes do requirements.txt..." -ForegroundColor Yellow
Write-Host "   (Isso pode levar alguns minutos na primeira instalação)" -ForegroundColor Gray
Write-Host ""

# Instalar pacotes
pip install -r requirements.txt

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "✅ Instalação bem-sucedida!" -ForegroundColor Green
} else {
    Write-Host ""
    Write-Host "❌ Erro durante instalação!" -ForegroundColor Red
    Write-Host "   Tente: pip install --upgrade -r requirements.txt" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "╔════════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║           Próximos Passos - Para Executar:                ║" -ForegroundColor Cyan
Write-Host "║                                                            ║" -ForegroundColor Cyan
Write-Host "║  1️⃣  Ative o ambiente virtual:                            ║" -ForegroundColor Cyan
Write-Host "║     .\venv\Scripts\Activate.ps1                            ║" -ForegroundColor Cyan
Write-Host "║                                                            ║" -ForegroundColor Cyan
Write-Host "║  2️⃣  Inicie a aplicação:                                  ║" -ForegroundColor Cyan
Write-Host "║     streamlit run app.py                                  ║" -ForegroundColor Cyan
Write-Host "║                                                            ║" -ForegroundColor Cyan
Write-Host "║  3️⃣  Abra no navegador:                                   ║" -ForegroundColor Cyan
Write-Host "║     http://localhost:8501                                 ║" -ForegroundColor Cyan
Write-Host "║                                                            ║" -ForegroundColor Cyan
Write-Host "╚════════════════════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""

Write-Host "📚 Documentação Disponível:" -ForegroundColor Yellow
Write-Host "  • START_HERE.md - Comece por aqui!" -ForegroundColor Gray
Write-Host "  • GUIA_USO.md - Como usar o software" -ForegroundColor Gray
Write-Host "  • EXEMPLOS_PRATICOS.md - Casos de uso reais" -ForegroundColor Gray
Write-Host "  • TABELAS_NBR5410.md - Referência NBR 5410" -ForegroundColor Gray
Write-Host "  • GUIA_RAPIDO_SPDA.md - Proteção contra descargas" -ForegroundColor Gray
Write-Host ""

Write-Host "✨ Funcionalidades v4.2:" -ForegroundColor Cyan
Write-Host "  ✅ Sistema de Projetos com salvamento" -ForegroundColor Green
Write-Host "  ✅ Dimensionamento de Condutores (NBR 5410)" -ForegroundColor Green
Write-Host "  ✅ Seleção de Transformadores (NBR 5356)" -ForegroundColor Green
Write-Host "  ✅ Proteção contra Surtos (SPDA - NBR 5419)" -ForegroundColor Green
Write-Host "  ✅ Cálculo de Curto-Circuito (IEC 60909)" -ForegroundColor Green
Write-Host "  ✅ Balanceamento de Fases" -ForegroundColor Green
Write-Host "  ✅ Exportação em múltiplos formatos" -ForegroundColor Green
Write-Host ""

Write-Host "🎉 Bom trabalho com seus projetos elétricos!" -ForegroundColor Green
Write-Host ""
