from dataclasses import dataclass, field

class BaseHeader():
    def __init__(self, **kwargs):
        self.__attrs__ = []

        for key, value in kwargs.items():
            self[key] = value

    def __repr__(self):
        return "".join([f" {key}={self[key]};" for key in self.__attrs__])
    
    def __getitem__(self, key):
        return self.__getattribute__(key)
    
    def __setitem__(self, key, value):
        self.__attrs__.append(key)
        self.__setattr__(key, value)



@dataclass
class Cookie(BaseHeader):
    """"Cookie header object"""

@dataclass
class ContentType(BaseHeader):
    """"content-type header object"""


@dataclass
class Headers:
    _attributes: dict = field(default_factory=lambda: {
        'User-Agent': 'my-app/0.0.1',
        'Cookie': "",
    })

    def __getitem__(self, key):
        return self._attributes[key]
    
    def __setitem__(self, key, value):
        # if key not in self._attributes:
        #     raise KeyError(f"UNDEFINED KEY: key not in {self._attributes.keys()}")
        self._attributes[key] = value

    def items(self):
        return self._attributes.items()
