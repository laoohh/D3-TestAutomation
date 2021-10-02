"""This module contains the ConvertStringToUpperCase proxy action class."""
from src.testproject.classes import ProxyDescriptor
from src.testproject.sdk.addons import ActionProxy


class ConvertStringToUpperCase(ActionProxy):
    def __init__(self, inputString: str):
        super().__init__()
        self.proxydescriptor = ProxyDescriptor(
            guid="D5P7e9ZMO0aPwXNrWJE9iA",
            classname="ConvertStringToUpperCase"
        )
        self.inputString = inputString
        self.result = None
