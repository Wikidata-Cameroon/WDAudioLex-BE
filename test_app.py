import os
import unittest
from dotenv import load_dotenv

class TestEnvVariables(unittest.TestCase):
    
    def test_env_variables(self):
        load_dotenv()
        self.assertEqual(os.getenv('SECRET_KEY'), 'supersecretkey')
        self.assertEqual(os.getenv('SQLALCHEMY_DATABASE_URI'), 'sqlite:///example.db')
        self.assertEqual(os.getenv('OAUTH_MWURI'), 'https://auth.example.com')
        self.assertEqual(os.getenv('OAUTH_EDIT_URI'), 'https://edit.example.com')
        self.assertEqual(os.getenv('CONSUMER_KEY'), 'examplekey')
        self.assertEqual(os.getenv('CONSUMER_SECRET'), 'examplesecret')

if __name__ == '__main__':
    unittest.main()
