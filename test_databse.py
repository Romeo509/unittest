# test_database.py
import unittest
from database import Database

class TestDatabase(unittest.TesCase):
    def setUp(self):
        self.db = Database()

    def test_get_user_success(self):
        user = self.db.get_user('alice')
        self.assertIsNotNone(user)
        self.assertEqual(user['password'], 'password123')
    
    def test_get_user_not_found(self):
        user = self.db.get_user('nonexistent_user')
        self.assertIsNone(user)

if __name__ == '__main__':
    unittest.main()