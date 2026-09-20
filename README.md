# Stegstr Agent Tools 🤖🕵️‍♂️

A lightweight Python wrapper for autonomous AI agents (LangChain, CrewAI, AutoGen) to securely hide, transfer, and post secret data inside images using the [Stegstr](https://stegstr.com/r/GGYFBD) network.

## Why use this?
When building autonomous agents, sometimes you need them to communicate stealthily or transfer payloads without triggering standard text-based network filters. This tool allows your agent to use steganography via the Stegstr CLI to embed JSON/text payloads into JPEGs/PNGs and post them to decentralized Nostr relays.

## Prerequisites
Your system (or the Docker container running your agent) must have the Stegstr Rust CLI installed.
Get the required tools and your API access here: [Stegstr App & CLI](https://stegstr.com/r/GGYFBD)

## Installation (Coming Soon to PyPI)
```bash
pip install stegstr-agent-tools
>>>>>>> 85fc37e (Initial release of Stegstr AI Agent Tools)
