"""
Calculator Agent - A simple agent demonstrating Google ADK lifecycle.

This agent can perform basic arithmetic operations using custom tools.
It demonstrates how agents are initialized with tools and configuration.
"""

import os
from dotenv import load_dotenv
from google.adk.agents.llm_agent import LlmAgent
from google.adk.models.lite_llm import LiteLlm
from google.adk.tools.function_tool import FunctionTool

# Load environment variables from .env file
load_dotenv()


# ============================================================================
# STEP 1: Define Tools (Functions the agent can call)
# ============================================================================

def add(a: float, b: float) -> float:
    """Add two numbers together.

    Args:
        a: First number
        b: Second number

    Returns:
        The sum of a and b
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """Subtract b from a.

    Args:
        a: First number
        b: Second number to subtract

    Returns:
        The difference a - b
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """Multiply two numbers.

    Args:
        a: First number
        b: Second number

    Returns:
        The product of a and b
    """
    return a * b


def divide(a: float, b: float) -> float:
    """Divide a by b.

    Args:
        a: Numerator
        b: Denominator (cannot be zero)

    Returns:
        The quotient a / b
    """
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b


# ============================================================================
# STEP 2: Create the Agent
# ============================================================================

def create_calculator_agent() -> LlmAgent:
    """
    Creates and configures a Calculator Agent.

    This demonstrates AGENT INITIALIZATION - one of the key lifecycle stages.

    Returns:
        A configured LlmAgent instance ready to perform calculations
    """
    print("\n" + "="*70)
    print("LIFECYCLE STAGE 1: AGENT INITIALIZATION")
    print("="*70)

    # Wrap Python functions as ADK tools
    tools = [
        FunctionTool(add),
        FunctionTool(subtract),
        FunctionTool(multiply),
        FunctionTool(divide),
    ]

    # Get model configuration from environment variables
    # Groq API configuration
    model_name = os.getenv("GROQ_MODEL", "groq/llama3-70b-8192")
    api_key = os.getenv("GROQ_API_KEY")
    base_url = os.getenv("GROQ_BASE_URL", "https://api.groq.com/openai/v1")

    if not api_key:
        raise ValueError("GROQ_API_KEY not found in .env file. Please add your Groq API key.")

    # Create the LLM Agent with LiteLLM configuration for Groq
    agent = LlmAgent(
        name="calculator_agent",
        model=LiteLlm(
            model=model_name,
            api_base=base_url,
            api_key=api_key,
        ),
        tools=tools,
        instruction=(
            "You are a helpful calculator assistant. "
            "When users ask you to perform calculations, use the available tools. "
            "Always show your work and explain the result."
        ),
    )

    print(f"✓ Agent: {agent.name}")
    print(f"✓ Model: {model_name} @ {base_url}")
    print(f"✓ Tools: {', '.join([tool.name for tool in tools])}")
    print("="*70 + "\n")

    return agent

