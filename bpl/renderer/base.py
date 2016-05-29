class Renderer(object):
    def __init__(self, dtype=None):
        self.dtype = dtype

    def render(self, program):
        raise NotImplementedError("render method should be implemented by subclass")
