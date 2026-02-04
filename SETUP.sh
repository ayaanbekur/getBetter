#!/bin/bash
# Get Better - Setup and Run Script
# Run this script to get started: bash SETUP.sh

echo "🚀 Get Better - Setup Script"
echo "================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8+"
    exit 1
fi

echo "✅ Python found: $(python3 --version)"
echo ""

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "🔌 Activating virtual environment..."
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    # Windows
    source venv/Scripts/activate
else
    # macOS/Linux
    source venv/bin/activate
fi

# Install dependencies
echo "📥 Installing dependencies..."
pip install -r requirements.txt

# Create database
echo "💾 Setting up database..."
python app.py &
sleep 2
kill $!

echo ""
echo "================================"
echo "✅ Setup Complete!"
echo "================================"
echo ""
echo "🎯 Next Steps:"
echo "1. Activate virtual environment (if needed)"
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    echo "   venv\\Scripts\\activate"
else
    echo "   source venv/bin/activate"
fi
echo ""
echo "2. Run the application"
echo "   python app.py"
echo ""
echo "3. Open in browser"
echo "   http://localhost:5000"
echo ""
echo "4. Test it out!"
echo "   - Sign up with test@example.com / password123"
echo "   - Select multiple goals"
echo "   - View your personalized plans"
echo ""
echo "📚 For more info, read QUICKSTART.md"
echo ""
