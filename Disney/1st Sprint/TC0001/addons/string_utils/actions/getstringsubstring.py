"""This module contains the GetStringSubstring proxy action class."""
from src.testproject.classes import ProxyDescriptor
from src.testproject.sdk.addons import ActionProxy


class GetStringSubstring(ActionProxy):
    def __init__(self, beginIndex: int, endIndex: int, inputString: str):
        super().__init__()
        self.proxydescriptor = ProxyDescriptor(
            guid="D5P7e9ZMO0aPwXNrWJE9iA",
            classname="GetStringSubstring"
        )
        self.beginIndex = beginIndex
        self.endIndex = endIndex
        self.inputString = inputString
        self.result = None
