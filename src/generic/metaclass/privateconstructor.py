
from typing import Any, TypeVar

T = TypeVar('T')

class PrivateConstructor(type):
    def __call__(cls: T, *args: Any, **kwargs: Any):
        raise TypeError('Consstructor is private')

    def _create(cls: T, *args: Any, **kwargs: Any) -> T:
        return super().__call__(*args, **kwargs)
