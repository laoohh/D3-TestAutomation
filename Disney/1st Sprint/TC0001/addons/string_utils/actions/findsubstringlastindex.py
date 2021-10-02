"""This module contains the FindSubstringLastIndex proxy action class."""
from src.testproject.classes import ProxyDescriptor
from src.testproject.sdk.addons import ActionProxy


class FindSubstringLastIndex(ActionProxy):
    def __init__(self, sourceString: str, substring: str):
        super().__init__()
        self.proxydescriptor = ProxyDescriptor(
            guid="D5P7e9ZMO0aPwXNrWJE9iA",
            classname="FindSubstringLastIndex"
        )
        self.sourceString = sourceString
        self.substring = substring
        self.index = None
