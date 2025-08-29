# 📚 NoteMind

*An AI-powered note manager that organizes, summarizes, and retrieves your notes.*

---

## 🚀 Overview

**NoteMind** is a CLI tool that helps you manage your notes intelligently using Generative AI.
With NoteMind, you can:

* Add and store raw notes
* Summarize them into clear, concise points
* Retrieve notes with semantic search (AI-powered)
* Generate study aids like flashcards
* Export structured outputs (JSON/Markdown)

This project demonstrates **prompt engineering, model controls, structured outputs, function calling, and embeddings** — making it both practical and portfolio-ready.

---

## ✨ Features

* 📝 **Add Notes:** Store your raw notes directly via CLI.
* 🔎 **Search with AI:** Retrieve contextually relevant notes using embeddings.
* 📑 **Summarize:** Get concise bullet-point summaries of long notes.
* 🎓 **Flashcards:** Convert notes into question–answer flashcards.
* ⚙ **Custom Controls:** Adjust temperature, top-k, and top-p for different styles.
* 📂 **Structured Output:** Export summaries and notes in JSON/Markdown.

---

## 🛠️ Installation

```bash
# Clone the repository
git clone https://github.com/your-username/notemind.git
cd notemind

# Install dependencies
npm install   # (if Node.js version)
# or
pip install -r requirements.txt   # (if Python version)

# Set up environment variables
cp .env.example .env
```

Inside `.env`, add your API key (Gemini/OpenAI/etc.):

```
API_KEY=your_api_key_here
```

---

## ⚡ Usage

### Add a note

```bash
nm add "Neural networks mimic the human brain's neuron connections."
```

### Summarize notes

```bash
nm summarize
```

➡ Output:

```
Topic: Neural Networks
Summary: NNs are AI models inspired by biological neurons, useful in pattern recognition.
```

### Search notes

```bash
nm search "What did I write about neural networks?"
```

### Generate flashcards

```bash
nm flashcards
```

➡ Output:

```
Q: What do neural networks mimic?  
A: The connections of neurons in the human brain.
```

---

## ⚙️ CLI Commands

| Command         | Description                                |
| --------------- | ------------------------------------------ |
| `nm add`        | Add new notes                              |
| `nm summarize`  | Summarize all stored notes                 |
| `nm search`     | Retrieve notes using embeddings            |
| `nm flashcards` | Generate flashcards from notes             |
| `nm export`     | Export notes/summaries to JSON or Markdown |

---

## 📂 Project Structure

```
notemind/
├── src/
│   ├── cli.js        # CLI entry point
│   ├── prompts/      # System & user prompts
│   ├── embeddings/   # Vector search logic
│   ├── utils/        # Helper functions
│   └── tests/        # Evaluation & tests
├── README.md
├── package.json / requirements.txt
└── .env.example
```

---

## 🧪 Testing

Run evaluation dataset against NoteMind to verify performance:

```bash
npm test
# or
pytest tests/
```

---

## 📖 Roadmap

* [x] Add/Summarize notes
* [x] Search with embeddings
* [x] Flashcard generation
* [ ] Web UI version
* [ ] Cloud sync

---

## 🤝 Contributing

Pull requests are welcome! Please open an issue first to discuss what you’d like to change.

---

## 📜 License

MIT License © 2025 \[Your Name]

---
System and User Prompt :
        👉 Example:

System: ‘You are NoteMind, an AI note manager. Always answer in bullet points.’

User: ‘Summarize this note: Neural networks mimic the brain.’
➡ Output:
• Neural networks imitate brain neurons
• Useful in AI models

This shows how system and user prompts shape the AI’s tone and structure.”



Zero-Shot Prompting :
“Now let’s look at Zero-Shot Prompting.
This is when we ask the model to answer without giving it any examples.

👉 Example:
User: ‘Explain overfitting in machine learning.’
➡ Output: ‘Overfitting happens when a model memorizes noise in the training data instead of learning patterns.’

As you can see, even with no examples, the model gives a clear answer. This is the foundation of AI-agent interactions.”


One-Shot Prompting :
        “Next is One-Shot Prompting.
Here, we give the AI one example before asking our question.

👉 Example:

Example:
User: ‘Summarize: Decision trees split data.’
Model: ‘• Definition • How it works • Uses’

New Query:
User: ‘Summarize underfitting.’
➡ Output: ‘• Too simple • Misses patterns • Poor accuracy.’

One example helps the model produce more structured and accurate answers.”


Multi-Shot Prompting :

“Now let’s see Multi-Shot Prompting.
This is when we provide multiple examples to guide the AI’s response.

👉 Example:
User provides:

Input: ‘Linear Regression’ → Flashcard: Q: What does it do? A: Predicts continuous values.

Input: ‘Logistic Regression’ → Flashcard: Q: What does it do? A: Classifies binary outcomes.

Then asks: ‘Make flashcards from Gradient Descent.’
➡ Output:
Q: What does Gradient Descent do?
A: Minimizes loss by iteratively updating parameters.

The more examples we provide, the more consistent the answers become.”


Chain-of-Thought Prompting :

“Next is Chain-of-Thought Prompting.
Here, we encourage the model to reason step by step before giving the answer.

👉 Example:
User: ‘Explain the bias-variance tradeoff.’
The model first reasons internally:

Bias is error from strong assumptions.

Variance is error from sensitivity to data.

➡ Final Output: ‘The bias-variance tradeoff is about balancing simplicity and flexibility to achieve better generalization.’

This hidden reasoning makes the answer more accurate.”

Dynamic Prompting (≈1 min)

“Finally, Dynamic Prompting.
This means building prompts dynamically using context or user inputs.

👉 Example:
If my last topic was CNNs and the user says: ‘Give me a 50-word summary of convolutional layers.’
➡ Output: ‘Convolutional layers detect features like edges and textures in images, forming the building blocks of CNNs for vision tasks.’

The AI adapts the prompt depending on the context, which is powerful for real applications like our NoteMind project.”

# NoteMind - AI Tokenization Guide

## Understanding Tokens and Tokenization

### What are Tokens?

Tokens are the fundamental units that AI language models use to process and understand text. Think of them as the "words" that the AI model recognizes, though they're not always actual words in the traditional sense.

### How Tokenization Works

1. **Text Breakdown**: When you input text, it gets broken down into smaller pieces (tokens)
2. **Model Processing**: The AI model processes these tokens sequentially
3. **Context Understanding**: Tokens help the model understand relationships and context

### Types of Tokens

- **Word Tokens**: Complete words (e.g., "hello" = 1 token)
- **Subword Tokens**: Parts of words (e.g., "running" = "run" + "ing" = 2 tokens)
- **Punctuation Tokens**: Special characters and punctuation
- **Special Tokens**: Model-specific tokens like start/end markers

### Why Token Limits Matter

AI models have maximum context windows (total tokens they can process):
- **Input Tokens**: Your prompt/question
- **Output Tokens**: AI's response
- **Total Limit**: Combined input + output cannot exceed the model's capacity

### Common Token Limits

| Model | Context Window | Typical Use Case |
|-------|----------------|------------------|
| GPT-3.5 | 4,096 tokens | General conversation |
| GPT-4 | 8,192 tokens | Complex analysis |
| Claude-3 | 200,000 tokens | Long documents |
| Llama-2 | 4,096 tokens | Open source models |

### Estimating Token Count

**Rough Guidelines:**
- **English**: ~1 token = 0.75 words
- **Code**: ~1 token = 0.5-1.5 characters
- **Technical text**: ~1 token = 0.5 words

**Example:**
```
"Hello, how are you today?" = ~7 tokens
"function calculateSum(a, b) { return a + b; }" = ~15 tokens
```

### Strategies for Managing Token Limits

#### 1. **Concise Prompts**
- Remove unnecessary words
- Use clear, direct language
- Focus on essential information

#### 2. **Chunking Long Content**
- Break documents into smaller sections
- Process each chunk separately
- Maintain context between chunks

#### 3. **Priority-Based Content**
- Lead with most important information
- Use bullet points for clarity
- Eliminate redundant content

### Token Counting Tools

Several tools can help estimate token usage:
- **OpenAI Tokenizer**: Official tool for GPT models
- **Hugging Face Tokenizers**: For various model types
- **Online Calculators**: Quick estimates
- **API Responses**: Most APIs return token counts

### Best Practices

1. **Monitor Usage**: Track token consumption in your applications
2. **Optimize Prompts**: Refine prompts for efficiency
3. **Plan Ahead**: Consider token limits when designing workflows
4. **Test Limits**: Understand your model's specific constraints

### Common Token Limit Errors

- **Input too long**: Prompt exceeds context window
- **Output truncated**: Response cut off due to limits
- **Context overflow**: Combined input/output too large

### Advanced Techniques

#### **Token-Efficient Prompting**
```
❌ Verbose: "Could you please help me understand how to implement a binary search algorithm in Python with detailed explanations and examples?"

✅ Concise: "Implement binary search in Python with example"
```

#### **Streaming Responses**
- Process long outputs in chunks
- Maintain conversation flow
- Avoid hitting output limits

### Real-World Examples

#### **Document Analysis**
```
Input: 50-page PDF (est. 15,000 tokens)
Strategy: Process in 3-4 chunks of ~4,000 tokens each
```

#### **Code Review**
```
Input: Large codebase (est. 20,000 tokens)
Strategy: Review file by file, maintain context summary
```

### Resources for Learning More

- [OpenAI Tokenizer](https://platform.openai.com/tokenizer)
- [Hugging Face Tokenizers](https://huggingface.co/docs/tokenizers)
- [Model Documentation](https://platform.openai.com/docs/models)
- [Token Limit Guidelines](https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them)

---

*This guide helps you understand and manage tokens effectively when working with AI models. Remember that token efficiency directly impacts both cost and performance.*