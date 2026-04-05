import sys
import os

# Cấu hình đường dẫn root của Python để import backend
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'backend'))

from app import create_app

# Biến `app` này sẽ được Vercel tự động import làm Serverless Function
app = create_app()
