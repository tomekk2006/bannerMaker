@echo off
if not exist venv\Scripts\python.exe (
	echo Installing virtual environment...
    python -m venv venv
	echo Installing dependencies...
    venv\Scripts\pip install -r requirements.txt
	echo Running main script
	echo
)
venv\Scripts\python main.py

