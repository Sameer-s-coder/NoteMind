import tiktoken
import re
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
import json

@dataclass
class TokenInfo:
    """Information about token usage for a piece of text."""
    text: str
    token_count: int
    word_count: int
    character_count: int
    estimated_cost: float
    model: str

class TokenManager:
    """Manages token counting and estimation for different AI models."""
    
    def __init__(self):
        self.models = {
            'gpt-3.5-turbo': {
                'context_window': 4096,
                'input_cost_per_1k': 0.0015,
                'output_cost_per_1k': 0.002
            },
            'gpt-4': {
                'context_window': 8192,
                'input_cost_per_1k': 0.03,
                'output_cost_per_1k': 0.06
            },
            'claude-3-sonnet': {
                'context_window': 200000,
                'input_cost_per_1k': 0.003,
                'output_cost_per_1k': 0.015
            }
        }
        
        # Initialize encoders for different models
        self.encoders = {}
        self._init_encoders()
    
    def _init_encoders(self):
        """Initialize token encoders for different models."""
        try:
            # GPT models use cl100k_base encoding
            self.encoders['gpt-3.5-turbo'] = tiktoken.get_encoding("cl100k_base")
            self.encoders['gpt-4'] = tiktoken.get_encoding("cl100k_base")
            # Claude models can use GPT encoding as approximation
            self.encoders['claude-3-sonnet'] = tiktoken.get_encoding("cl100k_base")
        except Exception as e:
            print(f"Warning: Could not initialize encoders: {e}")
    
    def count_tokens(self, text: str, model: str = 'gpt-3.5-turbo') -> int:
        """Count exact tokens for a given text and model."""
        if model not in self.encoders:
            raise ValueError(f"Model {model} not supported")
        
        return len(self.encoders[model].encode(text))
    
    def estimate_tokens(self, text: str, content_type: str = 'text') -> int:
        """Estimate token count based on content type."""
        if content_type == 'text':
            # Rough estimate: 1 token ≈ 0.75 words
            words = len(text.split())
            return int(words * 1.33)
        elif content_type == 'code':
            # Code is more dense: 1 token ≈ 1.5 characters
            return int(len(text) * 0.67)
        elif content_type == 'technical':
            # Technical text: 1 token ≈ 0.5 words
            words = len(text.split())
            return int(words * 2)
        else:
            return self.count_tokens(text)
    
    def analyze_text(self, text: str, model: str = 'gpt-3.5-turbo') -> TokenInfo:
        """Analyze text and return comprehensive token information."""
        token_count = self.count_tokens(text, model)
        word_count = len(text.split())
        character_count = len(text)
        
        # Calculate estimated cost
        model_info = self.models.get(model, self.models['gpt-3.5-turbo'])
        estimated_cost = (token_count / 1000) * model_info['input_cost_per_1k']
        
        return TokenInfo(
            text=text,
            token_count=token_count,
            word_count=word_count,
            character_count=character_count,
            estimated_cost=estimated_cost,
            model=model
        )
    
    def check_context_limit(self, text: str, model: str = 'gpt-3.5-turbo') -> Dict:
        """Check if text fits within model's context window."""
        token_count = self.count_tokens(text, model)
        model_info = self.models.get(model, self.models['gpt-3.5-turbo'])
        context_window = model_info['context_window']
        
        return {
            'fits': token_count <= context_window,
            'token_count': token_count,
            'context_window': context_window,
            'remaining_tokens': max(0, context_window - token_count),
            'overflow_percentage': (token_count / context_window) * 100 if context_window > 0 else 0
        }
    
    def chunk_text(self, text: str, max_tokens: int, model: str = 'gpt-3.5-turbo') -> List[str]:
        """Split text into chunks that fit within token limit."""
        chunks = []
        current_chunk = ""
        current_tokens = 0
        
        # Split by sentences for better chunking
        sentences = re.split(r'[.!?]+', text)
        
        for sentence in sentences:
            sentence = sentence.strip()
            if not sentence:
                continue
                
            sentence_tokens = self.count_tokens(sentence, model)
            
            if current_tokens + sentence_tokens <= max_tokens:
                current_chunk += sentence + ". "
                current_tokens += sentence_tokens
            else:
                if current_chunk:
                    chunks.append(current_chunk.strip())
                current_chunk = sentence + ". "
                current_tokens = sentence_tokens
        
        if current_chunk:
            chunks.append(current_chunk.strip())
        
        return chunks
    
    def optimize_prompt(self, prompt: str, target_tokens: int, model: str = 'gpt-3.5-turbo') -> str:
        """Optimize prompt to fit within target token count."""
        current_tokens = self.count_tokens(prompt, model)
        
        if current_tokens <= target_tokens:
            return prompt
        
        # Try to reduce tokens by removing unnecessary words
        words = prompt.split()
        optimized_words = []
        current_count = 0
        
        for word in words:
            test_prompt = " ".join(optimized_words + [word])
            test_tokens = self.count_tokens(test_prompt, model)
            
            if test_tokens <= target_tokens:
                optimized_words.append(word)
                current_count = test_tokens
            else:
                break
        
        return " ".join(optimized_words)
    
    def get_model_info(self, model: str) -> Dict:
        """Get information about a specific model."""
        return self.models.get(model, {})
    
    def list_models(self) -> List[str]:
        """List all supported models."""
        return list(self.models.keys())
    
    def calculate_conversation_tokens(self, messages: List[Dict], model: str = 'gpt-3.5-turbo') -> Dict:
        """Calculate token usage for a conversation."""
        total_tokens = 0
        input_tokens = 0
        output_tokens = 0
        
        for message in messages:
            role = message.get('role', 'user')
            content = message.get('content', '')
            
            if role == 'user':
                tokens = self.count_tokens(content, model)
                input_tokens += tokens
                total_tokens += tokens
            elif role == 'assistant':
                tokens = self.count_tokens(content, model)
                output_tokens += tokens
                total_tokens += tokens
        
        # Calculate costs
        model_info = self.models.get(model, self.models['gpt-3.5-turbo'])
        input_cost = (input_tokens / 1000) * model_info['input_cost_per_1k']
        output_cost = (output_tokens / 1000) * model_info['output_cost_per_1k']
        total_cost = input_cost + output_cost
        
        return {
            'total_tokens': total_tokens,
            'input_tokens': input_tokens,
            'output_tokens': output_tokens,
            'input_cost': input_cost,
            'output_cost': output_cost,
            'total_cost': total_cost,
            'fits_context': total_tokens <= model_info['context_window']
        }

# Example usage and testing
if __name__ == "__main__":
    # Initialize token manager
    token_mgr = TokenManager()
    
    # Example text
    sample_text = "Hello! This is a sample text to demonstrate token counting. It contains multiple sentences and should give us a good example of how the token manager works."
    
    # Analyze text
    analysis = token_mgr.analyze_text(sample_text)
    print(f"Text Analysis:")
    print(f"Tokens: {analysis.token_count}")
    print(f"Words: {analysis.word_count}")
    print(f"Characters: {analysis.character_count}")
    print(f"Estimated Cost: ${analysis.estimated_cost:.6f}")
    
    # Check context limits
    context_check = token_mgr.check_context_limit(sample_text)
    print(f"\nContext Check:")
    print(f"Fits in context: {context_check['fits']}")
    print(f"Remaining tokens: {context_check['remaining_tokens']}")
    
    # List available models
    print(f"\nAvailable Models: {token_mgr.list_models()}")
