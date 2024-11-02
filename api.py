from typing import Annotated
from fastapi import FastAPI, Header, Query

AUTHENTICATED_USER = "25f9e794323b453885f5181f1b624d0b"

app = FastAPI()

@app.get("/")
async def root(
        x: Annotated[int, Query()] = 1,
        y: Annotated[int, Query()] = 1,
        user_agent: Annotated[str | None, Header()] = None,
        login_request: Annotated[str | None, Header()] = None
    ):
    if login_request == AUTHENTICATED_USER:
        return {"msg": "welcome, User!"}
    
    return {"msg": "Invalid Crediantials"}