"""This module contains the InsertStringInIndex proxy action class."""
from src.testproject.classes import ProxyDescriptor
from src.testproject.sdk.addons import ActionProxy


class InsertStringInIndex(ActionProxy):
    def __init__(self, inputString: str, index: int, stringToInsert: str):
        super().__init__()
        self.proxydescriptor = ProxyDescriptor(
            guid="D5P7e9ZMO0aPwXNrWJE9iA",
            classname="InsertStringInIndex"
        )
        self.inputString = inputString
        self.index = index
        self.stringToInsert = stringToInsert
        self.convertedString = None
