import tdl
import esper

from rogueone import components, processors


class RogueOneApp(tdl.event.App):
    def __init__(self, renderer):
        super().__init__()
        self.renderer = renderer
        self.setup_world()

    def setup_world(self):
        self.world = esper.World()
        player = self.world.create_entity(
            components.Position(1, 1),
            components.Renderable("@"))
        self.world.add_processor(processors.RenderProcessor(self.renderer))

    def ev_QUIT(self, ev):
        raise SystemExit('The window has been closed.')

    def key_ESCAPE(self, ev):
        raise SystemExit('The window has been closed.')

    def update(self, dt):
        self.world.process()
        tdl.flush()
