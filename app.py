from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Load variables
# SECRET_KEY = os.getenv('SECRET_KEY')
# SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
# OAUTH_MWURI = os.getenv('OAUTH_MWURI')
# OAUTH_EDIT_URI = os.getenv('OAUTH_EDIT_URI')
# CONSUMER_KEY = os.getenv('CONSUMER_KEY')
# CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')

SECRET_KEY = os.getenv('SECRET_KEY')
if not SECRET_KEY:
    raise ValueError("Missing environment variable: SECRET_KEY")

SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
if not SQLALCHEMY_DATABASE_URI:
    raise ValueError("Missing environment variable: SQLALCHEMY_DATABASE_URI")

OAUTH_MWURI = os.getenv('OAUTH_MWURI')
if not OAUTH_MWURI:
    raise ValueError("Missing environment variable: OAUTH_MWURI")

OAUTH_EDIT_URI = os.getenv('OAUTH_EDIT_URI')
if not OAUTH_EDIT_URI:
    raise ValueError("Missing environment variable: OAUTH_EDIT_URI")

CONSUMER_KEY = os.getenv('CONSUMER_KEY')
if not CONSUMER_KEY:
    raise ValueError("Missing environment variable: CONSUMER_KEY")

CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
if not CONSUMER_SECRET:
    raise ValueError("Missing environment variable: CONSUMER_SECRET")


# Debugging output
print("SECRET_KEY:", SECRET_KEY)
print("SQLALCHEMY_DATABASE_URI:", SQLALCHEMY_DATABASE_URI)
print("OAUTH_MWURI:", OAUTH_MWURI)
print("OAUTH_EDIT_URI:", OAUTH_EDIT_URI)
print("CONSUMER_KEY:", CONSUMER_KEY)
print("CONSUMER_SECRET:", CONSUMER_SECRET)
