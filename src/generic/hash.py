from typing import Protocol, Union
from enum import Enum
from hashlib import md5, sha512, sha256


class hashable(Protocol):
    def hash(self):
        pass

class md5Hash(hashable):
    def __init__(self):
        self.__hashed_value = None

    @classmethod
    def hash(cls, content):
        return cls()._get_hash(content)
    
    def _get_hash(self, content: Union[str, bytes]):
        self.__hashed_value = md5(content.encode())
        return self

    def __str__(self) -> str:
        return self.__hashed_value.hexdigest()

class sha512Hash(hashable):
    def __init__(self):
        self.__hashed_value = None

    @classmethod
    def hash(cls, content: Union[str, bytes]):
        self = cls().__hashed_value = sha512(content.encode())
        return self
    
    def __str__(self) -> str:
        return self.__hashed_value.hexdigest()

class sha256Hash(hashable):
    def __init__(self):
        self.__hashed_value = None

    @classmethod
    def hash(cls, content: Union[str, bytes]):
        self = cls().__hashed_value = sha256(content.encode())
        return self
    
    def __str__(self) -> str:
        return self.__hashed_value.hexdigest()


class HashEnum(Enum):
    MD5=1
    SHA512=2
    SHA256=3

class HashFactory():
    @staticmethod
    def create_hash(hash_type: HashEnum, content: Union[str, bytes]):
        match hash_type:
            case HashEnum.MD5:
                return md5Hash.hash(content)
            case HashEnum.SHA512:
                return sha512Hash.hash(content)
            case HashEnum.SHA256:
                return sha256Hash.hash(content)
            case _:
                return Exception("hash type not recognized, types in [MD5, SHA512, SHA256]")