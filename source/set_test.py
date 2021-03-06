#!python

from set import Set
import unittest


class HashSetTest(unittest.TestCase):

    def test_init(self):
        set = Set(['A','B','C'])
        assert len(set) == 3
        assert set.contains('A') is True
        assert set.contains('B') is True
        assert set.contains('C') is True

    def test_add_remove(self):
        set = Set()
        set.add('A')
        assert len(set) == 1
        assert set.contains('A') is True
        set.add('B')
        assert len(set) == 2
        assert set.contains('B') is True
        set.add('C')
        assert len(set) == 3
        assert set.contains('C') is True
        set.remove('B')
        assert len(set) == 2
        assert set.contains('B') is False
        set.remove('A')
        assert len(set) == 1
        assert set.contains('A') is False
        set.remove('C')
        assert len(set) == 0
        assert set.contains('C') is False
        with self.assertRaises(ValueError):
            set.remove('C')

    def test_union(self):
        set1 = Set(['A', 'B'])
        set2 = Set(['B', 'C'])
        new_union = set1.union(set2).items()
        assert ['A', 'B', 'C'] <= new_union

    def test_intersection(self):
        set1 = Set(['A', 'B'])
        set2 = Set(['B', 'C'])
        new_intersection = set1.intersection(set2)
        assert len(new_intersection) == 1
        assert ['B'] == new_intersection

    def test_difference(self):
        set1 = Set(['A', 'B'])
        set2 = Set(['B', 'C'])
        new_difference = set1.difference(set2)
        assert len(new_difference) == 1
        assert ['A'] == new_difference

    def test_difference(self):
        set1 = Set(['A', 'B'])
        set2 = Set(['B', 'C'])
        assert set1.is_subset(set2) is False
        set2.add('A')
        assert set1.is_subset(set2) is True




if __name__ == '__main__':
    unittest.main()
