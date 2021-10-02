"""This module contains the TrimString proxy action class."""
from src.testproject.classes import ProxyDescriptor
from src.testproject.sdk.addons import ActionProxy


class TrimString(ActionProxy):
    def __init__(self, sourceString: str):
        super().__init__()
        self.proxydescriptor = ProxyDescriptor(
            guid="D5P7e9ZMO0aPwXNrWJE9iA",
            classname="TrimString"
        )
        self.sourceString = sourceString
        self.resultString = None
