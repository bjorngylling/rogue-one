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
        self.check_for_collisions(self.components(player_pos.map_section),
                                  self.map_sections[player_pos.map_section])

    def check_for_collisions(self, all_components, map_section):
        for ent, (pos, col, vel) in all_components:
            # Check for collisions on the map_section
            if (not map_section.walkable[pos.x + vel.dx, pos.y + vel.dy]):
                vel.dx = 0
                vel.dy = 0
                continue

            # Check for collisions against other entities
            for other_ent, (other_pos, other_col, other_vel) in all_components:
                if (ent == other_ent):
                    # We don't want to check against ourselves, that would be
                    # very silly!
                    continue
                if (pos.x + vel.dx == other_pos.x + other_vel.dx and
                        pos.y + vel.dy == other_pos.y + other_vel.dy):
                    self.solve_collision(ent, vel, other_ent, other_vel)

    def solve_collision(self, ent, vel, other_ent, other_vel):
        if ((vel.dx, vel.dy) != (0, 0)):
            vel.dx, vel.dy = (0, 0)
        elif ((other_vel.dx, other_vel.dy) != (0, 0)):
            other_vel.dx, other_vel.dy = (0, 0)

    def components(self, map_section: int):
        comps = self.world.get_components(components.Position,
                                          components.Collision,
                                          components.Velocity)
        return [(ent, (pos, col, vel)) for ent, (pos, col, vel) in comps
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
