#!/bin/bash

# Quick verification script for interview readiness
# Run: bash scripts/verify_setup.sh

set -e

echo "🔍 Verifying Interview Setup..."
echo ""

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check Python
echo -n "Checking Python... "
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
    echo -e "${GREEN}✓${NC} Python $PYTHON_VERSION"
else
    echo -e "${RED}✗${NC} Python not found"
    exit 1
fi

# Check uv
echo -n "Checking uv... "
if command -v uv &> /dev/null; then
    echo -e "${GREEN}✓${NC} $(which uv)"
else
    echo -e "${RED}✗${NC} uv not found - install from https://github.com/astral-sh/uv"
    exit 1
fi

# Check Node.js
echo -n "Checking Node.js... "
if command -v node &> /dev/null; then
    NODE_VERSION=$(node --version)
    echo -e "${GREEN}✓${NC} $NODE_VERSION"
else
    echo -e "${YELLOW}⚠${NC} Node.js not found (optional for backend-only work)"
fi

# Check Docker (optional)
echo -n "Checking Docker... "
if command -v docker &> /dev/null; then
    echo -e "${GREEN}✓${NC} $(docker --version | cut -d' ' -f3 | cut -d',' -f1)"
else
    echo -e "${YELLOW}⚠${NC} Docker not found (optional)"
fi

# Test backend dependencies
echo ""
echo "Testing backend setup..."
cd backend
if uv sync --dev &> /dev/null; then
    echo -e "${GREEN}✓${NC} Backend dependencies installed"
else
    echo -e "${RED}✗${NC} Failed to install backend dependencies"
    exit 1
fi

# Test imports
echo -n "Testing Python imports... "
if uv run python -c "from src.math_operations import square; from src.data_parsing import load_csv" 2>/dev/null; then
    echo -e "${GREEN}✓${NC} Imports work correctly"
else
    echo -e "${RED}✗${NC} Import errors"
    exit 1
fi

# Test data files exist
echo -n "Checking sample data files... "
if [ -f "data/sample_data.csv" ] && [ -f "data/sample_data.json" ]; then
    echo -e "${GREEN}✓${NC} Sample datasets found"
else
    echo -e "${YELLOW}⚠${NC} Some sample data files missing"
fi

# Test frontend (if Node.js available)
if command -v node &> /dev/null; then
    echo ""
    echo "Testing frontend setup..."
    cd ../frontend
    if [ -f "package.json" ]; then
        if npm list --depth=0 &> /dev/null || [ -d "node_modules" ]; then
            echo -e "${GREEN}✓${NC} Frontend dependencies available"
        else
            echo -e "${YELLOW}⚠${NC} Run 'npm install' in frontend/ directory"
        fi
    fi
fi

echo ""
echo -e "${GREEN}✅ Setup verification complete!${NC}"
echo ""
echo "Quick start commands:"
echo "  Backend:  cd backend && uv run python app.py"
echo "  Frontend: cd frontend && npm run dev"
echo "  Docker:   docker-compose up --build"
echo ""
echo "See INTERVIEW_READINESS.md for full details."

