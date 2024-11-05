from typing import Protocol

from fastapi import HTTPException
from fastapi.responses import JSONResponse

# from ...db.models import Todo
# from ...db.controller import TodoController


class TodoViewProt(Protocol):
    def show_todos(self, todos: list["Todo"]):
        pass

    def show_error_message(self, error_message: str) -> None:
        pass


class TodoView(TodoViewProt):
    def __init__(self, controller: "TodoController") -> None:
        self.__controller = controller
        controller.view = self
        controller.start_fetch_todos()
    
    def show_todos(self, todos: list["Todo"]):
        # Update view to show given todos
        if todos:
            todos_data = [{
                "id": todo.id,
                "name": todo.name,
                "is_done": todo.is_done,
            } for todo in todos]
            return JSONResponse(content=todos_data, status_code=200)
        else:
            return JSONResponse(content={"message": "No todos available."}, status_code=200)
        
    def show_error_message(self, error_message: str) -> None:
        raise HTTPException(status_code=400, detail=error_message)
