import lib.libtcodpy as libtcod

from ecs import System
import component


class HandleInput(System):
    def component_mask(self):
        return {component.Player, component.Movement, component.FieldOfView}

    def process_components(self, components):
        key = libtcod.console_wait_for_keypress(True)

        if key.vk == libtcod.KEY_ESCAPE:
            exit()

        velocity = self.handle_movement(key)
        components[component.Movement].dx = velocity[0]
        components[component.Movement].dy = velocity[1]

        if (velocity[0] != 0 or velocity[1] != 0):
            components[component.FieldOfView].recompute = True

    def handle_movement(self, key):
        velocity = (0, 0)
        if libtcod.console_is_key_pressed(libtcod.KEY_UP):
            velocity = (0, -1)

        elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN):
            velocity = (0, 1)

        elif libtcod.console_is_key_pressed(libtcod.KEY_LEFT):
            velocity = (-1, 0)

        elif libtcod.console_is_key_pressed(libtcod.KEY_RIGHT):
            velocity = (1, 0)

        return velocity


class UpdateFOV(System):
    def component_mask(self):
        return {component.FieldOfView, component.Position}

    def process_components(self, components):
        fov = components[component.FieldOfView]
        pos = components[component.Position]

        if fov.recompute:
            fov.recompute = False
            libtcod.map_compute_fov(fov.fov_map, pos.x, pos.y,
                                    fov.view_distance, fov.light_walls,
                                    fov.algorithm)


class WorldRenderer(System):
    def __init__(self, priority, console):
        super(WorldRenderer, self).__init__(priority)
        self._con = console

    def component_mask(self):
        return {component.Renderable, component.Position}

    def process_components(self, components):
        # Since we handle our own updating (see WorldRenderer#update) we do
        # nothing here.
        pass

    def update(self, world):
        self.prepare_rendering()

        # Draw the world
        player = world.get_entity({component.Player}).components
        fov_map = player[component.FieldOfView].fov_map
        world.map.draw(fov_map)

        # Draw all objects
        for entity in world.entities:
            if self.component_mask <= entity.component_mask:
                self.draw_entity({k: entity.components[k]
                                  for k in self.component_mask()}, fov_map)

    def draw_entity(self, components, fov_map):
        pos = components[component.Position]
        in_fov = libtcod.map_is_in_fov(fov_map, pos.x, pos.y)

        if in_fov:
            print "drawing entity: %s" % (components)
            render = components[component.Renderable]
            libtcod.console_set_char_background(
                self._con, pos.x, pos.y, render.bk_color, libtcod.BKGND_SET)
            libtcod.console_set_default_foreground(self._con, render.fg_color)

            if (render.char is not None):
                libtcod.console_put_char(
                     self._con, pos.x, pos.y, render.char, libtcod.BKGND_NONE)

    def prepare_rendering(self):
        libtcod.console_clear(self._con)
