# AI Study Assistant

An AI-powered command-line study assistant for learning and practicing
Artificial Intelligence, Machine Learning, Deep Learning, and Large
Language Models.

The project uses the Google Gemini API to provide conversational
technical explanations, streamed responses, interactive practice
sessions, AI-generated questions, answer evaluation, and basic
conversation usage awareness.

---

## Features

### Conversational Study Assistant

- Multi-turn conversations using Gemini Chat
- Context-aware follow-up questions
- Streaming responses
- System-level study instructions
- Technical explanations focused on understanding and reasoning
- Concept, intuition, mathematical, implementation, interview, and
  research-oriented explanations

### Interactive Practice Mode

The `practice` command starts an interactive practice session.

The user can configure:

- Topic
- Difficulty
- Number of questions
- Focus area

The practice workflow is:

```text
Configure Session
       ↓
Generate Question
       ↓
Student Answer
       ↓
AI Evaluation
       ↓
Feedback
       ↓
Next Question
       ↓
Final Practice Report
```

Each answer is evaluated using:

- Verdict
- Score
- What was correct
- What was wrong
- Missing concepts
- Correct reasoning
- Interview-quality answer
- Follow-up question

The session also calculates an average score from the completed
evaluations.

### Error Handling

The application handles:

- Empty input
- Transient API failures
- Rate-limit errors
- Server errors
- Exponential backoff retries
- Interrupted streaming responses

Transient API errors are retried up to three times using exponential
backoff.

The implementation avoids retrying after partial streamed output to
prevent duplicated responses.

### Conversation Summary

The `summary` command displays:

- Number of user messages
- Number of assistant messages
- Total messages
- Approximate token usage

Token usage is estimated using a character-based approximation and
should not be treated as an exact billing or quota measurement.

---

## CLI Commands

| Command | Description |
|---|---|
| `help` | Display available commands |
| `practice` | Configure and start an interactive practice session |
| `summary` | Display conversation statistics |
| `clear` | Clear the current conversation |
| `quit` | Exit the application |
| `exit` | Exit the application |

Any input that is not a recognized command is treated as a normal
study question and sent to Gemini.

---

## Example Usage

### Start the application

```bash
python main.py
```

```text
AI Study Assistant
Type 'help' to see available commands.

You: Explain RAG in simple words

Assistant: Retrieval-Augmented Generation (RAG) combines...
```

### Follow-up questions

Conversation context is maintained across messages:

```text
You: What are its two main components?

Assistant: The two main components are retrieval and generation...
```

### Check conversation usage

```text
You: summary

--- Conversation Summary ---
User messages: 2
Assistant messages: 2
Total messages: 4
Approximate tokens: ~350
```

### Start a practice session

```text
You: practice

=== Practice Mode ===

Topic: Transformers

Difficulty:
1. Beginner
2. Intermediate
3. Advanced

Choose difficulty [2]: 2

Number of questions [5]: 3

Focus:
1. Mixed
2. Conceptual reasoning
3. Mathematical reasoning
4. Implementation
5. Interview

Choose focus [1]: 1
```

The application then generates a question, accepts the student's answer,
evaluates it, and continues until the configured number of questions has
been completed.

Example final report:

```text
=== Practice Report ===

Topic: Transformers
Difficulty: intermediate
Focus: mixed
Questions completed: 3
Average score: 7.7/10

Scores:
  Question 1: 8/10
  Question 2: 7/10
  Question 3: 8/10

Practice session finished.
```

---

# Project Structure

```text
AI-Study-assistant/
│
├── main.py
├── chatbot.py
├── prompts.py
├── practice.py
├── config.py
├── requirements.txt
├── .gitignore
├── README.md
└── REFLECTION.md
```

### `main.py`

Handles:

- Command-line interface
- User interaction
- Practice-session configuration
- Practice workflow
- Final practice report

### `chatbot.py`

Contains:

- Gemini client initialization
- Conversation management
- Streaming responses
- Practice question generation
- Practice answer evaluation
- Error handling
- Retry logic
- Conversation statistics

### `practice.py`

Contains the `PracticeSession` class responsible for:

- Session configuration
- Question state
- Answer storage
- Evaluation storage
- Progress tracking
- Session results

### `prompts.py`

Contains reusable prompt templates for:

- System instructions
- Concept explanations
- Practice questions
- Answer evaluation

### `config.py`

Loads environment variables and application configuration.

---

# Architecture

```text
                         User
                           │
                           ▼
                        main.py
                    CLI / Interaction
                           │
              ┌────────────┴────────────┐
              │                         │
         Normal Chat              Practice Mode
              │                         │
              ▼                         ▼
        StudyChatbot             PracticeSession
              │                         │
              ▼                         │
     ConversationManager                │
              │                         │
              └────────────┬────────────┘
                           │
                           ▼
                     Gemini API
                           │
                           ▼
                  Streaming Responses
                           │
                           ▼
                      User Output
```

Prompt generation and evaluation logic are separated into `prompts.py`,
while practice-session state is managed independently in `practice.py`.

---

# Setup

## 1. Clone the repository

```bash
git clone https://github.com/Nishchalam/AI-Study-assistant.git
cd AI-Study-assistant
```

## 2. Create a virtual environment

### Linux/macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Configure the Gemini API key

Create a `.env` file in the project root:

```text
GEMINI_API_KEY=your_api_key_here
GEMINI_MODEL=gemini-3.5-flash-lite
```

**Do not commit the `.env` file to GitHub.**

The project includes `.env` in `.gitignore`.

## 5. Run the application

```bash
python main.py
```

---

# Tech Stack

- Python
- Google Gemini API
- `google-genai`
- `python-dotenv`
- Git
- GitHub

---

# Design Approach

The project follows the learning philosophy:

```text
Understand
    ↓
Reason
    ↓
Implement
    ↓
Apply
    ↓
Critique
```

The assistant is designed to prioritize conceptual understanding,
first-principles reasoning, implementation considerations, limitations,
and research/interview relevance rather than simple definition recall.

The system prompt explicitly instructs the model to challenge
misconceptions instead of blindly agreeing with the student.

---

# Engineering Decisions

### Separation of Responsibilities

The project separates:

- CLI interaction
- Gemini API communication
- Prompt construction
- Practice-session state

This keeps the application easier to extend without placing all logic
inside `main.py`.

### Streaming

Responses are streamed to the terminal instead of waiting for the
complete model response.

This improves perceived responsiveness and demonstrates handling of
streaming API responses.

### Retry Strategy

Transient API errors such as rate limits and temporary server failures
use exponential backoff.

Responses are not retried after partial streaming output because doing so
could duplicate already-displayed content.

### Session State

Practice-session state is maintained by Python rather than relying on
the language model to track:

- Current question
- Number of questions
- Answers
- Evaluations
- Progress

The model is responsible for language generation and evaluation, while
the application controls deterministic session state.

---

# Current Limitations

This version is intentionally a lightweight CLI application.

### Practice Context

Practice mode currently uses the existing Gemini chat infrastructure.
A future version should isolate practice conversations from normal chat
context to prevent unrelated previous messages from influencing
practice questions or evaluations.

### Evaluation Validation

Practice evaluations are requested in JSON format, but the current
implementation performs lightweight parsing rather than full schema
validation.

### Persistence

Practice results and conversation history are not persisted between
application runs.

### Adaptive Learning

The current practice engine generates and evaluates questions but does
not yet dynamically adjust difficulty based on previous performance.

### Token Usage

The `summary` command estimates token usage using a character-based
approximation. It is intended for awareness rather than precise API
billing or quota calculations.

---

# Future Improvements

Potential future versions could include:

- JSON schema validation
- Separate Gemini context for practice sessions
- Adaptive difficulty
- Weak-topic detection
- Persistent learning history
- Topic-wise performance tracking
- Spaced repetition
- Retrieval-Augmented Generation (RAG)
- Personal study-material ingestion
- Research-paper assistance
- Interview preparation workflows
- Web or graphical interface
- More precise API usage tracking
- User profiles and authentication

These features are intentionally outside the scope of the current
milestone.

---

# Project Status

**Current milestone: Step 6 — Interactive Practice Engine**

### Implemented

- Gemini API integration
- Streaming chatbot
- Multi-turn conversation management
- Prompt templates
- Error handling
- Retry logic
- Conversation usage summary
- CLI command system
- Practice-session state management
- Configurable practice sessions
- AI-generated practice questions
- Student answer submission
- AI answer evaluation
- Structured evaluation output
- Per-question scoring
- Final practice-session report

The current version is a functional command-line AI study assistant
with both conversational tutoring and interactive practice capabilities.

---

# Learning Reflection

See [`REFLECTION.md`](REFLECTION.md) for the engineering and learning
reflection behind the project, including:

- Prompt design
- Conversation state management
- API cost awareness
- Error handling
- Design decisions
- Lessons learned
