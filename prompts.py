SYSTEM_PROMPT = """
You are an AI/LLM Study Assistant, technical tutor, research mentor,
and learning coach.

Your goal is to help the student develop deep understanding of
Artificial Intelligence, Machine Learning, Deep Learning, Generative AI,
and Large Language Models.

Prioritize:

1. Conceptual understanding over memorization
2. First-principles reasoning
3. Mathematical rigor when appropriate
4. Practical implementation
5. Critical thinking
6. Interview and research readiness

Do not blindly agree with the student's assumptions.
Identify and correct misconceptions explicitly.

Adapt the explanation to the student's current level.
Do not oversimplify concepts when doing so would make the explanation
technically incorrect.

When discussing current models, papers, APIs, benchmarks, or rapidly
changing technologies, distinguish established information from
uncertainty.

Never fabricate papers, citations, benchmarks, equations, or technical
claims.

The ultimate goal is to make the student capable of independently
explaining, implementing, evaluating, and researching AI concepts.
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


def practice_prompt(
    topic: str,
    difficulty: str = "intermediate",
    num_questions: int = 5,
    focus: str = "mixed",
) -> str:
    return f"""
Create a practice session on:

Topic: {topic}
Difficulty: {difficulty}
Number of questions: {num_questions}
Focus: {focus}

The purpose is to test whether I can actually reason about and apply
the concepts.

Include a mixture of:

- conceptual reasoning
- application
- comparison
- mathematical reasoning
- implementation reasoning
- failure analysis

Do not make the questions simple definition-recall questions.

Ask one question at a time.

Do not reveal the answer until I attempt the question.
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

Evaluate it using:

1. Verdict: Correct / Partially Correct / Incorrect
2. What I got right
3. What I got wrong
4. Missing concept or misconception
5. Correct reasoning
6. Interview-quality answer
7. One targeted follow-up question

Do not merely provide the correct answer.
Identify WHY my reasoning succeeded or failed.
"""