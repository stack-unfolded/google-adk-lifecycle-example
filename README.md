# Google ADK Calculator Agent

An interactive calculator agent demonstrating the Google ADK (Agent Development Kit) lifecycle.

## What It Does

A calculator agent that performs arithmetic operations (add, subtract, multiply, divide) using:
- **Groq API** for fast LLM inference
- **Tool calling** to execute Python functions
- **Interactive chat** for hands-on learning

## Quick Start

### 1. Clone and Setup

```bash
git clone https://github.com/stack-unfolded/google-adk-lifecycle-example.git

# Create .env file
cp .example.env .env  # Or create manually
```

### 2. Get Groq API Key

Sign up at [console.groq.com](https://console.groq.com) and get your API key.

### 3. Configure

Edit `.env`:

```env
GROQ_BASE_URL=https://api.groq.com/openai/v1
GROQ_API_KEY=your_api_key_here
GROQ_MODEL=groq/qwen/qwen3-32b
```

### 4. Run

```bash
uv run main.py
```

## Example Usage

```
🧮 You: What is 100 divided by 4?
[Tool Call] divide({'a': 100, 'b': 4})
[Tool Result] divide returned: {'result': 25.0}
🤖 Agent: 100 divided by 4 equals 25.

🧮 You: quit
```

## Project Structure

```
example-adk/
├── src/
│   ├── calculator_agent.py    # Agent with calculator
│   └── lifecycle_demo.py      # Interactive demo
├── main.py                    # Entry point
├── .env                       # Configuration
└── README.md
```

## Recommended Models

Tested and working:
- `groq/qwen/qwen3-32b` ✅ (recommended)
- `openai/gpt-oss-20b` ✅

## Requirements

- Python 3.12+
- uv package manager
- Groq API key
