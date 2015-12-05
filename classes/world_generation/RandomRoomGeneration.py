from ..Rect import Rect
from ..World import Tile
import libtcodpy as libtcod


class RandomRoomGeneration:

    def carve_square(self, x, y, map):
        map[x][y].blocked = False
        map[x][y].block_sight = False
        map[x][y].char = "."
        map[x][y].fg_color = libtcod.Color(43, 35, 2)

    def carve_room(self, room, map):
        for x in range(room.x1 + 1, room.x2):
            for y in range(room.y1 + 1, room.y2):
                self.carve_square(x, y, map)

    def make_map(self, map):
        map.fill_map(Tile("#", libtcod.Color(43, 22, 2), True))

        room1 = Rect(20, 15, 10, 15)
        room2 = Rect(50, 15, 10, 15)
        self.carve_room(room1, map.map)
        self.carve_room(room2, map.map)

        def listener(x, y):
            self.carve_square(x, y, map.map)
            return True
        libtcod.line(30, 18, 50, 18, listener)

        return map
