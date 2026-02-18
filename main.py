"""
Google ADK Lifecycle Example - Main Entry Point

This script runs the complete Google ADK lifecycle demonstration
using a local Ollama model.
"""

import asyncio
from src.lifecycle_demo import main as lifecycle_main


if __name__ == "__main__":
    asyncio.run(lifecycle_main())
