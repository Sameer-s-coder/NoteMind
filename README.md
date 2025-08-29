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