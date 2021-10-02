"""This module contains the CompareTwoStrings proxy action class."""
from src.testproject.classes import ProxyDescriptor
from src.testproject.sdk.addons import ActionProxy


class CompareTwoStrings(ActionProxy):
    def __init__(self, firstString: str, secondString: str, ignoreCase: bool, expectedResult: int):
        super().__init__()
        self.proxydescriptor = ProxyDescriptor(
            guid="D5P7e9ZMO0aPwXNrWJE9iA",
            classname="CompareTwoStrings"
        )
        self.firstString = firstString
        self.secondString = secondString
        self.ignoreCase = ignoreCase
        self.expectedResult = expectedResult
        self.result = None
