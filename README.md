# AI Study Assistant

An AI-powered command-line study assistant for learning and practicing
Artificial Intelligence, Machine Learning, Deep Learning, and Large
Language Models.

The project uses the Google Gemini API to provide conversational
technical explanations, streamed responses, practice-question
generation, and basic conversation usage awareness.

---

## Features

### Conversational Study Assistant

- Multi-turn conversations using Gemini Chat
- Context-aware follow-up questions
- Streaming responses
- System-level study instructions
- Technical explanations focused on understanding and reasoning

### Practice Mode

The `practice` command allows the user to configure:

- Topic
- Difficulty
- Number of questions
- Focus area

The current implementation generates the first practice question.
A full question → answer → evaluation → adaptive practice workflow is
planned for a future version.

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
| `practice` | Configure and start a practice session |
| `summary` | Display conversation statistics |
| `clear` | Clear the current conversation |
| `quit` | Exit the application |
| `exit` | Exit the application |

Any input that is not a recognized command is treated as a normal
study question and sent to Gemini.

---

## Example Usage

Start the application:

```bash
python main.py
AI Study Assistant
Type 'help' to see available commands.
You: Explain RAG in simple words
Assistant: Retrieval-Augmented Generation (RAG) combines...
```
Follow-up questions retain the conversation context:
```bash
You: What are its two main components?
Assistant: The two main components are retrieval and generation...
```
Check conversation usage:
```bash
You: summary

--- Conversation Summary ---

User messages: 2
Assistant messages: 2
Total messages: 4
Approximate tokens: ~350
```
Start practice mode:
```bash
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
# Project Structure

```bash
AI-Study-assistant/
│
├── main.py
├── chatbot.py
├── prompts.py
├── config.py
├── requirements.txt
├── .gitignore
├── .env
└── README.md
```

```main.py```

Handles the command-line interface and user interaction.

```chatbot.py```

Contains:

Gemini client initialization
Conversation management
Streaming responses
Error handling
Retry logic
Conversation statistics

```prompts.py```

Contains reusable prompt templates for:

System instructions
Concept explanations
Practice questions
Answer feedback

```config.py```

Loads environment variables and application configuration.

# Architecture

```bash
                    User
                     │
                     ▼
                  main.py
                     │
          ┌──────────┼──────────┐
          │          │          │
        Chat       Commands   Practice
          │          │          │
          ▼          ▼          ▼
                 StudyChatbot
                     │
                     ▼
             ConversationManager
                     │
                     ▼
                Gemini API
                     │
                     ▼
             Streaming Response
```

# Setup
1. Clone the repository
```bash
git clone https://github.com/Nishchalam/AI-Study-assistant.git
cd AI-Study-assistant
``` 

2. Create a virtual environment
```bash
python3 -m venv .venv
```
Activate it:
```bash
Linux/macOS
source .venv/bin/activate
Windows
.venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Configure the Gemini API key
```bash
Create a .env file:

GEMINI_API_KEY=your_api_key_here
GEMINI_MODEL=gemini-3.5-flash-lite
```

**Do not commit the .env file to GitHub.**

The project includes **.env** in **.gitignore**.

5. Run the application
```bash
python main.py
```


# Tech Stack
```bash
Python
Google Gemini API
google-genai
python-dotenv
Git/GitHub
```

# Design Approach

The project follows the learning philosophy:
```bash
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
reasoning, implementation considerations, limitations, and
research/interview relevance rather than simple definition recall.

# Current Limitations

The current version is intentionally a lightweight CLI prototype.

# Practice Mode

Practice mode currently generates the first question but does not yet
implement a complete interactive practice session.

# Planned improvements include:

* Answer submission
* Automatic answer evaluation
* Per-question feedback
* Session scoring
* Adaptive difficulty
* Weak-topic detection
* Conversation History

Conversation history is maintained by the Gemini Chat interface.
Long conversations may increase context size and API usage.

A future version could introduce:

* Conversation summarization
* History trimming
* Persistent study sessions
* Topic-specific memory
* Token Usage

The current summary command uses an approximate character-to-token
conversion. It is intended for awareness rather than precise API
billing or quota calculations.

# Future Improvements
* Full interactive practice engine
* Adaptive questioning
* Answer evaluation and feedback
* Persistent learning history
* Topic-wise progress tracking
* Retrieval-Augmented Generation (RAG)
* Personal study material ingestion
* Research-paper assistance
* Interview preparation workflows
* Web or graphical interface
* More precise API usage tracking

# Project Status

Current milestone:

Step 5 — Testing, Documentation, and Reflection

### Implemented:

* Gemini API integration
* Streaming chatbot
* Conversation management
* Prompt templates
* Error handling
* Usage summary
* CLI command system
* Practice-mode prototype

# Next major development milestone: 
Build the full interactive practice engine.