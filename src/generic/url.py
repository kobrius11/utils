from functools import cache
import socket
from urllib.parse import urlparse
from typing import Generic, TypeVar, Final
from optional import Optional
from abc import abstractmethod
from dataclasses import dataclass
from .metaclass import PrivateConstructor

T = TypeVar("T")

class AbststractValidatedValue(Generic[T]):
    def __init__(self, value) -> None:
        self._value: Final = value
    
    @abstractmethod
    def is_valid(self) -> bool:
        pass

    def get(self) -> Optional:
        return (
            Optional.of(self._value)
            if self.is_valid()
            else Optional.empty()
        )
    
    class GetError(Exception):
        pass

    def try_get(self) -> T:
        if self.is_valid():
            return self._value
        else:
            raise self.GetError('Invalid ' + self.__class__.__name__)


class HttpSchema(AbststractValidatedValue[str]):
    @cache
    def is_valid(self) -> bool:
        lowercase_value = self._value.lower()
        return lowercase_value == 'http' or lowercase_value == 'https' 


class Port(AbststractValidatedValue[int]):
    @cache
    def is_valid(self):
        return 1 <= self._value <= 65535


class HttpHost(AbststractValidatedValue[str]):
    @cache
    def is_valid(self):
        try:
            self._ip_address = socket.gethostbyname(self._value)
            return True
        except socket.error:
            return False 

class HttpPath(AbststractValidatedValue[str]):
    @cache
    def is_valid(self):
        return True

class HttpQuery(AbststractValidatedValue[str]):
    @cache
    def is_valid(self):
        return True

@dataclass
class UrlParams:
    schema: str = ""
    host: str = ""
    port: int = 443
    path: str = ""
    query: str = ""

class HttpUrl(metaclass=PrivateConstructor):
    def __init__(
            self,
            schema: str,
            host: str,
            port: int,
            path: str,
            query: str
        ) -> None:
        self.__schema = schema
        self.__port = port
        self.__host = host
        self.__path = path
        self.__query = query

    class CreateError(Exception):
        pass

    @classmethod
    def create_url(cls, url_params: UrlParams) -> "HttpUrl | None":
        # validate args here return None if invalid
        return cls._create(
            schema=HttpSchema(url_params.schema).get(),
            host=HttpHost(url_params.host).get(),
            port=Port(url_params.port).get(),
            path=HttpPath(url_params.path).get(),
            query=HttpQuery(url_params.query).get()
        )
    
    @classmethod
    def try_create_url(cls, url_params: UrlParams) -> "HttpUrl":
        # validate args here raise error if invalid
        try:
            return cls._create(
                schema=HttpSchema(url_params.schema).try_get(),
                host=HttpHost(url_params.host).try_get(),
                port=Port(url_params.port).try_get(),
                path=HttpPath(url_params.path).try_get(),
                query=HttpQuery(url_params.query).try_get()
            )
        except AbststractValidatedValue.GetError as error:
            raise cls.CreateError(error)
    
    def __str__(self):
        return f"{self.__schema}://{self.__host}:{self.__port}/{self.__path}?{self.__query}"