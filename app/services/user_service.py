from app.schemas.user import User

class UserService:
    def __init__(self):
        self.users_db = []  # Simulations de la base de données

    async def create_user(self, user: User):
        self.users_db.append(user)
        return user

    async def get_all_users(self):
        return self.users_db
