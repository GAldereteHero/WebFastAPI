import re
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/', response_class=HTMLResponse)
def index():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>FastAPI</title>
    </head>
    <body>
        <h1>Mi primer aplicacion con FastAPI</h1>
        <br>
        <h2>Probando como podemos inscrustar contenido con HTML</h2>
    </body>
    </html>
    '''