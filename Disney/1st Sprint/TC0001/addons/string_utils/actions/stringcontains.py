"""This module contains the StringContains proxy action class."""
from src.testproject.classes import ProxyDescriptor
from src.testproject.sdk.addons import ActionProxy


class StringContains(ActionProxy):
    def __init__(self, inputString: str, substring: str, caseSensitive: bool, expectedResult: str = "true"):
        super().__init__()
        self.proxydescriptor = ProxyDescriptor(
            guid="D5P7e9ZMO0aPwXNrWJE9iA",
            classname="StringContains"
        )
        self.inputString = inputString
        self.substring = substring
        self.caseSensitive = caseSensitive
        self.expectedResult = expectedResult
        self.result = None
