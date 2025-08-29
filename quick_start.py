#!/usr/bin/env python3
"""
Quick Start Guide for Token Manager
Run this script to see the token manager in action!
"""

from token_manager import TokenManager

def main():
    print("🚀 NoteMind Token Manager - Quick Start")
    print("=" * 50)
    
    # Initialize the token manager
    print("Initializing Token Manager...")
    token_mgr = TokenManager()
    print("✅ Ready!\n")
    
    # Show available models
    print("📋 Available Models:")
    for model in token_mgr.list_models():
        info = token_mgr.get_model_info(model)
        print(f"  • {model}: {info['context_window']:,} tokens")
    print()
    
    # Interactive text analysis
    print("🔍 Text Analysis Example:")
    sample_text = input("Enter some text to analyze (or press Enter for default): ").strip()
    
    if not sample_text:
        sample_text = "Hello! This is a sample text to demonstrate how the token manager works."
        print(f"Using default text: {sample_text}")
    
    print(f"\nAnalyzing text with GPT-3.5-turbo...")
    analysis = token_mgr.analyze_text(sample_text)
    
    print(f"📊 Analysis Results:")
    print(f"  • Tokens: {analysis.token_count:,}")
    print(f"  • Words: {analysis.word_count:,}")
    print(f"  • Characters: {analysis.character_count:,}")
    print(f"  • Estimated Cost: ${analysis.estimated_cost:.6f}")
    print()
    
    # Context limit check
    print("🔐 Context Limit Check:")
    context_check = token_mgr.check_context_limit(sample_text)
    print(f"  • Fits in context: {'✅ Yes' if context_check['fits'] else '❌ No'}")
    print(f"  • Context window: {context_check['context_window']:,} tokens")
    print(f"  • Remaining tokens: {context_check['remaining_tokens']:,}")
    print(f"  • Usage: {context_check['overflow_percentage']:.1f}%")
    print()
    
    # Cost comparison across models
    print("💰 Cost Comparison Across Models:")
    for model in ['gpt-3.5-turbo', 'gpt-4']:
        model_analysis = token_mgr.analyze_text(sample_text, model)
        print(f"  • {model}: ${model_analysis.estimated_cost:.6f}")
    print()
    
    # Text chunking demo
    print("✂️  Text Chunking Demo:")
    long_text = """
    This is a longer text that demonstrates the chunking functionality. 
    It contains multiple sentences and will be split into smaller pieces. 
    Each chunk will fit within a specified token limit. 
    This is useful for processing long documents or conversations.
    """
    
    print("Original text length:", len(long_text), "characters")
    chunks = token_mgr.chunk_text(long_text, max_tokens=30)
    print(f"Split into {len(chunks)} chunks:")
    
    for i, chunk in enumerate(chunks, 1):
        tokens = token_mgr.count_tokens(chunk)
        print(f"  Chunk {i}: {tokens} tokens - {chunk[:50]}...")
    print()
    
    # Prompt optimization demo
    print("🎯 Prompt Optimization Demo:")
    verbose_prompt = """
    Could you please help me understand how to implement a binary search algorithm in Python? 
    I would really appreciate if you could provide detailed explanations with step-by-step instructions, 
    multiple examples showing different use cases, and also include some common pitfalls to avoid.
    """
    
    print("Original prompt tokens:", token_mgr.count_tokens(verbose_prompt))
    optimized = token_mgr.optimize_prompt(verbose_prompt, target_tokens=25)
    print("Optimized prompt tokens:", token_mgr.count_tokens(optimized))
    print("Optimized text:", optimized)
    print()
    
    # Interactive mode
    print("🎮 Interactive Mode:")
    print("Try analyzing your own text! (Type 'quit' to exit)")
    
    while True:
        user_text = input("\nEnter text to analyze: ").strip()
        
        if user_text.lower() in ['quit', 'exit', 'q']:
            break
        
        if not user_text:
            continue
        
        try:
            user_analysis = token_mgr.analyze_text(user_text)
            print(f"  📊 {user_analysis.token_count:,} tokens, {user_analysis.word_count:,} words")
            print(f"  💰 Cost: ${user_analysis.estimated_cost:.6f}")
            
            # Quick context check
            if user_analysis.token_count > 4000:
                print("  ⚠️  Warning: This text is quite long!")
            elif user_analysis.token_count > 2000:
                print("  ⚠️  Note: This text is moderately long")
            else:
                print("  ✅ Text length is good")
                
        except Exception as e:
            print(f"  ❌ Error: {e}")
    
    print("\n👋 Thanks for trying the Token Manager!")
    print("Check out the examples.py file for more advanced usage.")

if __name__ == "__main__":
    main()
