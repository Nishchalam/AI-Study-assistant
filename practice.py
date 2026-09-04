class PracticeSession:
    """Manages the state of a practice session."""

    def __init__(
        self,
        topic,
        difficulty="intermediate",
        total_questions=5,
        focus="mixed",
    ):
        self.topic = topic
        self.difficulty = difficulty
        self.total_questions = total_questions
        self.focus = focus

        self.current_question_number = 0
        self.current_question = None

        self.questions = []
        self.answers = []
        self.evaluations = []

    def start(self):
        """Start the practice session."""

        self.current_question_number = 1

    def set_question(self, question):
        """Store the current question."""

        self.current_question = question
        self.questions.append(question)

    def submit_answer(self, answer):
        """Store the student's answer."""

        self.answers.append(answer)

    def add_evaluation(self, evaluation):
        """Store evaluation for the current question."""

        self.evaluations.append(evaluation)

    def has_more_questions(self):
        """Check whether more questions remain."""

        return self.current_question_number < self.total_questions

    def next_question(self):
        """Move to the next question."""

        if self.has_more_questions():
            self.current_question_number += 1
            self.current_question = None
            return True

        return False

    def get_progress(self):
        """Return current session progress."""

        return {
            "current_question": self.current_question_number,
            "total_questions": self.total_questions,
            "questions_answered": len(self.answers),
            "questions_evaluated": len(self.evaluations),
        }

    def is_complete(self):
        """Check whether the practice session is complete."""

        return (
            len(self.answers) >= self.total_questions
            and len(self.evaluations) >= self.total_questions
        )

    def get_results(self):
        """Return all practice session results."""

        return {
            "topic": self.topic,
            "difficulty": self.difficulty,
            "focus": self.focus,
            "total_questions": self.total_questions,
            "questions": self.questions,
            "answers": self.answers,
            "evaluations": self.evaluations,
        }
    
# if __name__ == "__main__":

#     session = PracticeSession(
#         topic="Transformers",
#         difficulty="intermediate",
#         total_questions=3,
#         focus="mixed",
#     )

#     session.start()

#     print("Topic:", session.topic)
#     print("Difficulty:", session.difficulty)
#     print("Questions:", session.total_questions)
#     print("Focus:", session.focus)

#     session.set_question(
#         "Why is self-attention useful in Transformers?"
#     )

#     print("\nQuestion:", session.current_question)

#     session.submit_answer(
#         "Self-attention allows the model to consider relationships "
#         "between different tokens."
#     )

#     session.add_evaluation(
#         {
#             "verdict": "Correct",
#             "score": 8,
#         }
#     )

#     print("\nProgress:")
#     print(session.get_progress())

#     print("\nMoving to next question...")
#     session.next_question()

#     print(session.get_progress())