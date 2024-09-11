from common.interfaces.validator_interface import ValidatorInterface


class BaseValidator(ValidatorInterface):
    def validate(self, data):
        raise NotImplementedError("Validate method must be implemented by subclasses")
