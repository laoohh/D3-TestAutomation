"""This module contains the ReplaceSubstringsWithRegex proxy action class."""
from src.testproject.classes import ProxyDescriptor
from src.testproject.sdk.addons import ActionProxy


class ReplaceSubstringsWithRegex(ActionProxy):
    def __init__(self, sourceString: str, regex: str, replacement: str):
        super().__init__()
        self.proxydescriptor = ProxyDescriptor(
            guid="D5P7e9ZMO0aPwXNrWJE9iA",
            classname="ReplaceSubstringsWithRegex"
        )
        self.sourceString = sourceString
        self.regex = regex
        self.replacement = replacement
        self.resultString = None
