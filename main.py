from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db import session
from models import CEO


app = FastAPI()

origins = [
    "http://localhosst", 
     "http://localhosst:3000"

]
app.add_middleware(
    CORSMiddleware, 
    allow_origins=origins, 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get('/')
def home():
    return {'message': "hello world"}

@app.get('/ceos')
def get_ceos():
    ceos = session.query(CEO)
    return ceos.all()

@app.post('/create')
async def create_ceo(name: str, slug: str, year: int):
    new_ceo = CEO(name=name, slug=slug, year=year)
    session.add(new_ceo)
    session.commit()
    return{"CEO Added": new_ceo.name}

@app.get('/ceos/{slug}')
def get_single_ceo(slug: str):
    ceo = session.query(CEO).filter(CEO.slug == slug)
    return ceo.all()
