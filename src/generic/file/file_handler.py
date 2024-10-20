from typing import Protocol
from abc import ABC, abstractmethod


class Writable(Protocol):
    def write(self):
       pass

class Readable(Protocol):
    def read(self):
        pass

class AbstractFileHandler(ABC, Readable, Writable):
    
    @abstractmethod
    def get_filename(self):
        raise NotImplementedError("")
    
    @abstractmethod
    def get_content(self):
        raise NotImplementedError("")

    @abstractmethod
    def get_path(self):
        raise NotImplementedError("")
    
    @abstractmethod
    def get_encoding(self):
        raise NotImplementedError("")
    
    @abstractmethod
    def get_extension(self):
        raise NotImplementedError("")
    
    @abstractmethod
    def get_newline(self):
        raise NotImplementedError("")
    
    @abstractmethod
    def get_full_filename(self):
        raise NotImplementedError("")
    
    @abstractmethod
    def get_full_path(self):
        raise NotImplementedError("")
    

class FileHandler(AbstractFileHandler):
    def __init__(
        self,
        path,
        filename,
        extension,
        content,
        encoding,
        newline
    ):
        self.__path = path
        self.__filename = filename
        self.__extension = extension
        self.__content = content
        self.__encoding = encoding
        self.__newline = newline

    def write(self):
        with open(
            file=self.get_full_path(),
            mode='w',
            encoding=self.get_encoding(),
            newline=self.__newline
        ) as f:
            f.write(self.get_content())
        return self

    def read(self):
        with open(
            file=self.get_full_path(),
            mode='w',
            encoding=self.get_encoding(),
            newline=self.__newline
        ) as f:
            self.__content = f.read()
        return self

    def get_filename(self):
        return self.__filename
    
    def get_content(self):
        return self.__content

    def get_path(self):
        return self.__path
    
    def get_encoding(self):
        return self.__encoding
    
    def get_extension(self):
        return self.__extension
    
    def get_newline(self):
        return self.__newline

    def get_full_filename(self):
        return self.get_filename() + '.' + self.get_extension()
    
    def get_full_path(self):
        return (self.get_path() / self.get_full_filename()).absolute()


if __name__ == '__main__':
    pass