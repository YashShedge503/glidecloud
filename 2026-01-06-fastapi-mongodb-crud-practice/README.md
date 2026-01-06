# FastAPI + MongoDB Minimal Setup

# Create virtual environment
python -m venv venv

# Activate venv 
venv/Scripts/activate 

# Upgrade pip
python -m pip install
--upgrade pip

# Install required packages
pip install fastapi uvicorn motor python-dotenv pydantic

# Create folders
mkdir -p app/routes

# Create files
touch app/main.py app/database.py app/schemas.py app/routes/user_routes.py

touch .env .gitignore requirements.txt README.md

# Create .gitignore
venv/
__pycache__/
.env
EOF


## Tech
- FastAPI
- Uvicorn
- MongoDB (Motor)
- Python 3.10+

## Run

uvicorn app.main:app --reload


## Docs
- http://127.0.0.1:8000/docs

Author: Yash Shedge

echo "Minimal setup completed"
