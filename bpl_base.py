import numpy as np


class BPLBase(object):
    """
    BPL base class.
    """

    def __init__(self):
        pass

    def generate_type(self, _type):
        raise NotImplementedError("Subclass should implement generate_type")

    def generate_symbol(self):
        raise NotImplementedError("Subclass should implement generate_type")
