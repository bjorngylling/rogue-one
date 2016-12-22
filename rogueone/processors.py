import esper

from rogueone import components


class RenderProcessor(esper.Processor):
    def __init__(self, renderer):
        super().__init__()
        self.renderer = renderer

    def process(self):
        self.renderer.clear()

        for ent, (rend, pos) in self.world.get_components(
                components.Renderable, components.Position):
            self.renderer.draw_str(pos.x, pos.y, rend.character)
