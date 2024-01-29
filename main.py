from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import schemas, models
from database import engine

app = FastAPI()

models.Base.metadata.create_all(engine)

templates = Jinja2Templates(directory='templates')

@app.get('/')
async def index(request: Request):
    return templates.TemplateResponse('index.html',  {'request': request, 'name': 'Wiktor'})