#!/bin/bash
# Quick Setup Script for macOS/Linux
# Run: bash quick_setup.sh

echo "🚀 Excel Merger - Quick Setup"
echo "================================"

# Check Python
echo "✓ Checking Python..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found. Please install from python.org"
    exit 1
fi

PYTHON_VERSION=$(python3 --version | awk '{print $2}')
echo "  Python $PYTHON_VERSION found ✓"

# Create virtual environment
echo ""
echo "✓ Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "✓ Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo ""
echo "✓ Upgrading pip..."
pip install --upgrade pip > /dev/null 2>&1

# Install dependencies
echo "✓ Installing dependencies..."
pip install -r requirements.txt > /dev/null 2>&1

echo ""
echo "================================"
echo "✅ Setup Complete!"
echo "================================"
echo ""
echo "To start the app, run:"
echo ""
echo "  source venv/bin/activate"
echo "  streamlit run app.py"
echo ""
echo "Then open: http://localhost:8501"
echo ""
