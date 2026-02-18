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

1. **Install Ollama** - Download from [ollama.com](https://ollama.com)
2. **Pull a model** - Run `ollama pull llama3.2` (recommended for tool calling)
3. **Start Ollama** - Run `ollama serve` (usually starts automatically)

**Note on Model Selection:** For best tool calling support with Ollama, use models like:
- `llama3.2` (recommended)
- `llama3.1`
- `mistral`
- `qwen2.5`

Some smaller models may have limited tool calling capabilities.

## Configuration

Edit the `.env` file to configure your local model:

```env
# The model name with ollama/ prefix (e.g., ollama/llama3.2, ollama/mistral)
MODEL_NAME=ollama/llama3.2

# Ollama API base URL (default: http://localhost:11434)
BASE_URL=http://localhost:11434
```

## How to Run

```bash
# Pull a recommended model (if not already installed)
ollama pull llama3.2

# Make sure Ollama is running
ollama list  # Verify your model is available

# Update .env with your model name
# MODEL_NAME=ollama/llama3.2

# Run the lifecycle demonstration
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

1. **Check your model** - Some Ollama models have better tool calling support than others
   - ✅ Recommended: `llama3.2`, `llama3.1`, `mistral`, `qwen2.5`
   - ⚠️ Limited support: Smaller models like `qwen3:4b` may not work well

2. **Update your model**:
   ```bash
   ollama pull llama3.2
   # Update .env: MODEL_NAME=ollama/llama3.2
   ```

3. **Test with a simple query**: Try "What is 5 + 12?" and see if the `add` tool is called

### Agent returns empty responses

- Make sure Ollama is running: `ollama serve`
- Verify the model is loaded: `ollama list`
- Check the BASE_URL in `.env` matches your Ollama endpoint

## Learn More

- [Google ADK Documentation](https://google.github.io/adk-docs/)
- [Event Loop Details](https://google.github.io/adk-docs/event-loop/)
- [Sessions & Memory](https://google.github.io/adk-docs/sessions/)
