from typing import Generic, TypeVar

TModel = TypeVar('TModel')
TView = TypeVar('TView')

class Controller(Generic[TModel, TView]):
    __model: TModel | None = None
    __view: TView | None = None

    @property
    def model(self) -> TModel | None:
        return self.__model 

    @model.setter
    def model(self, model: TModel) -> None:
        self.__model = model

    @property
    def view(self) -> TView | None:
        return self.__view
    
    @view.setter
    def view(self, view: TView) -> None:
        self.__view = view
