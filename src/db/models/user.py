from typing import Protocol

class UserModelProt(Protocol):
    async def fetch_user(self) -> None:
        pass

    async def set_active_user(self, id) -> None:
        pass


class UserModel(UserModelProt):
    pass