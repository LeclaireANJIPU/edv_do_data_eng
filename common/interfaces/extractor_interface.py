from abc import ABC, abstractmethod


class ExtractorInterface(ABC):
    @abstractmethod
    def extract(self):
        pass
