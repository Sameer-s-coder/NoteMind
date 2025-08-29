from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="notemind-token-manager",
    version="1.0.0",
    author="NoteMind Team",
    description="A comprehensive token management system for AI language models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Linguistic",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "token-manager=token_cli:main",
        ],
    },
    keywords="tokens, tokenization, AI, language models, GPT, Claude, cost optimization",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/notemind/issues",
        "Source": "https://github.com/yourusername/notemind",
        "Documentation": "https://github.com/yourusername/notemind/blob/main/README.md",
    },
)
