import numpy as np


class Program(object):
    """
    Subclass Program to create a specific type, e.g. MotorProgram.
    """
    def __init__(self,
                 image_width=30,
                 image_height=30,
                 params={}):
        self.image = np.matrix(np.empty([image_height, image_width]))
        self.params = params
