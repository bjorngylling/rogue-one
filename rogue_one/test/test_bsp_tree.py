import unittest
from rogue_one.generation import bsp_generation
from rogue_one.generation.bsp_generation import BSPTreeNode


class BSPTreeTestCase(unittest.TestCase):
    def test_get_leaf_nodes(self):
        self.assertEquals(
            bsp_generation.get_leaf_nodes(self.tree), [2, 4, 5])

    def setUp(self):
        """ Create a tree such as:
            0
           / \
          1   3
         /   / \
        2   4   5
        """
        self.tree = BSPTreeNode(0,
                                BSPTreeNode(1,
                                            BSPTreeNode(2)),
                                BSPTreeNode(3,
                                            BSPTreeNode(4),
                                            BSPTreeNode(5)))
