# Concept Learning Prompt

Teach me **[CONCEPT / TOPIC]**.

My goal is not just to memorize the definition. I want to understand the concept well enough to **explain it, derive it, implement it, apply it, and answer interview/research questions about it**.

Structure the explanation in the following order:

### 1. Prerequisites
List the minimum concepts I should already understand. If an important prerequisite is missing, explain it briefly before proceeding.

### 2. Problem & Motivation
- What problem does this concept solve?
- Why was it introduced?
- What limitations of earlier approaches motivated it?

### 3. Intuition
Build a simple mental model first.
Use a concrete analogy or example only if it genuinely improves understanding.

### 4. Formal Definition
Give the precise technical definition and terminology.

### 5. How It Works
Explain the mechanism step-by-step.
Trace what happens to the input through the system where applicable.

### 6. Mathematics
Give the important equations and derive them where useful.
For every important equation, explain:
- what each variable means
- why the equation has that form
- what the equation means intuitively
- how changing its terms affects the system

Do not hide important mathematics merely to make the explanation simpler.

### 7. Worked Example
Take a small concrete example and work through it step-by-step.

### 8. Implementation
Show a minimal implementation when applicable.
Prefer Python/PyTorch for deep-learning concepts.

Separate:
- educational implementation
- practical/production implementation

Explain the important implementation decisions.

### 9. Comparison
Compare the concept with the most relevant alternatives or closely related concepts.
Focus on **why** they differ, not merely what they are.

### 10. Limitations & Failure Modes
Explain:
- assumptions
- weaknesses
- computational costs
- failure cases
- situations where the method should not be used

### 11. Common Misconceptions
Identify mistakes that a student or interview candidate is likely to make.

### 12. AI/LLM Relevance
Explain how this concept appears in modern AI/LLM systems and why it matters.

### 13. Interview Perspective
Give:
- 3 basic interview questions
- 3 conceptual questions
- 2 deeper technical questions

Do not provide the answers yet unless I ask.

### 14. Research Perspective
Explain:
- important research directions
- unresolved limitations
- useful papers or seminal work where relevant
- what would constitute a meaningful improvement

Clearly distinguish established findings from hypotheses or current research.

### 15. Knowledge Check
Finish with 3–5 questions that test whether I actually understood the concept.

Do not make these pure definition-recall questions. Prefer questions requiring prediction, reasoning, comparison, or application.

---

## Teaching Rules

- Do not blindly agree with my assumptions.
- Explicitly identify misconceptions.
- Prefer first-principles explanations.
- Do not introduce advanced concepts unnecessarily.
- Do not oversimplify something if the simplification becomes technically wrong.
- Define unfamiliar terminology.
- Distinguish intuition from formal technical claims.
- Use examples only when they illuminate the mechanism.
- Never fabricate papers, results, benchmarks, equations, or citations.
- If information is uncertain or time-sensitive, say so and verify it when possible.
- Adjust the depth according to my apparent level.
- If I appear to understand the topic already, skip basic material and go deeper.
- If I appear confused because of a prerequisite gap, stop and fix that gap first.

The final goal is **independent technical understanding**, not completion of an explanation.