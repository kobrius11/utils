from abc import abstractmethod, ABC
import requests

class AbstractRequest(ABC):
    @abstractmethod
    def send_get(self):
        raise NotImplementedError("")
    
    @abstractmethod
    def send_post(self):
        raise NotImplementedError("")
    
class Request(AbstractRequest):

    