import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)

class Config:
    db_url = os.getenv('DATABASE_URL', 'postgresql://postgres:postgres@localhost:5432/mealwise_db')
    if db_url.startswith("postgresql://"):
        db_url = db_url.replace("postgresql://", "postgresql+psycopg://", 1)
    SQLALCHEMY_DATABASE_URI = db_url
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'mealwise-secret-key-2024')
    JSON_AS_ASCII = False  # Hỗ trợ tiếng Việt trong JSON response
