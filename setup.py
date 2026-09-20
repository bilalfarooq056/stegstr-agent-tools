from setuptools import setup, find_packages

setup(
    name="stegstr-agent-tools",
    version="0.1.0",
    author="Bilal",
    description="A Python wrapper for Stegstr CLI, allowing AI agents to easily hide and transfer secret data in images.",
    long_description="An open-source integration tool for AI agents (LangChain, AutoGen, etc.) to perform steganography and post secure data using Stegstr.",
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires='>=3.7',
)