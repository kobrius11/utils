from typing import Any


class classproperty(property):
    def __get__(self, instance: Any, owner: type | None = None) -> Any:
        return classmethod(self.fget).__get__(None, owner)()