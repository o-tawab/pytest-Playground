from bst import BST
import pytest


# All of the following satisfies statement and branch coverage criteria.
@pytest.fixture
def bst():
    return BST()


class TestFind:
    def test_1(self, bst):
        bst.insert(3)
        bst.insert(5)
        bst.insert(1)
        bst.insert(7)
        bst.insert(9)
        bst.insert(5)
        bst.insert(20)
        bst.insert(11)
        node = bst.find(bst.root, 9)
        assert node.value == 9

    def test_2(self, bst):
        bst.insert(3)
        bst.insert(5)
        bst.insert(1)
        bst.insert(7)
        bst.insert(9)
        bst.insert(5)
        bst.insert(20)
        bst.insert(11)
        assert bst.find(bst.root, 222) is None

    def test_3(self, bst):
        assert bst.find(bst.root, 5) is None