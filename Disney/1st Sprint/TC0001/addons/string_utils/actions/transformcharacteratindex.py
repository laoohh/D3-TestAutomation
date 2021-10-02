"""This module contains the TransformCharacterAtIndex proxy action class."""
from src.testproject.classes import ProxyDescriptor
from src.testproject.sdk.addons import ActionProxy


class TransformCharacterAtIndex(ActionProxy):
    def __init__(self, input: str, lowerOrUpperCase: str, index: str):
        super().__init__()
        self.proxydescriptor = ProxyDescriptor(
            guid="D5P7e9ZMO0aPwXNrWJE9iA",
            classname="TransformCharacterAtIndex"
        )
        self.input = input
        self.lowerOrUpperCase = lowerOrUpperCase
        self.index = index
        self.output = None
