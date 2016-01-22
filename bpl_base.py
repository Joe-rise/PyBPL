import numpy as np


class BPLBase(object):
    """
    BPL base class.
    """

    def __init__(self, cpd):
        """
        :param cpd:
         A CPD instance (from cpd.py).
        :return:
        """
        self.cpd = cpd

    def generate_type(self, _type):
        raise NotImplementedError("Subclass should implement generate_type")

    def generate_token(self):
        raise NotImplementedError("Subclass should implement generate_token")
