# app/models/question_model.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Question(BaseModel):
    id: Optional[str] = None  # ID optionnel pour la question
    question_text: str
    answer_text: Optional[str] = None
    created_at: datetime = datetime.utcnow()
