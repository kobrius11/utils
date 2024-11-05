class Todo():
    def __init__(self, id: int, name: str, is_done: bool) -> None:
        self.__id = id
        self.__name = name
        self.__is_done = is_done

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def is_done(self):
        return self.__is_done

    @is_done.setter
    def is_done(self, value):
        self.is_done = value
