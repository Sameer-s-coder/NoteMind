"""
Configuration file for NoteMind Token Manager
Customize models, costs, and settings here.
"""

# Model configurations
MODELS = {
    'gpt-3.5-turbo': {
        'context_window': 4096,
        'input_cost_per_1k': 0.0015,
        'output_cost_per_1k': 0.002,
        'description': 'Fast and cost-effective for most tasks'
    },
    'gpt-3.5-turbo-16k': {
        'context_window': 16384,
        'input_cost_per_1k': 0.003,
        'output_cost_per_1k': 0.004,
        'description': 'Extended context for longer documents'
    },
    'gpt-4': {
        'context_window': 8192,
        'input_cost_per_1k': 0.03,
        'output_cost_per_1k': 0.06,
        'description': 'Most capable model for complex tasks'
    },
    'gpt-4-32k': {
        'context_window': 32768,
        'input_cost_per_1k': 0.06,
        'output_cost_per_1k': 0.12,
        'description': 'Extended context GPT-4 for large documents'
    },
    'claude-3-sonnet': {
        'context_window': 200000,
        'input_cost_per_1k': 0.003,
        'output_cost_per_1k': 0.015,
        'description': 'Anthropic model with very long context'
    },
    'claude-3-haiku': {
        'context_window': 200000,
        'input_cost_per_1k': 0.00025,
        'output_cost_per_1k': 0.00125,
        'description': 'Fast and cost-effective Claude model'
    }
}

# Default settings
DEFAULT_MODEL = 'gpt-3.5-turbo'
DEFAULT_OUTPUT_FORMAT = 'text'  # 'text' or 'json'

# Token estimation settings
TOKEN_ESTIMATION = {
    'text': 1.33,        # tokens per word for general text
    'code': 0.67,        # tokens per character for code
    'technical': 2.0,    # tokens per word for technical content
    'conversation': 1.2  # tokens per word for conversations
}

# Chunking settings
CHUNKING = {
    'default_max_tokens': 1000,
    'overlap_tokens': 50,        # tokens to overlap between chunks
    'min_chunk_tokens': 100,     # minimum tokens per chunk
    'preserve_sentences': True   # try to keep sentences intact
}

# Cost thresholds for warnings
COST_THRESHOLDS = {
    'warning': 0.01,     # warn when cost exceeds $0.01
    'critical': 0.10,    # critical warning at $0.10
    'max_daily': 1.00    # maximum recommended daily cost
}

# Output formatting
OUTPUT_FORMATS = {
    'text': {
        'show_tokens': True,
        'show_cost': True,
        'show_percentage': True,
        'show_warnings': True
    },
    'json': {
        'pretty_print': True,
        'include_metadata': True
    }
}

# Logging settings
LOGGING = {
    'level': 'INFO',     # DEBUG, INFO, WARNING, ERROR
    'log_to_file': False,
    'log_file': 'token_manager.log'
}

# Performance settings
PERFORMANCE = {
    'cache_results': True,
    'cache_size': 1000,  # number of cached results
    'batch_size': 100,   # process texts in batches
    'timeout_seconds': 30
}
