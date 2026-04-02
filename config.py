import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'WDAudioLex')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # oauth 
    CONSUMER_KEY = "ef9f619cfa02d15596b61b72ad35ecd4"
    CONSUMER_SECRET = "e18d71307b49e5235294332ed327563311fd59e2"

    OAUTH_MWURI =  "https://meta.wikimedia.org/w/index.php"