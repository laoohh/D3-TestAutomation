"""This module contains the StringStartsWith proxy action class."""
from src.testproject.classes import ProxyDescriptor
from src.testproject.sdk.addons import ActionProxy


class StringStartsWith(ActionProxy):
    def __init__(self, sourceString: str, prefix: str, offset: int, expectedResult: bool):
        super().__init__()
        self.proxydescriptor = ProxyDescriptor(
            guid="D5P7e9ZMO0aPwXNrWJE9iA",
            classname="StringStartsWith"
        )
        self.sourceString = sourceString
        self.prefix = prefix
        self.offset = offset
        self.expectedResult = expectedResult
        self.result = None
