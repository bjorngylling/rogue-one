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


class Renderer(System):

    def __init__(self, priority, console):
        super(Renderer, self).__init__(priority)
        self._con = console

    def component_mask(self):
        return {component.Renderable, component.Position}

    def update(self, world):
        # We override the parent update since we are going to need the world
        # to be able to access the map-data.

        self.prepare_rendering()

    def prepare_rendering(self):
        libtcod.console_clear(self._con)
