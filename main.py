#imports
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import webbrowser

app = FastAPI()

URLS = [
    "https://github.com/6GVisible",
    "https://rahti.csc.fi/",
    "https://chat.openai.com/",
    "https://docs.google.com/spreadsheets/d/1gx7nYJmS03RO3jSOVx6hOyyBleIatrK6f4_Be6Qm_z8/edit",
    "https://interval-timer-app-git-main-vishakabs-projects.vercel.app/",
    "https://www.overleaf.com/project",
    "https://github.com/6GVisible",
    "github-desktop://",
    "vscode://",
]

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <h1>Morning Launcher</h1>
    <button onclick="fetch('/start', {method:'POST'})">
        Start Work
    </button>
    """

@app.post("/start")
def start_work():
    for url in URLS:
        webbrowser.open_new_tab(url)
    return {"ok": True}