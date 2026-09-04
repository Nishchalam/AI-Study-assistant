from chatbot import StudyChatbot
def show_help():
    """Display available commands."""

    print("""
Available commands:

  help       Show available commands
  practice   Start a practice session
  summary    Show conversation statistics
  clear      Clear the conversation
  quit       Exit the application
""")
    
def main():

    chatbot = StudyChatbot()

    print("AI Study Assistant")
    print("Type 'help' to see available commands.")
    print()
    while True:

        user_input = input("You: ").strip()

        if not user_input:
            print("Please enter a question.\n")
            continue

        if user_input.lower() in {"exit", "quit"}:
            print("Goodbye.")
            break
        
        if user_input.lower() == "help":
            show_help()
            continue
        
        if user_input.lower() == "clear":
            chatbot.clear_conversation()
            print("Conversation cleared.\n")
            continue

        if user_input.lower() == "summary":

            summary = chatbot.get_summary()

            print("\n--- Conversation Summary ---")
            print(f"User messages: {summary['user_messages']}")
            print(f"Assistant messages: {summary['assistant_messages']}")
            print(f"Total messages: {summary['total_messages']}")
            print(
                f"Approximate tokens: "
                f"~{summary['approximate_tokens']}"
            )
            print()

            continue

        if user_input.lower() == "practice":

            print("\n=== Practice Mode ===\n")

            topic = input("Topic: ").strip()

            if not topic:
                print("Practice cancelled: topic cannot be empty.\n")
                continue

            print("\nDifficulty:")
            print("1. Beginner")
            print("2. Intermediate")
            print("3. Advanced")

            difficulty_choice = input("Choose difficulty [2]: ").strip()

            difficulty_map = {
                "1": "beginner",
                "2": "intermediate",
                "3": "advanced",
            }

            difficulty = difficulty_map.get(
                difficulty_choice,
                "intermediate",
            )

            number_input = input(
                "\nNumber of questions [5]: "
            ).strip()

            if number_input:
                try:
                    num_questions = int(number_input)

                    if num_questions <= 0:
                        raise ValueError

                except ValueError:
                    print(
                        "Invalid number. Using default of 5.\n"
                    )
                    num_questions = 5
            else:
                num_questions = 5

            print("\nFocus:")
            print("1. Mixed")
            print("2. Conceptual reasoning")
            print("3. Mathematical reasoning")
            print("4. Implementation")
            print("5. Interview")

            focus_choice = input("Choose focus [1]: ").strip()

            focus_map = {
                "1": "mixed",
                "2": "conceptual reasoning",
                "3": "mathematical reasoning",
                "4": "implementation",
                "5": "interview",
            }

            focus = focus_map.get(
                focus_choice,
                "mixed",
            )

            print("\n=== Practice Session ===")
            print(f"Topic: {topic}")
            print(f"Difficulty: {difficulty}")
            print(f"Questions: {num_questions}")
            print(f"Focus: {focus}")

            print("\nQuestion 1:\n")

            for chunk in chatbot.start_practice(
                topic=topic,
                difficulty=difficulty,
                focus=focus,
            ):
                print(chunk, end="", flush=True)

            print("\n")

            continue

        print("\nAssistant: ", end="", flush=True)

        for chunk in chatbot.stream_response(user_input):
            print(chunk, end="", flush=True)

        print("\n")


if __name__ == "__main__":
    main()