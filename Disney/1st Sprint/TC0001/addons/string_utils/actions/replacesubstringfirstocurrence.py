"""This module contains the ReplaceSubstringFirstOcurrence proxy action class."""
from src.testproject.classes import ProxyDescriptor
from src.testproject.sdk.addons import ActionProxy


class ReplaceSubstringFirstOcurrence(ActionProxy):
    def __init__(self, sourceString: str, regex: str, replacement: str):
        super().__init__()
        self.proxydescriptor = ProxyDescriptor(
            guid="D5P7e9ZMO0aPwXNrWJE9iA",
            classname="ReplaceSubstringFirstOcurrence"
        )
        self.sourceString = sourceString
        self.regex = regex
        self.replacement = replacement
        self.resultString = None
