import secrets
from string import ascii_letters, punctuation, digits


class Salt():

    def __init__(self, k) -> None:
        self.__k = k
        self.__salt = None

    @classmethod
    def create_salt(cls, k):
        return cls(k)._get_salt().__str__()
    
    def _get_salt(self):
        chars = ascii_letters + digits + punctuation.replace("'", '').replace('"', '')
        self.__salt = [secrets.choice(chars) for _ in range(self.__k)]
        return self
    
    def __str__(self) -> str:
        return ''.join(self.__salt)