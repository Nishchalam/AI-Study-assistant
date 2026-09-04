# Technical Reflection

## 1. Prompt Design

A major design decision in this project was to separate the assistant's
behavior from the application logic.

The system prompt defines the overall role of the AI Study Assistant,
including its emphasis on conceptual understanding, first-principles
reasoning, mathematical rigor, implementation, research, and interview
readiness.

Specific tasks such as concept explanation, practice-question
generation, and answer evaluation are represented using separate prompt
functions.

This separation makes the prompts easier to modify and test without
changing the chatbot implementation.

One important lesson was that prompt design is not simply about adding
more instructions. The instructions need to be structured around the
actual behavior we want from the model. For example, practice questions
should test reasoning rather than only definition recall.

---

## 2. Conversation State Management

The first implementation attempted to represent conversation history
using a generic message structure. This caused compatibility problems
with the Gemini API because its expected content representation differs
from the message format used by some other LLM APIs.

The solution was to use Gemini's native Chat interface to manage
multi-turn conversation state.

This provided a cleaner architecture:

User input
    ↓
Gemini Chat
    ↓
Conversation history
    ↓
Streaming response

The `ConversationManager` class separates conversation state from the
CLI and the higher-level `StudyChatbot` interface.

The project currently relies on the Gemini Chat session to maintain
conversation history. A limitation of this approach is that long
conversations can increase context size and API usage.

A future version could introduce conversation summarization and
selective history retention so that older information can be compressed
without losing important context.

---

## 3. API Cost Awareness

Working with an LLM API introduced an important engineering
consideration: every interaction has a computational and potentially
financial cost.

Conversation history is particularly relevant because previous messages
can become part of the context for subsequent requests. As a
conversation becomes longer, the amount of information processed by the
model can increase.

The `summary` command was therefore added to provide basic usage
awareness. It reports the number of user and assistant messages and
provides an approximate token count.

The current token calculation is intentionally simple and uses a
character-based approximation. It is useful for awareness but should
not be treated as an exact representation of API usage or billing.

A future implementation should use the token-usage metadata provided by
the API where available.

---

## 4. Error Handling

The project also demonstrated why API integrations should not assume
that every request will succeed.

During development, the Gemini API returned a `503 UNAVAILABLE` error
because the selected model was temporarily experiencing high demand.

Instead of allowing the application to terminate with a traceback,
transient errors are now handled using retry logic with exponential
backoff.

The current implementation retries selected transient errors such as
429, 500, 502, 503, and 504.

An important consideration is streaming. If part of a response has
already been displayed, retrying the entire request could produce
duplicated content. The implementation therefore treats an interrupted
stream differently from a request that fails before streaming begins.

---

## 5. Overall Learning

This project demonstrated that building an LLM application involves
more than sending a prompt to an API.

The main engineering considerations were:

- designing reliable prompts
- managing conversational state
- handling API failures
- controlling API usage
- separating application responsibilities
- designing a usable CLI
- documenting limitations honestly

The current implementation is intentionally a small foundation rather
than a complete intelligent tutoring system.

The next significant improvement would be to build a dedicated
interactive practice engine that can generate one question at a time,
evaluate the student's answer, provide targeted feedback, track
performance, and adapt subsequent questions based on weaknesses.