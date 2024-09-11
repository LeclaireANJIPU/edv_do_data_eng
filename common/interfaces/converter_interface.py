from abc import ABC, abstractmethod


class ConverterInterface(ABC):
    @abstractmethod
    def convert(self, data):
        pass
