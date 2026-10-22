from abc import ABC, abstractmethod
from typing import Callable, Sequence, Any

class NumericalMethod(ABC):
    def __init__(self, name: str):
        self.__name = name
     
    @property   
    def name(self):
        return self.__name

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}: {self.__name}>"
    
    
class Regressor(NumericalMethod):
    def __init__(self, name:str):
        super().__init__(name)
        self._coeff = None   
    
    @abstractmethod
    def fit(self, x: Sequence[float], y: Sequence[float]) -> None:
        pass
    
    @abstractmethod
    def predict(self, x: Sequence[float]) -> Any:
        pass
if __name__ == "__main__":
    pass