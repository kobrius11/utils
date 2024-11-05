from typing import Protocol
from .controller import Controller
from ...generic.view import TodoView
# from ..models import Todo, TodoModel


class TodoControllerProt(Protocol):
    async def start_fetch_todos(self) -> None:
        pass

    async def toggle_todo(self, id) -> None:
        pass

    def update_view_with_todos(self, todos: list["Todo"]):
        pass

    def update_view_with_error_message(self, error_message: str) -> None:
        pass

class TodoController(Controller["TodoModel", "TodoView"], TodoControllerProt):
    async def start_fetch_todos(self) -> None:
        if self.model is not None:
            await self.model.fetch_todos()

    async def toggle_todo(self, id: int) -> None:
        if self.model is not None:
            await self.model.toggle_todo_done(id)

    def update_view_with_todos(self, todos: list["Todo"]):
        if self.view is not None:
            self.view.show_todos(todos)

    def update_view_with_error_message(self, error_message: str) -> None:
        if self.view is not None:
            self.view.show_error_message(error_message)


