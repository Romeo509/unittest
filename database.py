# databse.py
class Databse:
    def __init__(self):
        self.users = {
            'alice': {'password': 'password123'},
            'bob': {'password': 'bobpassword'},
        }

    def get_user(self, username):
        """Fetch user details by username from the database."""
        return self.users.get(username)
    