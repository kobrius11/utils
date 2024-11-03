from typing import Annotated
from fastapi import FastAPI, Header, Query, Response, Request
from .src.db import DBControler

DBCONN = DBControler()

app = FastAPI()

@app.get("/")
async def root(
        x: Annotated[int, Query()] = 1,
        y: Annotated[int, Query()] = 1,
        user_agent: Annotated[str | None, Header()] = None,
        login_request: Annotated[str | None, Header()] = None
    ):
    return {"msg": "Invalid Crediantials"}


@app.get("/login")
async def root(
        username: Annotated[str | None, Header()] = None,
        password: Annotated[str | None, Header()] = None,
    ):
    db = DBCONN.connect_db("users")
    user_password = db.select("users", username).fetchone()[0]
    if user_password == password:
        return {"msg": f"Welcome Back! {username}"}
    
    return {"msg": "Invalid Crediantials"}

@app.middleware('http')
async def log(request: Request, call_next):
    print(f"GET {request.url}")
    return await call_next(request)