from customLib import CustomLib as lib
import unittest
bloc_test = [lib.Bloc(10, 12, 32),  lib.Bloc(32, 10, 12), lib.Bloc(4, 6, 7),
             lib.Bloc(4, 5, 6), lib.Bloc(6, 4, 5),
             lib.Bloc(1, 2, 3), lib.Bloc(3, 1, 2)]


class TestStringMethods(unittest.TestCase):
    def test_algo_dynamic(self):
        a = lib.algo_dynamic(bloc_test)
        self.assertEqual(a, 60)


if __name__ == '__main__':
    unittest.main()
