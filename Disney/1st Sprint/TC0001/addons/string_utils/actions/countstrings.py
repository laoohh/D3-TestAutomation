"""This module contains the CountStrings proxy action class."""
from src.testproject.classes import ProxyDescriptor
from src.testproject.sdk.addons import ActionProxy


class CountStrings(ActionProxy):
    def __init__(self, inputString: str, delimiter: str):
        super().__init__()
        self.proxydescriptor = ProxyDescriptor(
            guid="D5P7e9ZMO0aPwXNrWJE9iA",
            classname="CountStrings"
        )
        self.inputString = inputString
        self.delimiter = delimiter
        self.count = None
