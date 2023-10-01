from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from data.database import get_users


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/hello")
def read_root():
    response = {}
    users = []
    for user in get_users():
        users.append({
            'id': user[0],
            'nombre': user[1],
            'email': user[2],
            'telefono': user[3]
        })
    response["usuarios"] = users
    return response

