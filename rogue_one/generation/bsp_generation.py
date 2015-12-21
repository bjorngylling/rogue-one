import lib.libtcodpy as libtcod

from rogue_one.geometry import Rect

from map_generation import BaseGenerator


class BSPGenerator(BaseGenerator):
    """This generator uses BSP-trees to generate a map with rooms and corridors
    """

    def __init__(self, seed, number_of_iterations=4):
        super(BSPGenerator, self).__init__(seed)
        self.number_of_iterations = number_of_iterations

    def run(self, map):
        area = Rect(0, 0, len(map) - 1, len(map[0]) - 1)

        tree = self.generate_bsp_tree(self.number_of_iterations, area)

        self.generate_rooms(tree, map)

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

    def generate_rooms(self, tree, map):
        return


class BSPTreeNode(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def get_leaf_nodes(node):
    """Returns a list containing all leaf nodes in the tree.
    """
    result = []

    def traveller(node):
        if (node.left is None and node.right is None):
            result.add(node.data)

    traverse_tree_depth_first(node, traveller)

    return result


def traverse_tree_depth_first(node, traveller):
    """This function traverses all nodes under the supplied node, calling the
    provided traveller for each individual node. Stops if the traverser returns
    False or if there are no further nodes.
    """
    if traveller(node):
        if node.left is not None:
            traverse_tree_depth_first(node.left, traveller)
        if node.right is not None:
            traverse_tree_depth_first(node.right, traveller)
