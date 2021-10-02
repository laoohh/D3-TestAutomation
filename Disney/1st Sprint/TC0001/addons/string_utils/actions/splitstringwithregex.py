"""This module contains the SplitStringWithRegex proxy action class."""
from src.testproject.classes import ProxyDescriptor
from src.testproject.sdk.addons import ActionProxy


class SplitStringWithRegex(ActionProxy):
    def __init__(self, sourceString: str, regex: str, limit: int, indexOfElement: str):
        super().__init__()
        self.proxydescriptor = ProxyDescriptor(
            guid="D5P7e9ZMO0aPwXNrWJE9iA",
            classname="SplitStringWithRegex"
        )
        self.sourceString = sourceString
        self.regex = regex
        self.limit = limit
        self.indexOfElement = indexOfElement
        self.result = None
        self.valueOfElement = None
        self.numberOfElements = None
