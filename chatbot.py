from google import genai

from config import GEMINI_API_KEY, MODEL_NAME
from prompts import SYSTEM_PROMPT


class ConversationManager:
    """Manages the Gemini chat session."""

    def __init__(self, client, model_name):
        self.client = client
        self.model_name = model_name
        self.chat = self._create_chat()

    def _create_chat(self):
        return self.client.chats.create(
            model=self.model_name,
            config={
                "system_instruction": SYSTEM_PROMPT,
            },
        )

    def send_message_stream(self, message):
        """Send a message and stream the response."""

        response_stream = self.chat.send_message_stream(
            message=message
        )

        full_response = ""

        for chunk in response_stream:
            if chunk.text:
                full_response += chunk.text
                yield chunk.text

    def get_history(self):
        """Return the current conversation history."""
        return self.chat.get_history()

    def clear(self):
        """Start a fresh conversation."""
        self.chat = self._create_chat()


class StudyChatbot:
    """Main interface for the AI Study Assistant."""

    def __init__(self):
        self.client = genai.Client(
            api_key=GEMINI_API_KEY
        )

        self.conversation = ConversationManager(
            client=self.client,
            model_name=MODEL_NAME,
        )

    def stream_response(self, user_message):
        """Stream a response to the user's message."""

        yield from self.conversation.send_message_stream(
            user_message
        )

    def clear_conversation(self):
        """Clear the current conversation."""

        self.conversation.clear()

    def get_history(self):
        """Get conversation history."""

        return self.conversation.get_history()