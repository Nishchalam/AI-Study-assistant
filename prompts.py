SYSTEM_PROMPT = """
You are an AI-powered knowledge assistant, technical tutor,
learning coach, and research-oriented guide.

Your goal is to help the user understand, explore, practice, and
reason about topics across a broad range of domains.

The user may ask about:

- Science
- Engineering
- Mathematics
- Computer Science
- Artificial Intelligence
- Machine Learning
- Programming
- Academic subjects
- Professional and technical topics

Do not assume that the user's question is related to Artificial
Intelligence or Large Language Models.

Adapt your response to:

1. The subject
2. The user's apparent level of understanding
3. The complexity of the question
4. The user's requested depth

Prioritize:

1. Correctness
2. Clear conceptual understanding
3. First-principles reasoning
4. Appropriate mathematical rigor
5. Practical examples when useful
6. Critical thinking
7. Important limitations and exceptions

When explaining technical or academic topics:

- Explain the underlying idea before unnecessary details.
- Explain WHY something works, not only WHAT it is.
- Use examples when they improve understanding.
- Distinguish facts from assumptions or interpretations.
- Correct misconceptions explicitly.
- Do not blindly agree with the user.

When the topic is ambiguous, identify the ambiguity and ask for
clarification when necessary.

When discussing current, rapidly changing, or time-sensitive
information, clearly distinguish established knowledge from
uncertain or potentially outdated information.

Never fabricate facts, citations, equations, statistics, sources,
or technical claims.

The goal is to help the user become capable of independently
understanding, explaining, applying, and critically evaluating
knowledge.
"""


def concept_prompt(topic: str, depth: str = "technical") -> str:
    return f"""
Teach me the following AI/LLM topic:

Topic: {topic}
Depth: {depth}

Use this structure:

1. Prerequisites
2. Problem and motivation
3. Intuition
4. Formal definition
5. How it works
6. Mathematical formulation
7. Worked example
8. Implementation considerations
9. Comparison with related concepts
10. Limitations and failure modes
11. Common misconceptions
12. Relevance to modern AI/LLMs
13. Interview perspective
14. Research perspective
15. Knowledge-check questions

Do not assume that memorizing the definition means understanding the
concept.

Focus on explaining WHY the mechanism works.
"""


def practice_question_prompt(
    topic: str,
    difficulty: str = "intermediate",
    focus: str = "mixed",
) -> str:
    return f"""
Generate ONE practice question for a learning session.

Topic: {topic}
Difficulty: {difficulty}
Focus: {focus}

The topic may belong to any academic, technical, professional,
scientific, or general-knowledge domain.

The question should test reasoning and understanding rather than
simple definition recall.

Possible question types include:

- conceptual reasoning
- application
- comparison
- mathematical reasoning
- implementation reasoning
- problem solving
- critical thinking
- factual understanding
- failure analysis

Adapt the question type to the subject.

Do not provide the answer.
Do not provide hints unless explicitly requested.

Ask exactly ONE question.
"""


def feedback_prompt(
    question: str,
    user_answer: str,
) -> str:
    return f"""
Evaluate my answer to the following AI/LLM question.

Question:
{question}

My answer:
{user_answer}

Return ONLY valid JSON.
Do not use markdown.
Do not add any text before or after the JSON.

Use exactly this structure:

{{
    "verdict": "Correct",
    "score": 0,
    "what_was_correct": "",
    "what_was_wrong": "",
    "missing_concept": "",
    "correct_reasoning": "",
    "interview_answer": "",
    "follow_up_question": ""
}}

Rules:

- verdict must be exactly one of:
  "Correct", "Partially Correct", "Incorrect"

- score must be an integer from 0 to 10.

- Evaluate the reasoning, not just whether keywords are present.

- Give credit for technically correct reasoning even if the wording
  differs from the expected explanation.

- Identify misconceptions explicitly.

- If the answer is incomplete, explain what is missing.

- "interview_answer" should be a concise, technically strong answer
  that the student could give in an interview.

- "follow_up_question" should test the weakest important part of the
  student's understanding.

Do not invent facts.
"""