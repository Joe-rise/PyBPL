from bpl.renderer.base import Renderer


class TextRenderer(Renderer):
    def __init__(self):
        Renderer.__init__(self, 'text')

    def render(self, program):
        #TODO: implement text renderer based on parameters and ditribution(s) in program object
        pass
