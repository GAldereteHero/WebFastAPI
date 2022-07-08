from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse

app = FastAPI()

@app.get('/', response_class=HTMLResponse)
def index():
    htmlAdress = ".\public\pages\index.html"
    return FileResponse(htmlAdress, status_code=200)