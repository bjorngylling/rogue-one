import lib.libtcodpy as libtcod

from map_generation import BaseGenerator
from rogue_one.geometry import Rect


class RandomRoomGenerator(BaseGenerator):
    """This class will generate a random room (square or rectangle for now)
    inside the provided bounds on the provided map"""

    def __init__(self, seed, width_variation=5, height_variation=4):
        super(RandomRoomGenerator, self).__init__(seed)
        self.width_variation = width_variation
        self.height_variation = height_variation

    def run(self, map, bounds=None):
        if bounds is None:
            bounds = Rect((1, 1), len(map) - 1, len(map[0]) - 1)

        random = libtcod.random_get_int(self.seed, 0, self.width_variation)
        room = Rect((bounds.x1 + random, bounds.y1 + random),
                    0, 0)
        room.setSecondPos(((bounds.x2 - random, bounds.y2 - random)))

        self.carve_room(map, room)

    def carve_room(self, map, room):
        for x in range(room.x1, room.x2 - 2):
            for y in range(room.y1, room.y2 - 2):
                map[x][y] = 0
