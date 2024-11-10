from typing import Annotated
from contextlib import asynccontextmanager
from fastapi import FastAPI, Header, Query, Response, Request, HTTPException, Depends
from .src.db.sqlite import db, init_db
from .src.db.controller import TodoController
from .src.db.service import TodoService
from .src.db.models import TodoModel
from .src.generic.view import TodoView

todo_service = TodoService()
todo_controller = TodoController()
todo_model = TodoModel(todo_controller, todo_service)
todo_view = TodoView(todo_controller)

app = FastAPI()

@asynccontextmanager
async def lifespan(app: FastAPI):
    await db.connect()
    yield  
    await db.disconnect()

app.router.lifespan_context = lifespan

@app.middleware('http')
async def log(request: Request, call_next):
    print(f"GET {request.url}")
    return await call_next(request)



@app.get("/")
async def root(
        x: Annotated[int, Query()] = 1,
        y: Annotated[int, Query()] = 1,
        user_agent: Annotated[str | None, Header()] = None,
        login_request: Annotated[str | None, Header()] = None
    ):
    return {"msg": "Invalid Crediantials"}

@app.get("/todos")
async def get_todos(
    todo_controller=todo_controller
    ):
    try:
        init_db()
        todos = await todo_controller.model.todo_service.try_get_todos()
        return todo_controller.view.show_todos(todos)
    except Exception as e:
        todo_controller.update_view_with_error_message(str(e))
        raise HTTPException(status_code=500, detail="Error fetching todos")
