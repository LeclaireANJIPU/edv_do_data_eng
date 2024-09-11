from common.interfaces.loader_interface import LoaderInterface


class BaseLoader(LoaderInterface):
    def load(self, data):
        raise NotImplementedError("Load method must be implemented by subclasses")
