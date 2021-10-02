"""This module contains the ConcatenateTwoStrings proxy action class."""
from src.testproject.classes import ProxyDescriptor
from src.testproject.sdk.addons import ActionProxy


class ConcatenateTwoStrings(ActionProxy):
    def __init__(self, firstString: str, secondString: str):
        super().__init__()
        self.proxydescriptor = ProxyDescriptor(
            guid="D5P7e9ZMO0aPwXNrWJE9iA",
            classname="ConcatenateTwoStrings"
        )
        self.firstString = firstString
        self.secondString = secondString
        self.result = None
