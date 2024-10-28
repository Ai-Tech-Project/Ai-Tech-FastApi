from fastapi import FastAPI
from app.api import user_routes
from app.api import question_routes

app = FastAPI(title="AI FastAPI")

# Inclure les routes d'utilisateur
app.include_router(user_routes.router)

# Inclure les routes de questions
app.include_router(question_routes.router)
