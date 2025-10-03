"""
Simple AI Q&A Chatbot using Meta LLaMA 3.1 8B via Groq API
Single file implementation - just run and chat!
"""

import os
from groq import Groq
from dotenv import load_dotenv

def main():
    # Load environment variables from .env file
    load_dotenv()

    # Get API key from environment
    api_key = os.getenv('GROQ_API_KEY')

    if not api_key:
        print("❌ Error: GROQ_API_KEY not found in .env file!")
        print("Add this line to your .env file: GROQ_API_KEY=your_actual_key_here")
        return

    # Initialize Groq client
    client = Groq(api_key=api_key)

    # System message for the conversation
    messages = [
        {
            "role": "system",
            "content": "You are a helpful AI assistant. Provide clear, accurate, and concise answers."
        }
    ]

    print("🚀 AI Q&A Bot (Meta LLaMA 3.1 8B via Groq)")
    print("=" * 50)
    print("Ask me anything! Type 'quit', 'exit', or 'bye' to stop.")
    print("=" * 50)

    while True:
        try:
            # Get user input
            user_input = input("\n💬 You: ").strip()

            # Check for exit commands
            if user_input.lower() in ['quit', 'exit', 'bye', 'q']:
                print("\n👋 Thanks for chatting! Goodbye!")
                break

            # Skip empty inputs
            if not user_input:
                continue

            # Add user message to conversation
            messages.append({"role": "user", "content": user_input})

            print("\n🤔 Thinking...")

            # Get response from Groq using LLaMA 3.1 8B
            chat_completion = client.chat.completions.create(
                messages=messages,
                model="llama-3.1-8b-instant",  # Meta LLaMA 3.1 8B model
                max_tokens=200,
                temperature=0.7,
            )

            # Extract and display response
            response = chat_completion.choices[0].message.content
            print(f"\n🤖 Bot: {response}")

            # Add response to conversation history
            messages.append({"role": "assistant", "content": response})

        except KeyboardInterrupt:
            print("\n\n👋 Chat interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}")
            print("Please check your API key and internet connection.")
            continue

if __name__ == "__main__":
    main()
