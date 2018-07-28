import sys
import unittest
import unittest.mock as mock
import main


class MainTest(unittest.TestCase):

    def setUp(self):
        main.TEAMS = {
            'T1': 5,
            'T2': 3,
            'T3': 7,
            'T4': 6,
            'T5': 4,
            'T6': 1,
        }
        main.MATCHES = (
            (('T1', 'T2'), ('T3', 'T4'), ('T5', 'T6'),),
            (('T1', 'T3'), ('T4', 'T5'), ('T2', 'T6'),),
            (('T1', 'T4'), ('T2', 'T5'), ('T3', 'T6'),),
            (('T1', 'T5'), ('T2', 'T3'), ('T4', 'T6'),),
            (('T1', 'T6'), ('T2', 'T4'), ('T3', 'T5'),),
        )

    def test_opponent(self):
        res = main._opponent('T1', ('T1', 'T2'))
        self.assertEqual(res, 'T2')

        res = main._opponent('T1', ('T2', 'T1'))
        self.assertEqual(res, 'T2')

    def test_find_match(self):
        res = main._find_match('T1', 0)
        self.assertEqual(res, ('T1', 'T2'))

    def test_match_difficult(self):
        res = main._match_difficult('T1', ('T1', 'T2'))
        self.assertEqual(res, -2)

        res = main._match_difficult('T1', ('T2', 'T1'))
        self.assertEqual(res, -2)

        res = main._match_difficult('T1', ('T1', 'T4'))
        self.assertEqual(res, 1)

    def test_calculate_difficult(self):
        res = main.calculate_difficult([])
        self.assertEqual(res, float('Inf'))

        res = main.calculate_difficult(['T3'])
        self.assertEqual(res, -16)

        res = main.calculate_difficult(['T1'])
        self.assertEqual(res, -4)

        # week | T4 | T5 | MIN
        #    0 | +1 | -3 | -3
        #    1 | -2 | +2 | -2
        #    2 | -1 | -1 | -1
        #    3 | -5 | +1 | -5
        #    4 | -3 | -1 | -3
        #      | -------------
        #      |           -14
        res = main.calculate_difficult(['T4', 'T5'])
        self.assertEqual(res, -14)

    @mock.patch('sys.argv', ['xyz.py', 'T1', 'T2'])
    @mock.patch('builtins.print', mock.Mock())
    @mock.patch('main.calculate_difficult')
    def test_main(self, calculate_difficult):
        main.main()
        calculate_difficult.assert_called_once_with(['T1', 'T2'])


if __name__ == '__main__':
    unittest.main()
