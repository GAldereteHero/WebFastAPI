from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory=".\public\static"), name="static")

templates = Jinja2Templates(directory="./public/templates")

@app.get('/', response_class=HTMLResponse)
def index():
    htmlAdress = ".\public\static\html\index.html"
    return FileResponse(htmlAdress, status_code=200)

@app.get('/dashboard', response_class=HTMLResponse)
def index(request:Request):
    return templates.TemplateResponse("list.html",{"request":request,"name":'Adrian'})