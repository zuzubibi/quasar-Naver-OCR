import requests
import uuid
import time
import json

from fastapi import FastAPI
from models import Images
from ocr import post_general_ocr
from ocr import post_template_ocr
from ocr import save_file
from ocr import get_text
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    # "http://localhost:8080",  # mohaet local
    # "http://localhost:3000",
    # "http://localhost:5050",
    # "http://localhost",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/SendPhoto")
async def post(data: Images):
    # response = await post_general_ocr(data=data)
    response = post_template_ocr(data=data, template_id="28780")
    final = get_text(response)
    return final
