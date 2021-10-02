"""This module contains the ReplaceSubstrings proxy action class."""
from src.testproject.classes import ProxyDescriptor
from src.testproject.sdk.addons import ActionProxy


class ReplaceSubstrings(ActionProxy):
    def __init__(self, inputString: str, target: str, replacement: str):
        super().__init__()
        self.proxydescriptor = ProxyDescriptor(
            guid="D5P7e9ZMO0aPwXNrWJE9iA",
            classname="ReplaceSubstrings"
        )
        self.inputString = inputString
        self.target = target
        self.replacement = replacement
        self.result = None
