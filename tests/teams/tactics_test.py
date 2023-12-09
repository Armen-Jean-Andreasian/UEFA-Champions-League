from teams.tactics import LineUp
import unittest


class TestingMethods(unittest.TestCase):
    def test_value_error(self):
        team_name = ""
        formation = '4-3-2'
        lineup_obj = LineUp(team_name, formation)

        with self.assertRaises(ValueError) as context:
            lineup_obj.get_formation()
        self.assertTrue(str(context.exception))

    def test_formation_4_3_3(self):
        team_name = ""
        formation = '4-3-3'
        desired_lineup = ('GK', 'CB', 'CB', 'LB', 'RB', 'CM', 'CM', 'CM', 'RW', 'ST', 'LW')

        lineup_obj = LineUp(team_name, formation)
        current_lineup = lineup_obj.get_formation()
        self.assertEqual(current_lineup, desired_lineup)


if __name__ == '__main__':
    unittest.main()
