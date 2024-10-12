# auth_service.py
from database import Databse

class AuthService:
    def __init__(self):
        self.db = Database()

    def authenticate(self, username, password):
        """Authenticate user by username and password"""
        user = self.db.get_user(username)
        if not user:
            return False
        return user['password'] == password
