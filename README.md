# Google ADK Lifecycle Example

A simple, educational example demonstrating the complete Google ADK (Agent Development Kit) lifecycle.

## What This Example Demonstrates

This example shows the **5 key stages** of the Google ADK lifecycle (see `adk_lifecycle.png`):

1. **Agent Initialization** - Creating an LLM agent with tools and configuration
2. **Runner & Session Service Setup** - Initializing the execution environment
3. **Invocation Creation** - How invocations are created when you run an agent
4. **Events** - Understanding event types and event actions (state_delta, artifact_delta)
5. **Event Loop** - The complete flow from user input to agent response

## The Example: Calculator Agent

A simple calculator agent that can perform basic arithmetic operations (add, subtract, multiply, divide). This demonstrates:

- Tool integration (Python functions as agent tools)
- LLM decision-making (when to call which tool)
- Event flow through the system
- Session state persistence
- Multi-turn conversations with context

## Files

- `src/calculator_agent.py` - Agent definition with calculator tools
- `src/lifecycle_demo.py` - Complete lifecycle demonstration with detailed comments
- `main.py` - Entry point to run the demo
- `.env` - Configuration file for Ollama model settings
- `adk_lifecycle.png` - Visual diagram of the ADK lifecycle

## Prerequisites

1. **Get a Groq API Key** - Sign up at [console.groq.com](https://console.groq.com)
2. **Python 3.12+** - Required for Google ADK
3. **uv package manager** - For running the project

**Note on Model Selection:** Groq provides fast inference for various models. Based on testing, these models work well with tool calling:
- `groq/qwen/qwen3-32b` (recommended - tested and working perfectly)
- `groq/llama-3.1-8b-instant` (fast and efficient)
- `groq/llama-3.1-70b-versatile` (high quality)
- `groq/mixtral-8x7b-32768` (good performance)

**Note:** `groq/llama-3.3-70b-versatile` has tool calling format compatibility issues and is not recommended.

## Configuration

Edit the `.env` file to configure your Groq API settings:

```env
# Groq API base URL (OpenAI-compatible endpoint)
GROQ_BASE_URL=https://api.groq.com/openai/v1

# Your Groq API key from console.groq.com
GROQ_API_KEY=your_groq_api_key_here

# Model name (use groq/ prefix for LiteLLM)
GROQ_MODEL=groq/qwen/qwen3-32b
```

## How to Run

```bash
# 1. Get your Groq API key from https://console.groq.com

# 2. Update .env with your API key
# GROQ_API_KEY=your_actual_api_key_here

# 3. Run the lifecycle demonstration
uv run main.py
```

## What You'll See

The demo provides an **interactive chat interface** where you can:

1. See the agent initialization and runner setup
2. Type your own calculation queries
3. Watch tool calls happen in real-time (e.g., `add(25, 17)`)
4. Get responses from the local Ollama model
5. Have multi-turn conversations with context
6. See session persistence in action

**Example interaction:**
```
🧮 You: What is 25 + 17?
[Tool Call] add({'a': 25.0, 'b': 17.0})
🤖 Agent: The sum of 25 and 17 is 42.

🧮 You: Now multiply that by 3
[Tool Call] multiply({'a': 42.0, 'b': 3.0})
🤖 Agent: 42 multiplied by 3 equals 126.
```

Type `quit` or `exit` to end the session.

## Troubleshooting

### Tools are not being called

If you see the agent responding but tools are not being called:

1. **Check your model** - Groq models have excellent tool calling support
   - ✅ Recommended: `groq/llama-3.3-70b-versatile`, `groq/llama-3.1-70b-versatile`
   - Try switching models in `.env` if you encounter issues

2. **Test with a simple query**: Try "What is 5 + 12?" and see if the `add` tool is called

### API Key errors

- Make sure you've added your Groq API key to `.env`
- Get your API key from [console.groq.com](https://console.groq.com)
- Verify the key is correctly copied (no extra spaces)

### Rate limiting

- Groq has rate limits on the free tier
- If you hit rate limits, wait a moment and try again
- Consider upgrading your Groq plan for higher limits

## Learn More

- [Google ADK Documentation](https://google.github.io/adk-docs/)
- [Event Loop Details](https://google.github.io/adk-docs/event-loop/)
- [Sessions & Memory](https://google.github.io/adk-docs/sessions/)
