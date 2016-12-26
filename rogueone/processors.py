import esper

from rogueone import components


class MovementProcessor(esper.Processor):
    def __init__(self):
        super().__init__()

    def process(self):
        for ent, (vel, pos) in self.world.get_components(components.Velocity,
                                                         components.Position):
            if (vel.dx, vel.dy) != (0, 0):
                pos.x += vel.dx
                pos.y += vel.dy
                vel.dx = 0
                vel.dy = 0


class CollisionProcessor(esper.Processor):
    def __init__(self, player: int, map_sections):
        super().__init__()
        self.player = player
        self.map_sections = map_sections

    def process(self):
        # Only handle collisions on the same map section as the player
        player_pos = self.world.component_for_entity(self.player,
                                                     components.Position)
        for ent, (pos, col) in self.components(player_pos.map_section):
            pass

    def components(self, map_section: int):
        comps = self.world.get_components(components.Position,
                                          components.Collision)
        return [(ent, (pos, col)) for ent, (pos, col) in comps
                if pos.map_section == map_section]


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
        self.render_map(self.map_sections[player_pos.map_section])

        for ent, (rend, pos) in self.world.get_components(
                components.Renderable, components.Position):
            self.renderer.draw_char(pos.x, pos.y,
                                    rend.character,
                                    rend.color, None)

    def render_map(self, map_section):
        for x, y in map_section:
            self.renderer.draw_char(x, y,
                                    map_section.char_for_pos(x, y),
                                    *map_section.color_for_pos(x, y))
