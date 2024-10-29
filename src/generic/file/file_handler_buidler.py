from typing import Protocol, TypeVar
from abc import ABC, abstractmethod
from pathlib import Path



class Buildable(Protocol):
    def build(self):
        pass


class AbstracFileBuilder(ABC, Buildable):

    T = TypeVar('T')
    FILE_HANDLER_TYPE = TypeVar('FileHandler')
    FILE_BUILDER_TYPE = TypeVar('FileBuilder')
    
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
    def build(self) -> FILE_HANDLER_TYPE:
        raise NotImplementedError("")
    


    