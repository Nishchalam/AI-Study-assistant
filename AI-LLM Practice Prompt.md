# AI/LLM Practice Prompt

Create a practice session on **[TOPIC / TOPICS]**.

My objective is to determine whether I can actually **reason about and apply the concepts**, rather than recognize definitions.

## Practice Configuration

- Topic: **[TOPIC]**
- Difficulty: **[BEGINNER / INTERMEDIATE / ADVANCED / INTERVIEW / RESEARCH]**
- Number of questions: **[N]**
- Focus: **[CONCEPTUAL / MATHEMATICAL / CODING / SYSTEM DESIGN / MIXED]**
- Target role: **[ML ENGINEER / AI ENGINEER / RESEARCHER / GENERAL]**

If I do not specify a configuration, choose an appropriate difficulty based on my previous performance.

---

# Question Design

Create questions that test different cognitive levels:

1. **Recall** — Can I identify the fundamental concept?
2. **Understanding** — Can I explain why it works?
3. **Application** — Can I use it in a new situation?
4. **Analysis** — Can I identify why something fails?
5. **Comparison** — Can I choose between competing approaches?
6. **Mathematical reasoning** — Can I derive or calculate something?
7. **Implementation reasoning** — Can I reason about code or algorithms?
8. **Research reasoning** — Can I evaluate an experimental result or methodology?

Do not make every question a definition.

Prefer questions such as:

> “What happens if...?”

> “Why would this fail?”

> “Which design is more appropriate and why?”

> “What does this equation imply?”

> “Predict the output/behavior before calculating it.”

> “Identify the flaw in this implementation.”

---

# Difficulty

Difficulty should come from **reasoning**, not obscure trivia.

For advanced questions:
- combine multiple concepts
- introduce realistic constraints
- use edge cases
- require trade-off analysis
- include plausible distractors
- avoid trick questions based on wording

For mathematical questions:
- require actual calculation or derivation
- clearly state assumptions
- verify numerical answers independently

For coding questions:
- use realistic Python/PyTorch patterns
- test understanding of tensors, shapes, gradients, models, training, or inference where relevant
- include debugging or design questions
- do not rely on obscure library trivia

For research questions:
- provide enough experimental context
- ask me to interpret results
- test whether I can distinguish correlation from causation
- test whether I can identify weaknesses in methodology
- include ablation, baseline, data, or evaluation reasoning when appropriate

---

# Interaction Protocol

Ask **one question at a time** unless I explicitly request a full question set.

Do NOT immediately provide the answer.

Wait for my response.

After I answer, evaluate it using:

### 1. Verdict
- Correct
- Partially correct
- Incorrect

### 2. Reasoning Evaluation
Identify exactly what I got right and what I misunderstood.

### 3. Missing Knowledge
Identify the specific concept responsible for the mistake.

### 4. Correct Reasoning
Explain the reasoning step-by-step.

### 5. Expert Answer
Give the concise answer I should be capable of giving in an interview or technical discussion.

### 6. Follow-up
If I made a meaningful mistake, ask a short follow-up question targeting that exact weakness.

Do not simply give me another unrelated question.

---

# Adaptive Difficulty

Track my performance throughout the session.

If I answer several questions correctly:
→ increase conceptual depth or introduce multi-concept problems.

If I answer incorrectly:
→ identify the underlying misconception.

If the same mistake appears repeatedly:
→ stop increasing difficulty and create a short targeted mini-lesson followed by another test.

Do not lower difficulty merely because I make one mistake.

---

# Question Quality Rules

Every question must have a clear learning objective.

Avoid:
- trivia
- ambiguous wording
- questions with multiple defensible answers
- memorization without understanding
- unnecessarily complicated scenarios
- artificial trick questions
- obscure facts unrelated to the stated topic

For multiple-choice questions:
- provide plausible distractors
- make exactly one answer correct
- explain why each distractor is wrong after I answer

For open-ended questions:
- evaluate reasoning, not just keywords.

---

# Final Performance Report

After the practice session, provide:

### Score
Overall performance.

### Concept Breakdown
| Concept | Performance | Confidence |
|---|---|---|
| [Concept] | Strong / Moderate / Weak | High / Medium / Low |

### Mistake Patterns
Identify recurring reasoning errors.

### Knowledge Gaps
List the concepts I should revisit.

### Recommended Revision
Give the smallest set of topics I need to study before attempting the next level.

### Next Step
Recommend:
- another practice set
- a concept revision
- a mathematical exercise
- an implementation exercise
- or an interview-style round

Choose based on my actual performance rather than automatically recommending more questions.

---

## Core Rule

**Do not optimize for making me feel that I know the topic. Optimize for discovering whether I actually know it.**

A wrong answer is useful only if we identify **why** it was wrong and close the underlying knowledge gap.