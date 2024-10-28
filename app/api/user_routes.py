from fastapi import APIRouter
from app.schemas.user import User
from app.services.user_service import UserService

router = APIRouter(prefix="/users")  # Préfixe pour toutes les routes d'utilisateurs
user_service = UserService()  # Instanciation du service utilisateur

@router.post("/add_user", summary="Create a user")
async def create_user(user: User):
    return await user_service.create_user(user)

@router.get("/all_users", summary="Get all users")
async def get_users():
    return await user_service.get_all_users()
