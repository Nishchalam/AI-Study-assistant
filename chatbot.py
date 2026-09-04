import time

from google import genai
from google.genai import errors

from config import GEMINI_API_KEY, MODEL_NAME
from prompts import SYSTEM_PROMPT,practice_question_prompt,feedback_prompt


class ConversationManager:
    """Manages the Gemini chat session."""

    MAX_RETRIES = 3
    INITIAL_BACKOFF = 1

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

    @staticmethod
    def _is_retryable_error(error):
        """Check whether an API error is likely temporary."""

        if isinstance(error, errors.APIError):
            return error.code in {429, 500, 502, 503, 504}

        return False

    def send_message_stream(self, message):
        """Send a message and stream the response."""

        if not message.strip():
            yield "Please enter a question."
            return

        for attempt in range(self.MAX_RETRIES):

            try:
                response_stream = self.chat.send_message_stream(
                    message=message
                )

                response_started = False

                for chunk in response_stream:

                    if chunk.text:
                        response_started = True
                        yield chunk.text

                return

            except errors.APIError as error:

                # Do not retry after we have already streamed
                # part of the response. Retrying could duplicate text.
                if response_started:
                    yield (
                        "\n\n[The response was interrupted by "
                        "a temporary API error.]"
                    )
                    return

                if not self._is_retryable_error(error):
                    yield f"\n\n[API error: {error}]"
                    return

                if attempt == self.MAX_RETRIES - 1:
                    yield (
                        "\n\n[Gemini is temporarily unavailable. "
                        "Please try again later.]"
                    )
                    return

                backoff = self.INITIAL_BACKOFF * (2 ** attempt)

                print(
                    f"\n[Temporary API error. "
                    f"Retrying in {backoff} seconds...]\n"
                )

                time.sleep(backoff)

    def get_history(self):
        """Return the current conversation history."""

        return self.chat.get_history()

    def get_summary(self):
        """Return basic conversation statistics."""

        history = self.get_history()

        user_messages = 0
        assistant_messages = 0
        total_characters = 0

        for message in history:

            role = getattr(message, "role", None)

            if role == "user":
                user_messages += 1

            elif role == "model":
                assistant_messages += 1

            parts = getattr(message, "parts", None)

            if not parts:
                continue

            for part in parts:

                text = getattr(part, "text", None)

                if text:
                    total_characters += len(text)

        total_messages = user_messages + assistant_messages

        # Rough approximation:
        # 1 token ≈ 4 characters for typical English text.
        approximate_tokens = total_characters // 4

        return {
            "user_messages": user_messages,
            "assistant_messages": assistant_messages,
            "total_messages": total_messages,
            "approximate_tokens": approximate_tokens,
        }
    
    
    
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

    def start_practice(
        self,
        topic,
        difficulty="intermediate",
        focus="mixed",
    ):
        """Generate the first practice question."""

        prompt = practice_question_prompt(
            topic=topic,
            difficulty=difficulty,
            focus=focus,
        )

        yield from self.stream_response(prompt)

    def generate_practice_question(
        self,
        topic,
        difficulty="intermediate",
        focus="mixed",
    ):
        """Generate one practice question."""

        prompt = practice_question_prompt(
            topic=topic,
            difficulty=difficulty,
            focus=focus,
        )

        return self.stream_response(prompt)
    
    def evaluate_practice_answer(
        self,
        question,
        user_answer,
    ):
        """Evaluate a student's answer."""

        prompt = feedback_prompt(
            question=question,
            user_answer=user_answer,
        )

        return self.stream_response(prompt)
    
    def clear_conversation(self):
        """Clear the current conversation."""

        self.conversation.clear()

    def get_history(self):
        """Get conversation history."""

        return self.conversation.get_history()
    
    def get_summary(self):
        """Get conversation statistics."""

        return self.conversation.get_summary()