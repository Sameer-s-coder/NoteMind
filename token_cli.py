#!/usr/bin/env python3
"""
Command-line interface for token management and analysis.
"""

import argparse
import sys
from token_manager import TokenManager
import json

def main():
    parser = argparse.ArgumentParser(description='Token Manager CLI')
    parser.add_argument('--text', '-t', help='Text to analyze')
    parser.add_argument('--file', '-f', help='File to analyze')
    parser.add_argument('--model', '-m', default='gpt-3.5-turbo', 
                       help='AI model to use for token counting')
    parser.add_argument('--action', '-a', choices=['count', 'analyze', 'check', 'chunk', 'optimize', 'models'],
                       default='analyze', help='Action to perform')
    parser.add_argument('--max-tokens', type=int, help='Maximum tokens for chunking/optimization')
    parser.add_argument('--output', '-o', choices=['text', 'json'], default='text',
                       help='Output format')
    
    args = parser.parse_args()
    
    # Initialize token manager
    try:
        token_mgr = TokenManager()
    except Exception as e:
        print(f"Error initializing token manager: {e}")
        sys.exit(1)
    
    # Get text to analyze
    text = ""
    if args.text:
        text = args.text
    elif args.file:
        try:
            with open(args.file, 'r', encoding='utf-8') as f:
                text = f.read()
        except Exception as e:
            print(f"Error reading file: {e}")
            sys.exit(1)
    else:
        print("Please provide either --text or --file argument")
        sys.exit(1)
    
    # Perform requested action
    try:
        if args.action == 'count':
            result = token_mgr.count_tokens(text, args.model)
            output_result({'tokens': result, 'model': args.model}, args.output)
            
        elif args.action == 'analyze':
            result = token_mgr.analyze_text(text, args.model)
            output_result({
                'tokens': result.token_count,
                'words': result.word_count,
                'characters': result.character_count,
                'cost': result.estimated_cost,
                'model': result.model
            }, args.output)
            
        elif args.action == 'check':
            result = token_mgr.check_context_limit(text, args.model)
            output_result(result, args.output)
            
        elif args.action == 'chunk':
            if not args.max_tokens:
                print("--max-tokens is required for chunking")
                sys.exit(1)
            chunks = token_mgr.chunk_text(text, args.max_tokens, args.model)
            output_result({
                'chunks': chunks,
                'chunk_count': len(chunks),
                'max_tokens_per_chunk': args.max_tokens,
                'model': args.model
            }, args.output)
            
        elif args.action == 'optimize':
            if not args.max_tokens:
                print("--max-tokens is required for optimization")
                sys.exit(1)
            optimized = token_mgr.optimize_prompt(text, args.max_tokens, args.model)
            original_tokens = token_mgr.count_tokens(text, args.model)
            optimized_tokens = token_mgr.count_tokens(optimized, args.model)
            output_result({
                'original_text': text,
                'optimized_text': optimized,
                'original_tokens': original_tokens,
                'optimized_tokens': optimized_tokens,
                'tokens_saved': original_tokens - optimized_tokens,
                'target_tokens': args.max_tokens,
                'model': args.model
            }, args.output)
            
        elif args.action == 'models':
            models = token_mgr.list_models()
            model_info = {}
            for model in models:
                model_info[model] = token_mgr.get_model_info(model)
            output_result(model_info, args.output)
            
    except Exception as e:
        print(f"Error performing action: {e}")
        sys.exit(1)

def output_result(result, output_format):
    """Output result in specified format."""
    if output_format == 'json':
        print(json.dumps(result, indent=2))
    else:
        if isinstance(result, dict):
            for key, value in result.items():
                if isinstance(value, list):
                    print(f"{key}:")
                    for i, item in enumerate(value):
                        print(f"  {i+1}: {item}")
                else:
                    print(f"{key}: {value}")
        else:
            print(result)

if __name__ == "__main__":
    main()
