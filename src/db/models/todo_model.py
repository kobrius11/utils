from typing import Protocol
# from ..controller import TodoController
from ..service import TodoService
# from .todo import Todo


class TodoModelProt(Protocol):
    async def fetch_todos(self) -> None:
        pass

    async def toggle_todo(self, id) -> None:
        pass

class TodoModel(TodoModelProt):
    __todos: list["Todo"]

    def __init__(self, controller: "TodoController", todo_service: "TodoService"):
        self.__controller = controller
        controller.model = self
        self.__todo_service = todo_service
        self.__todos = []

    async def fetch_todos(self) -> None:
        try:
            self.__todos = await self.__todo_service.try_get_todos()
        except TodoService.Error as err:
            self.__controller.update_view_with_error_message(err.message)
        else:
            self.__controller.update_view_with_todos(self.__todos)

    async def toggle_todo(self, id) -> None:
        found_todos = [todo for todo in self.__todos if todo.id == id]
        todo = found_todos[0] if len(found_todos) else None

        if todo:
            todo.is_done = not todo.is_done

            try:
                await self.__todo_service.try_update_todo(todo)
            except TodoService.Error as err:
                self.__controller.update_view_with_error_message(err.message)