import esper

from rogueone import components


class RenderProcessor(esper.Processor):
    def __init__(self, renderer, player, map_sections):
        super().__init__()
        self.renderer = renderer
        self.player = player
        self.map_sections = map_sections

    def process(self):
        self.renderer.clear()

        player_pos = self.world.component_for_entity(self.player,
                                                     components.Position)
        self.render_map(self.map_sections[player_pos.map])

        for ent, (rend, pos) in self.world.get_components(
                components.Renderable, components.Position):
            self.renderer.draw_str(pos.x, pos.y, rend.character)

    def render_map(self, map_section):
        for x, y in map_section:
            if map_section.walkable[x, y]:
                self.renderer.draw_str(x, y, '.')
