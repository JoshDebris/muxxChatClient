import time
import os
from colored import Fore, attr
import google.generativeai as genai
from yaspin import yaspin
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure API with environment variable
api_key = os.getenv("GENAI_API_KEY")
if not api_key:
    print("❌ ERROR: API Key not found. Please set GENAI_API_KEY in your .env file.")
    exit(1)

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

def chat():
    # Welcome Message
    print(f"{Fore.GREEN}Welcome to the ChatBot! (Enter 'exit' to end the conversation.){attr('reset')}")
    context = []  # Context as a list to manage history better

    while True:
        # User input
        user_input = input(f"{Fore.CYAN}👽 Du: {attr('reset')}")

        # Option to end the conversation
        if user_input.lower() == "exit":
            print("See you again!")
            break

        # Update context
        context.append(f"Du: {user_input}")

        # Limit context history to last 10 exchanges
        if len(context) > 20:
            context = context[-20:]

        # Prepare context string for API
        context_str = "\n".join(context)

        # Spinner during processing
        with yaspin(text="Thinking...", color="yellow") as spinner:
            try:
                response = model.generate_content(context_str)
                bot_reply = response.text.strip()
                spinner.ok("✔️")
            except Exception as e:
                spinner.fail("💥")
                print(f"{Fore.RED}API Error:{attr('reset')} {e}")
                continue

        # Remove a double “Bot:” prefix, if present
        if bot_reply.lower().startswith("bot:"):
            bot_reply = bot_reply[4:].strip()

        # Update context with the bot's reply
        context.append(f"Bot: {bot_reply}")

        # Show bot's answer
        print(f"{Fore.YELLOW}🤖 Bot:{attr('reset')} {bot_reply}\n")

# Start the Chat
if __name__ == "__main__":
    chat()
