from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
    name: str

items = []

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API"}

# TODO: Implementar endpoints para /items