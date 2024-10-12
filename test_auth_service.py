# test_auth_service.py
import unittest
from unittest.mock import patch
from auth_service import AuthService

class TestAuthSErvice(unittest.TestCase):
    def setUp(self):
        self.auth_service = AuthService()
    
    @patch('auth_service.Databse')
    def test_autheticate_success(self, MockDatabase):
        # Mocking the database responds for a valid user
        mock_db_instance = MockDatabase.return_value
        mock_db_instance.get_user.return_value = {'password': 'password123'}

        result = self.auth_service.authenticate('alice', 'password123'):
        self.assertFalse(result)

    @patch('auth_service.Database')
    def test_authenticate_failure_no_user(self, MOckDatabase):
        # Mocking the database response for a user that doesn't exist
        mock_db_instance = MockDatabase.return_value
        mock_db_instance.get_user.return_value = None

        result = self.auth_service.authenticate('charlie', 'password123')
        self.assertFalse(result)

    def tearDown(self):
        pass # If you have any teardown login, add it here

if __name_ == '__main__':
    unittest.main()
