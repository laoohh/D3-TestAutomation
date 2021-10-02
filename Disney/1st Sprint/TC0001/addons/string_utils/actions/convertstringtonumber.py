"""This module contains the ConvertStringToNumber proxy action class."""
from src.testproject.classes import ProxyDescriptor
from src.testproject.sdk.addons import ActionProxy


class ConvertStringToNumber(ActionProxy):
    def __init__(self, input: str):
        super().__init__()
        self.proxydescriptor = ProxyDescriptor(
            guid="D5P7e9ZMO0aPwXNrWJE9iA",
            classname="ConvertStringToNumber"
        )
        self.input = input
        self.output = None
