from common.interfaces.extractor_interface import ExtractorInterface


class BaseExtractor(ExtractorInterface):
    def extract(self):
        raise NotImplementedError("Extract method must be implemented by subclasses")
