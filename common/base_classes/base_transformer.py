from common.interfaces.transformer_interface import TransformerInterface


class BaseTransformer(TransformerInterface):
    def transform(self, data):
        raise NotImplementedError("Transform method must be implemented by subclasses")
