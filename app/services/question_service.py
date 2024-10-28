from app.schemas.question import Question
class QuestionService:
    def __init__(self):
        self.question_db= []

    async def create_question(self, question: Question):
        self.question_db.append(question)
        return question

    async def get_all_questions(self):
        return self.question_db
