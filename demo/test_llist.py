from llist import LinkedList
import pytest


@pytest.fixture
def llist():
    return LinkedList()


class TestAsList(object):
    def test_1(self, llist):
        llist.add_node(5)
        assert llist.as_list() == [5]


class TestAdd(object):
    def test_1(self, llist):
        llist.add_node(1)
        assert llist.as_list() == [1]

    def test_2(self, llist):
        llist.add_node(1)
        llist.add_node(2)
        assert llist.as_list() == [1, 2]


class TestSearch(object):
    def test_1(self, llist):
        llist.add_node(1)
        llist.add_node(2)
        llist.add_node(3)
        assert llist.search(4) == -1

    def test_2(self, llist):
        llist.add_node(1)
        llist.add_node(2)
        llist.add_node(3)
        assert llist.search(1) == 0


class TestRemove(object):
    def test_1(self, llist):
        llist.add_node(1)
        llist.add_node(2)
        llist.remove_node(1)
        assert llist.as_list() == [1]

    def test_2(self, llist):
        llist.remove_node(0)
        assert llist.as_list() == []
