# Setup Guide for NoteMind Token Manager

## 🚀 Quick Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Test Installation
```bash
python quick_start.py
```

## 📁 Project Structure

```
NoteMind/
├── README.md              # Comprehensive token guide
├── SETUP.md              # This setup guide
├── requirements.txt      # Python dependencies
├── setup.py             # Package installation
├── token_manager.py     # Core token management class
├── token_cli.py         # Command-line interface
├── examples.py          # Usage examples
├── quick_start.py       # Interactive quick start
└── test_token_manager.py # Unit tests
```

## 🛠️ Installation Options

### Option 1: Install as Package
```bash
pip install -e .
```

This installs the `token-manager` command globally.

### Option 2: Use Directly
```bash
python token_manager.py
python examples.py
python quick_start.py
```

## 🔧 Usage Examples

### Command Line Interface

#### Basic Token Counting
```bash
python token_cli.py --text "Hello world" --action count
```

#### Analyze Text File
```bash
python token_cli.py --file document.txt --action analyze --model gpt-4
```

#### Check Context Limits
```bash
python token_cli.py --text "Your long text here" --action check
```

#### Chunk Long Text
```bash
python token_cli.py --file long_document.txt --action chunk --max-tokens 1000
```

#### Optimize Prompt
```bash
python token_cli.py --text "Your verbose prompt" --action optimize --max-tokens 50
```

#### List Available Models
```bash
python token_cli.py --action models
```

### Python API Usage

```python
from token_manager import TokenManager

# Initialize
token_mgr = TokenManager()

# Count tokens
tokens = token_mgr.count_tokens("Hello world")

# Analyze text
analysis = token_mgr.analyze_text("Your text here")

# Check context limits
context_check = token_mgr.check_context_limit("Your text")

# Chunk long text
chunks = token_mgr.chunk_text(long_text, max_tokens=1000)

# Optimize prompts
optimized = token_mgr.optimize_prompt(verbose_prompt, target_tokens=100)
```

## 🧪 Testing

### Run All Tests
```bash
python -m unittest test_token_manager.py
```

### Run Specific Test
```bash
python -m unittest test_token_manager.TestTokenManager.test_count_tokens
```

## 📊 Supported Models

| Model | Context Window | Input Cost/1K | Output Cost/1K |
|-------|----------------|----------------|----------------|
| GPT-3.5-turbo | 4,096 tokens | $0.0015 | $0.002 |
| GPT-4 | 8,192 tokens | $0.03 | $0.06 |
| Claude-3-sonnet | 200,000 tokens | $0.003 | $0.015 |

## 🔍 Features

### Core Functionality
- ✅ Exact token counting using tiktoken
- ✅ Cost estimation across models
- ✅ Context limit checking
- ✅ Text chunking for long documents
- ✅ Prompt optimization
- ✅ Conversation token tracking
- ✅ Multiple model support

### Advanced Features
- ✅ Content-type specific estimation
- ✅ Sentence-aware chunking
- ✅ Cost comparison across models
- ✅ Comprehensive text analysis
- ✅ Error handling and validation

## 🚨 Troubleshooting

### Common Issues

#### 1. Import Error: No module named 'tiktoken'
```bash
pip install tiktoken
```

#### 2. Encoding Error
The system automatically falls back to estimation if encoders fail to initialize.

#### 3. Model Not Supported
Check available models with:
```bash
python token_cli.py --action models
```

### Performance Tips

1. **Use estimation for quick checks**: `estimate_tokens()` is faster than `count_tokens()`
2. **Batch processing**: Process multiple texts together when possible
3. **Cache results**: Store token counts for repeated text analysis
4. **Choose appropriate models**: Use smaller models for simple tasks

## 📚 Learning Resources

- **README.md**: Comprehensive token guide
- **examples.py**: Practical usage examples
- **quick_start.py**: Interactive tutorial
- **test_token_manager.py**: Understanding through tests

## 🔄 Updates and Maintenance

### Check for Updates
```bash
pip list --outdated
```

### Update Dependencies
```bash
pip install -r requirements.txt --upgrade
```

### Verify Installation
```bash
python -c "from token_manager import TokenManager; print('✅ Token Manager ready!')"
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Ensure all tests pass
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

**Need Help?** Check the examples, run the quick start, or review the comprehensive README guide!
