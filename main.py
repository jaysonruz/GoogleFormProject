# from typing import Optional
from fastapi import FastAPI
from sheets import get_form_response

app = FastAPI()

@app.get("/get_response/{number}")
async def get_form_data(number):
    return get_form_response(number)


# uvicorn main:app --reload


