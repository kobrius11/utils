from collections.abc import Awaitable
from typing import Protocol


from ..sqlite import db



class TodoServiceProt(Protocol):
    class Error(Exception):
        pass

    async def try_get_todos(self) -> Awaitable[list["Todo"]]:
        pass

    async def try_update_todo(self, todo: "Todo") -> None:
        pass


class TodoService(TodoServiceProt):
    class Error(Exception):
        pass

    async def try_get_todos(self) -> Awaitable[list["Todo"]]:
        from ..models import Todo
        query = "SELECT id, name, is_done FROM todos"
        rows = await db.fetch_all(query)
        return [Todo(**row) for row in rows]

    async def try_update_todo(self, todo: "Todo") -> None:
        query = "UPDATE todos SET is_done = :is_done WHERE id = :id"
        values = {"is_done": todo.is_done, "id": todo.id}

        result = await db.execute(query=query, values=values)
        if not result:
            raise self.Error("Failed to update Todo Status")