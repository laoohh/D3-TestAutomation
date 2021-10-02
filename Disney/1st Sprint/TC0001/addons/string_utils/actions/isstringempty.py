"""This module contains the IsStringEmpty proxy action class."""
from src.testproject.classes import ProxyDescriptor
from src.testproject.sdk.addons import ActionProxy


class IsStringEmpty(ActionProxy):
    def __init__(self, string: str, expectedResult: bool):
        super().__init__()
        self.proxydescriptor = ProxyDescriptor(
            guid="D5P7e9ZMO0aPwXNrWJE9iA",
            classname="IsStringEmpty"
        )
        self.string = string
        self.expectedResult = expectedResult
        self.result = None
