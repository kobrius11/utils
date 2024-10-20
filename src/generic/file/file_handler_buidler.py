from typing import Protocol, TypeVar
from abc import ABC, abstractmethod
from pathlib import Path
from file_handler import FileHandler

T = TypeVar('T')
FILE_HANDLER_TYPE = TypeVar('FileHandler')
FILE_BUILDER_TYPE = TypeVar('FileBuilder')


class Buildable(Protocol):
    def build(self):
        pass


class AbstracFileBuilder(ABC, Buildable):
    
    @abstractmethod
    def set_path(self, path: Path) -> FILE_BUILDER_TYPE:
        raise NotImplementedError("")
    
    @abstractmethod
    def set_filename(self, filename: str) -> FILE_BUILDER_TYPE:
        raise NotImplementedError("")
    
    @abstractmethod
    def set_extension(self, extension: str) -> FILE_BUILDER_TYPE:
        raise NotImplementedError("")
    
    @abstractmethod
    def set_content(self, content: T) -> FILE_BUILDER_TYPE:
        raise NotImplementedError("")
    
    @abstractmethod
    def set_encoding(self, encoding: str) -> FILE_BUILDER_TYPE:
        raise NotImplementedError("")
    
    @abstractmethod
    def set_newline(self, newline: str) -> FILE_BUILDER_TYPE:
        raise NotImplementedError("")

    @abstractmethod 
    def build(self) -> FileHandler:
        raise NotImplementedError("")
    

class FileHandlerBuilder(AbstracFileBuilder):
    def __init__(self) -> None:
        self.__path = Path('./output')
        self.__filename = 'output'
        self.__extension = ''
        self.__content = ''
        self.__encoding = None
        self.__newline = None
        
    def set_path(self, path: Path) -> FILE_BUILDER_TYPE:
        self.__path = path
        return self
    
    def set_filename(self, filename: str) -> FILE_BUILDER_TYPE:
        self.__filename = filename
        return self
    
    def set_extension(self, extension: str) -> FILE_BUILDER_TYPE:
        self.__extension = extension
        return self
    
    def set_content(self, content: T) -> FILE_BUILDER_TYPE:
        self.__content = content
        return self
    
    def set_encoding(self, encoding: str) -> FILE_BUILDER_TYPE:
        self.__encoding = encoding
        return self
    
    def set_newline(self, newline: str) -> FILE_BUILDER_TYPE:
        self.__newline = newline
        return self

    def build(self) -> FileHandler:
        return FileHandler(
            self.__path,
            self.__filename,
            self.__extension,
            self.__content,
            self.__encoding,
            self.__newline
        )
    