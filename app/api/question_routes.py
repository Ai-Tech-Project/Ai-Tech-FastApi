from fastapi import APIRouter
from app.schemas.question import Question
from app.services.question_service import QuestionService

router = APIRouter(prefix="/questions")  # Préfixe pour toutes les routes de questions

question_service = QuestionService()
# Route pour créer une question
@router.post("/add_question", summary="Create a question")
async def create_question(question: Question):
    return await question_service.create_question(question)

# Route pour obtenir toutes les questions
@router.get("/all_questions", summary="Get all questions")
async def get_questions():
    return question_service.get_all_questions()
