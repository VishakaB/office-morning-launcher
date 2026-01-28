@echo off
set "ROOT=%~dp0"
set "PY=%ROOT%.venv\Scripts\python.exe"

if not exist "%PY%" (
  echo Virtualenv not found at: %PY%
  echo Create it with: python -m venv .venv
  pause
  exit /b 1
)

REM Install deps once (safe to run every time; it will be quick if already installed)
"%PY%" -m pip install -q --upgrade pip
"%PY%" -m pip install -q fastapi "uvicorn[standard]"

REM Start server
start "" http://127.0.0.1:8000
"%PY%" -m uvicorn main:app --host 127.0.0.1 --port 8000
