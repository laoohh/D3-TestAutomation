"""This module contains the ExtractStringUsingRegex proxy action class."""
from src.testproject.classes import ProxyDescriptor
from src.testproject.sdk.addons import ActionProxy


class ExtractStringUsingRegex(ActionProxy):
    def __init__(self, regex: str, input: str):
        super().__init__()
        self.proxydescriptor = ProxyDescriptor(
            guid="D5P7e9ZMO0aPwXNrWJE9iA",
            classname="ExtractStringUsingRegex"
        )
        self.output = None
        self.regex = regex
        self.input = input
