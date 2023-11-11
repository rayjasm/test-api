from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import json

app = FastAPI()

class req(BaseModel):
    image_path: str

@app.post('/')
def post_test(item: req):
    return {
    "success": "true",
    "message": "success",
    "estimated_data": {
    "class": 3,
    "confidence": 0.8683
    }
    }