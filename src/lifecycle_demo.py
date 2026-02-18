"""
Google ADK Lifecycle Demonstration - Interactive Mode

This script demonstrates the complete Google ADK agent lifecycle interactively:
1. Agent Initialization
2. Runner Initialization with Session Service
3. Invocation Creation (happens when you send a message)
4. Events and Event Loop (watch events as they happen)
5. State Management (session persists across messages)

Type your calculation queries and see the agent respond!
"""

import asyncio
from google.adk.runners import Runner
from google.adk.sessions.in_memory_session_service import InMemorySessionService
from google.genai import types

from .calculator_agent import create_calculator_agent


async def main():
    """
    Interactive demonstration of the Google ADK lifecycle.
    """

    # ========================================================================
    # LIFECYCLE STAGE 1: AGENT INITIALIZATION
    # ========================================================================
    agent = create_calculator_agent()


    # ========================================================================
    # LIFECYCLE STAGE 2: RUNNER INITIALIZATION WITH SESSION SERVICE
    # ========================================================================
    print("="*70)
    print("LIFECYCLE STAGE 2: RUNNER & SESSION SERVICE INITIALIZATION")
    print("="*70)

    session_service = InMemorySessionService()
    print("✓ Created InMemorySessionService")

    runner = Runner(
        app_name="calculator_app",
        agent=agent,
        session_service=session_service,
        auto_create_session=True,
    )
    print("✓ Created Runner")
    print(f"  → App: {runner.app_name}, Agent: {runner.agent.name}")
    print("="*70 + "\n")
    

    # ========================================================================
    # INTERACTIVE CHAT LOOP
    # ========================================================================
    print("="*70)
    print("INTERACTIVE CHAT - Try the Calculator Agent!")
    print("="*70)
    print("Type your calculation queries (e.g., 'What is 15 + 27?')")
    print("Type 'quit' or 'exit' to end the session")
    print("="*70 + "\n")

    user_id = "demo_user"
    session_id = "demo_session_001"

    while True:
        # Get user input
        try:
            user_input = input("\n🧮 You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n\nExiting...")
            break

        if not user_input:
            continue

        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("\n👋 Goodbye!")
            break

        # Create user message
        user_message = types.Content(
            role="user",
            parts=[types.Part(text=user_input)]
        )

        print("\n" + "-" * 70)
        print("LIFECYCLE STAGES 3-5: Invocation → Events → Event Loop")
        print("-" * 70)

        # Run the agent and collect response
        agent_response = ""

        async for event in runner.run_async(
            user_id=user_id,
            session_id=session_id,
            new_message=user_message,
        ):
            # Show function calls (tool usage)
            if event.get_function_calls():
                function_calls = event.get_function_calls()
                for fc in function_calls:
                    print(f"[Tool Call] {fc.name}({fc.args})")

            # Show function responses (tool results)
            if event.get_function_responses():
                function_responses = event.get_function_responses()
                for fr in function_responses:
                    print(f"[Tool Result] {fr.name} returned: {fr.response}")

            # Collect agent's final response (text content)
            if event.content and event.content.parts and event.author == "calculator_agent":
                text_parts = [p.text for p in event.content.parts if p.text]
                if text_parts:
                    agent_response = text_parts[0]

        # Display agent response
        if agent_response:
            print(f"\n🤖 Agent: {agent_response}")
        else:
            print(f"\n🤖 Agent: [Completed tool calls]")

        print("-" * 70)

    # Show session summary
    session = await session_service.get_session(
        app_name="calculator_app",
        user_id=user_id,
        session_id=session_id,
    )

    print("\n" + "="*70)
    print("SESSION SUMMARY")
    print("="*70)
    print(f"Total events in session: {len(session.events)}")
    print(f"Session persisted all conversation history and tool calls")
    print("="*70)


if __name__ == "__main__":
    asyncio.run(main())

