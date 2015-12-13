import lib.libtcodpy as libtcod

from MapGeneration import BaseGenerator
from ..Geometry import Rect


class BSPGenerator(BaseGenerator):
    """This generator uses BSP-trees to generate a map with rooms and corridors
    """

    def __init__(self, seed, number_of_iterations=4):
        super(BSPGenerator, self).__init__(seed)
        self.number_of_iterations = number_of_iterations

    def run(self, map):
        area = Rect(0, 0, len(map) - 1, len(map[0]) - 1)

        tree = self.generate_bsp_tree(self.number_of_iterations, area)

        return tree

    def generate_bsp_tree(self, iteration, area):
        if iteration > 0:
            split_vertically = area.w > area.h
            ratio = libtcod.random_get_float(self.seed, 0.4, 0.6)
            if split_vertically:
                # Vertical
                a = Rect(area.x1,
                         area.y1,
                         int(area.w * ratio),
                         area.h)
                b = Rect(area.x1 + a.w,
                         area.y1,
                         area.w - a.w,
                         area.h)
            else:
                # Horizontal
                a = Rect(area.x1,
                         area.y1,
                         area.w,
                         int(area.h * ratio))
                b = Rect(area.x1,
                         area.y1 + a.h,
                         area.w,
                         area.h - a.h)

            return BSPTreeNode(area,
                               self.generate_bsp_tree(iteration - 1, a),
                               self.generate_bsp_tree(iteration - 1, b))
        else:
            return BSPTreeNode(area)


class BSPTreeNode(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
