from abc import ABC, abstractmethod

class NumericalMethod(ABC):
    def __init__(self, name: str):
        self._name = name
     
    @property   
    def name(self):
        return self._name


if __name__ == "__main__":
    pass