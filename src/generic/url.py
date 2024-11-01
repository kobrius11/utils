from dataclasses import dataclass
from .metaclass import PrivateConstructor


@dataclass
class UrlParams:
    host: str
    schema: str = 'https'
    port: int = 443
    path: str = ""
    query: str = ""


class Url(metaclass=PrivateConstructor):
    def __init__(self, schema: str, port: int, host: str, path: str, query: str) -> None:
        self.__schema = schema
        self.__port = port
        self.__host = host
        self.__path = path
        self.__query = query

    @classmethod
    def create_url(cls, url_params: UrlParams) -> "Url | None":
        # validate args here return None if invalid
        return cls._create(url_params.schema, url_params.port, url_params.host, url_params.path, url_params.query)
    
    @classmethod
    def try_create_url(cls, url_params: UrlParams) -> "Url":
        # validate args here raise error if invalid
        return cls._create(url_params.schema, url_params.port, url_params.host, url_params.path, url_params.query)
    
    def __str__(self):
        return "".join(self.__schema, self.__host, self.__path, self.__query)