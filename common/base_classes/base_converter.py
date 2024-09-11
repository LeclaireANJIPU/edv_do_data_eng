from common.interfaces.converter_interface import ConverterInterface


class BaseConverter(ConverterInterface):
    def convert(self, data):
        raise NotImplementedError("Convert method must be implemented by subclasses")
