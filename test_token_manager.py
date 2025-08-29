#!/usr/bin/env python3
"""
Tests for the TokenManager class.
"""

import unittest
from unittest.mock import patch, MagicMock
from token_manager import TokenManager, TokenInfo

class TestTokenManager(unittest.TestCase):
    """Test cases for TokenManager class."""
    
    def setUp(self):
        """Set up test fixtures."""
        with patch('tiktoken.get_encoding') as mock_encoding:
            mock_encoder = MagicMock()
            mock_encoder.encode.return_value = [1, 2, 3, 4, 5]  # 5 tokens
            mock_encoding.return_value = mock_encoder
            
            self.token_mgr = TokenManager()
    
    def test_init(self):
        """Test TokenManager initialization."""
        self.assertIsInstance(self.token_mgr.models, dict)
        self.assertIn('gpt-3.5-turbo', self.token_mgr.models)
        self.assertIn('gpt-4', self.token_mgr.models)
        self.assertIn('claude-3-sonnet', self.token_mgr.models)
    
    def test_count_tokens(self):
        """Test token counting functionality."""
        text = "Hello world"
        tokens = self.token_mgr.count_tokens(text)
        self.assertEqual(tokens, 5)
    
    def test_count_tokens_unsupported_model(self):
        """Test token counting with unsupported model."""
        with self.assertRaises(ValueError):
            self.token_mgr.count_tokens("Hello", "unsupported-model")
    
    def test_estimate_tokens_text(self):
        """Test token estimation for text content."""
        text = "Hello world this is a test"
        estimated = self.token_mgr.estimate_tokens(text, 'text')
        # 6 words * 1.33 ≈ 8 tokens
        self.assertGreaterEqual(estimated, 6)
    
    def test_estimate_tokens_code(self):
        """Test token estimation for code content."""
        code = "def hello(): return 'world'"
        estimated = self.token_mgr.estimate_tokens(code, 'code')
        # 25 characters * 0.67 ≈ 17 tokens
        self.assertGreaterEqual(estimated, 15)
    
    def test_estimate_tokens_technical(self):
        """Test token estimation for technical content."""
        technical = "This is technical documentation with complex terminology"
        estimated = self.token_mgr.estimate_tokens(technical, 'technical')
        # 8 words * 2 = 16 tokens
        self.assertEqual(estimated, 16)
    
    def test_analyze_text(self):
        """Test comprehensive text analysis."""
        text = "Hello world"
        analysis = self.token_mgr.analyze_text(text)
        
        self.assertIsInstance(analysis, TokenInfo)
        self.assertEqual(analysis.text, text)
        self.assertEqual(analysis.token_count, 5)
        self.assertEqual(analysis.word_count, 2)
        self.assertEqual(analysis.character_count, 11)
        self.assertIsInstance(analysis.estimated_cost, float)
        self.assertEqual(analysis.model, 'gpt-3.5-turbo')
    
    def test_check_context_limit(self):
        """Test context limit checking."""
        text = "Hello world"
        result = self.token_mgr.check_context_limit(text)
        
        self.assertIn('fits', result)
        self.assertIn('token_count', result)
        self.assertIn('context_window', result)
        self.assertIn('remaining_tokens', result)
        self.assertIn('overflow_percentage', result)
        
        self.assertTrue(result['fits'])
        self.assertEqual(result['token_count'], 5)
        self.assertEqual(result['context_window'], 4096)
    
    def test_chunk_text(self):
        """Test text chunking functionality."""
        long_text = "First sentence. Second sentence. Third sentence. Fourth sentence."
        chunks = self.token_mgr.chunk_text(long_text, max_tokens=10)
        
        self.assertIsInstance(chunks, list)
        self.assertGreater(len(chunks), 1)
        
        # Each chunk should be within token limit
        for chunk in chunks:
            tokens = self.token_mgr.count_tokens(chunk)
            self.assertLessEqual(tokens, 10)
    
    def test_optimize_prompt(self):
        """Test prompt optimization."""
        long_prompt = "This is a very long prompt that needs to be optimized to fit within token limits"
        optimized = self.token_mgr.optimize_prompt(long_prompt, target_tokens=10)
        
        self.assertIsInstance(optimized, str)
        self.assertLessEqual(len(optimized), len(long_prompt))
        
        # Check if optimized prompt fits within target
        tokens = self.token_mgr.count_tokens(optimized)
        self.assertLessEqual(tokens, 10)
    
    def test_get_model_info(self):
        """Test model information retrieval."""
        info = self.token_mgr.get_model_info('gpt-3.5-turbo')
        self.assertIn('context_window', info)
        self.assertIn('input_cost_per_1k', info)
        self.assertIn('output_cost_per_1k', info)
    
    def test_list_models(self):
        """Test model listing."""
        models = self.token_mgr.list_models()
        self.assertIsInstance(models, list)
        self.assertIn('gpt-3.5-turbo', models)
        self.assertIn('gpt-4', models)
    
    def test_calculate_conversation_tokens(self):
        """Test conversation token calculation."""
        conversation = [
            {"role": "user", "content": "Hello"},
            {"role": "assistant", "content": "Hi there"},
            {"role": "user", "content": "How are you?"}
        ]
        
        result = self.token_mgr.calculate_conversation_tokens(conversation)
        
        self.assertIn('total_tokens', result)
        self.assertIn('input_tokens', result)
        self.assertIn('output_tokens', result)
        self.assertIn('total_cost', result)
        self.assertIn('fits_context', result)
        
        # Should have 3 messages * 5 tokens each = 15 total
        self.assertEqual(result['total_tokens'], 15)
        self.assertEqual(result['input_tokens'], 10)  # 2 user messages
        self.assertEqual(result['output_tokens'], 5)  # 1 assistant message

class TestTokenInfo(unittest.TestCase):
    """Test cases for TokenInfo dataclass."""
    
    def test_token_info_creation(self):
        """Test TokenInfo object creation."""
        info = TokenInfo(
            text="Hello world",
            token_count=5,
            word_count=2,
            character_count=11,
            estimated_cost=0.001,
            model="gpt-3.5-turbo"
        )
        
        self.assertEqual(info.text, "Hello world")
        self.assertEqual(info.token_count, 5)
        self.assertEqual(info.word_count, 2)
        self.assertEqual(info.character_count, 11)
        self.assertEqual(info.estimated_cost, 0.001)
        self.assertEqual(info.model, "gpt-3.5-turbo")

if __name__ == '__main__':
    unittest.main()
