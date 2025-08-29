#!/usr/bin/env python3
"""
Examples of using the TokenManager for various use cases.
"""

from token_manager import TokenManager
import json

def example_basic_usage():
    """Basic token counting and analysis."""
    print("=== Basic Token Usage ===")
    
    token_mgr = TokenManager()
    
    # Simple text analysis
    text = "Hello! This is a sample text to demonstrate token counting."
    analysis = token_mgr.analyze_text(text)
    
    print(f"Text: {text}")
    print(f"Tokens: {analysis.token_count}")
    print(f"Words: {analysis.word_count}")
    print(f"Cost: ${analysis.estimated_cost:.6f}")
    print()

def example_context_limits():
    """Demonstrate context limit checking."""
    print("=== Context Limit Checking ===")
    
    token_mgr = TokenManager()
    
    # Check different models
    models = ['gpt-3.5-turbo', 'gpt-4', 'claude-3-sonnet']
    text = "This is a moderately long text that we'll use to test context limits across different models."
    
    for model in models:
        check = token_mgr.check_context_limit(text, model)
        print(f"Model: {model}")
        print(f"  Fits: {check['fits']}")
        print(f"  Tokens: {check['token_count']}")
        print(f"  Remaining: {check['remaining_tokens']}")
        print(f"  Usage: {check['overflow_percentage']:.1f}%")
        print()

def example_text_chunking():
    """Demonstrate text chunking for long documents."""
    print("=== Text Chunking ===")
    
    token_mgr = TokenManager()
    
    # Simulate a long document
    long_text = """
    This is the first paragraph of our document. It contains some basic information about tokens and tokenization.
    
    The second paragraph goes into more detail about how AI models process text. It explains the concept of context windows and why they matter.
    
    Our third paragraph discusses practical applications. We talk about cost optimization and efficient prompt design.
    
    Finally, the fourth paragraph wraps up with best practices and recommendations for working with token limits.
    """
    
    # Chunk into smaller pieces
    chunks = token_mgr.chunk_text(long_text, max_tokens=50)
    
    print(f"Original text length: {len(long_text)} characters")
    print(f"Number of chunks: {len(chunks)}")
    print()
    
    for i, chunk in enumerate(chunks):
        tokens = token_mgr.count_tokens(chunk)
        print(f"Chunk {i+1} ({tokens} tokens):")
        print(f"  {chunk[:100]}...")
        print()

def example_prompt_optimization():
    """Demonstrate prompt optimization."""
    print("=== Prompt Optimization ===")
    
    token_mgr = TokenManager()
    
    # Verbose prompt
    verbose_prompt = """
    Could you please help me understand how to implement a binary search algorithm in Python? 
    I would really appreciate if you could provide detailed explanations with step-by-step instructions, 
    multiple examples showing different use cases, and also include some common pitfalls to avoid. 
    Additionally, it would be helpful to see performance analysis and time complexity explanations.
    """
    
    print("Original prompt:")
    print(verbose_prompt)
    print(f"Tokens: {token_mgr.count_tokens(verbose_prompt)}")
    print()
    
    # Optimize to fit within 50 tokens
    optimized = token_mgr.optimize_prompt(verbose_prompt, target_tokens=50)
    
    print("Optimized prompt:")
    print(optimized)
    print(f"Tokens: {token_mgr.count_tokens(optimized)}")
    print()

def example_conversation_tracking():
    """Demonstrate conversation token tracking."""
    print("=== Conversation Token Tracking ===")
    
    token_mgr = TokenManager()
    
    # Simulate a conversation
    conversation = [
        {"role": "user", "content": "Hello! Can you help me with Python programming?"},
        {"role": "assistant", "content": "Of course! I'd be happy to help you with Python programming. What specific topic or problem would you like to discuss?"},
        {"role": "user", "content": "I'm trying to learn about data structures and algorithms. Can you explain linked lists?"},
        {"role": "assistant", "content": "Linked lists are a fundamental data structure in computer science. They consist of nodes, where each node contains data and a reference to the next node in the sequence. This creates a chain-like structure that allows for efficient insertion and deletion operations."}
    ]
    
    # Calculate tokens for different models
    for model in ['gpt-3.5-turbo', 'gpt-4']:
        result = token_mgr.calculate_conversation_tokens(conversation, model)
        print(f"Model: {model}")
        print(f"  Total tokens: {result['total_tokens']}")
        print(f"  Input tokens: {result['input_tokens']}")
        print(f"  Output tokens: {result['output_tokens']}")
        print(f"  Total cost: ${result['total_cost']:.6f}")
        print(f"  Fits context: {result['fits_context']}")
        print()

def example_cost_analysis():
    """Demonstrate cost analysis for different content types."""
    print("=== Cost Analysis ===")
    
    token_mgr = TokenManager()
    
    # Different types of content
    content_samples = {
        "Short question": "What is Python?",
        "Medium explanation": "Python is a high-level, interpreted programming language known for its simplicity and readability. It supports multiple programming paradigms and has extensive standard libraries.",
        "Long document": "Python is a versatile programming language that was created by Guido van Rossum and first released in 1991. It emphasizes code readability with its notable use of significant whitespace. Python features a dynamic type system and automatic memory management. It supports multiple programming paradigms, including structured, object-oriented, and functional programming. Python interpreters are available for many operating systems. A global community of programmers maintains and develops CPython, an open source reference implementation of Python. The Python Software Foundation manages and directs resources for Python and CPython development.",
        "Code example": "def fibonacci(n):\n    if n <= 1:\n        return n\n    return fibonacci(n-1) + fibonacci(n-2)\n\n# Test the function\nfor i in range(10):\n    print(fibonacci(i))"
    }
    
    models = ['gpt-3.5-turbo', 'gpt-4']
    
    for content_type, content in content_samples.items():
        print(f"\n{content_type}:")
        for model in models:
            analysis = token_mgr.analyze_text(content, model)
            print(f"  {model}: {analysis.token_count} tokens, ${analysis.estimated_cost:.6f}")

def main():
    """Run all examples."""
    print("Token Manager Examples\n")
    
    example_basic_usage()
    example_context_limits()
    example_text_chunking()
    example_prompt_optimization()
    example_conversation_tracking()
    example_cost_analysis()
    
    print("=== Examples Complete ===")

if __name__ == "__main__":
    main()
