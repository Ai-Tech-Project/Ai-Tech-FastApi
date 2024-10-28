# app/models/user_model.py
from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: Optional[str] = None  # ID optionnel pour l'utilisateur
    username: str
    email: str
    password: str


