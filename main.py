from chatbot import StudyChatbot


def main():

    chatbot = StudyChatbot()

    print("AI Study Assistant")
    print("Type 'exit' to quit.")
    print("Type 'clear' to clear the conversation.")
    print()

    while True:

        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        if user_input.lower() == "clear":
            chatbot.clear_conversation()
            print("Conversation cleared.\n")
            continue

        print("\nAssistant: ", end="", flush=True)

        for chunk in chatbot.stream_response(user_input):
            print(chunk, end="", flush=True)

        print("\n")


if __name__ == "__main__":
    main()