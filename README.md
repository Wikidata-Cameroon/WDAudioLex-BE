# WikiData Audio Lex Tool Backend

### Overview

The WDAudioLEx-BE Tool Backend is a backend system built using Flask, providing functionality to support login authentication via the MediaWiki API. This project is structured to facilitate modular development and deployment, using best practices in Python development, Flask frameworks, and integration with third-party APIs for secure login.
Features

    Flask-based Backend: Lightweight, scalable, and easy to extend.
    Secure Authentication: Implements MediaWiki's API for robust login mechanisms using action=login and action=clientlogin.
    Virtual Environment Integration: Manage dependencies effectively to ensure a consistent development experience.
    Modular Architecture: Organized project structure for easy navigation and updates.

### Project Structure

```
WDAudioLEx-BE/
├── app/
│   ├── __init__.py        # Flask app factory
│   ├── routes.py          # Route definitions
│   ├── forms.py           # Flask-WTF forms
│   ├── static/            # Static files (CSS, JS, images)
│   └── templates/         # HTML templates for rendering views
├── clientlogin.py         # MediaWiki API integration for authentication
├── requirements.txt       # List of dependencies
├── config.py              # Configuration settings
├── run.py                 # Main application entry point
└── README.md              # Project documentation
```

### Installation

#### 1. Prerequisites

    Python Version: Flask supports Python 3.9 and newer. Ensure you have Python installed.
    Flask Dependencies:
        Werkzeug: Implements WSGI.
        Jinja: Template rendering engine.
        MarkupSafe: Ensures template safety.
        ItsDangerous: Protects session cookies.
        Click: For command-line functionality.
        Blinker (Optional): Enables signal handling in Flask.

#### 2. Setup

```bash
# Step 1: Clone the Repository
git clone https://github.com/your-repo/WDAudioLEx-BE.git
cd WDAudioLEx-BE
# Step 2: Create a Virtual Environment
python3 -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
# Step 3: Install Dependencies
pip install -r requirements.txt
# Step 4: Run the Applicatiozn
python run.py
```

Access the application at http://127.0.0.1:5000.
Login Authentication with MediaWiki API

The project integrates MediaWiki's login system for user authentication. Two methods are supported:
Method 1: Using action=login

Steps:

    Fetch a login token using action=query&meta=tokens.
    Submit the login request using the lgtoken, username, and password.

Sample Code:

```bash
response = S.post(
    url="https://your-wiki-site/api.php",
    data={
        "action": "login",
        "lgname": "your_username",
        "lgpassword": "your_password",
        "lgtoken": "your_login_token",
        "format": "json"
    }
)
```

Method 2: Using action=clientlogin

This method is suited for interactive applications. It follows these steps:

    Fetch login fields using action=query&meta=authmanagerinfo.
    Obtain a login token.
    Submit the clientlogin request with the necessary fields.

Sample Code:

```bash
response = S.post(
    url="https://your-wiki-site/api.php",
    data={
        "action": "clientlogin",
        "username": "your_username",
        "password": "your_password",
        "loginreturnurl": "http://127.0.0.1:5000/",
        "logintoken": "your_login_token",
        "format": "json"
    }
)
```

### Configuration

The application configuration is managed in config.py. Update the following settings as per your environment:

```python
class Config:
    SECRET_KEY = "your_secret_key"
    FLASK_ENV = "development"
    DEBUG = True
```

### Templates

The HTML templates are located in the app/templates/ directory and styled using Bootstrap for responsive design.

Example Template (Login Form):

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Login</title>
    <link rel="stylesheet" href="static/bootstrap/css/bootstrap.min.css">
</head>
<body>
<div class="container">
    <h2>MediaWiki Log In</h2>
    <form method="post">
        <div class="form-group">
            <label for="username">Username</label>
            <input type="text" name="username" class="form-control" id="username" required>
        </div>
        <div class="form-group">
            <label for="password">Password</label>
            <input type="password" name="password" class="form-control" id="password" required>
        </div>
        <button type="submit" class="btn btn-primary">Log In</button>
    </form>
</div>
</body>
</html>
```


### Testing

The application uses Flask's built-in test client for unit testing.

Example Test:
```python
def test_login_page():
    response = app.test_client().get('/')
    assert response.status_code == 200
```
Run tests with:
```bash
pytest
```

### SQLAlchemy API Project Setup Guide

## 📋 Project Overview
This documentation provides a comprehensive guide to setting up a robust SQLAlchemy API project with best practices for database management, API development, and project structure.

## 🛠 Prerequisites
- Python 3.8+
- pip (Python package manager)
- Virtual environment tool (venv recommended)

## 🔧 Project Setup

### 1. Environment Preparation

#### Create Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 2. Dependencies Installation

#### Create Requirements File
Create `requirements.txt` with the following dependencies:
```
SQLAlchemy==2.0.19
FastAPI==0.103.1
Pydantic==2.3.0
psycopg2-binary==2.9.7
python-dotenv==1.0.0
alembic==1.11.3
uvicorn==0.23.2
```

#### Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Project Structure
```
project_root/
│
├── app/
│   ├── __init__.py
│   ├── database.py       # Database configuration
│   ├── models.py         # SQLAlchemy models
│   ├── schemas.py        # Pydantic schemas
│   └── crud.py           # CRUD operations
│
├── migrations/           # Alembic migrations
├── main.py               # Main application file
├── requirements.txt
├── .env
└── README.md
```

### 4. Database Configuration

#### Environment Variables (`.env`)
```
DATABASE_URL=postgresql://username:password@localhost/dbname
SECRET_KEY=your_secret_key
```

#### Database Connection (`app/database.py`)
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Database URL
DATABASE_URL = os.getenv("DATABASE_URL")

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

### 5. Database Migrations with Alembic

#### Initialize Alembic
```bash
alembic init migrations
```

#### Configuration
Edit `alembic.ini` and `migrations/env.py` to point to your models and database:

```python
# In migrations/env.py
from app.database import Base
from app.models import *  # Import all models
target_metadata = Base.metadata
```

#### Create and Apply Migrations
```bash
# Generate migration
alembic revision --autogenerate -m "Initial migration"

# Apply migration
alembic upgrade head
```

## 🚀 Running the Application

### Development Server
```bash
uvicorn main:app --reload
```

## 📦 Key Components

### Models (`app/models.py`)
```python
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from .database import Base
from datetime import datetime

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    created_at = Column(DateTime, default=datetime.utcnow)
```

### Schemas (`app/schemas.py`)
```python
from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    email: EmailStr

class User(UserCreate):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
```

### CRUD Operations (`app/crud.py`)
```python
from sqlalchemy.orm import Session
from . import models, schemas

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
```

## 🔒 Best Practices

1. **Environment Management**
   - Use `.env` for sensitive configuration
   - Never commit sensitive information to version control

2. **Database**
   - Use migrations for schema changes
   - Implement proper indexing
   - Use connection pooling

3. **Security**
   - Implement authentication
   - Use HTTPS
   - Validate and sanitize inputs

4. **Performance**
   - Use database indexing
   - Implement caching
   - Use efficient query patterns

## 🛠 Troubleshooting

### Common Issues
- Database connection failures
- Migration conflicts
- Dependency version mismatches

### Debugging Steps
1. Check `.env` configuration
2. Verify database accessibility
3. Ensure all dependencies are installed
4. Check Alembic migration history

## 📝 Notes
- Customize models according to your specific requirements
- Implement proper error handling
- Add logging for better observability

## 🤝 Contributing
1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request
