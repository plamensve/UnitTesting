from project.tennis_player import TennisPlayer

from unittest import TestCase, main


class TestTennisPlayer(TestCase):
    def test__init__correct(self):
        player = TennisPlayer('Plamen', 34, 100)
        self.assertEqual('Plamen', player.name)
        self.assertEqual(34, player.age)
        self.assertEqual(100, player.points)
        self.assertEqual([], player.wins)

    def test_setter_name_if_len_is_below_2_raise_error(self):
        with self.assertRaises(ValueError) as ex:
            player = TennisPlayer('P', 34, 100)
        self.assertEqual("Name should be more than 2 symbols!", str(ex.exception))

    def test_setter_name_if_len_is_equal_2_raise_error(self):
        with self.assertRaises(ValueError) as ex:
            player = TennisPlayer('Pl', 34, 100)
        self.assertEqual("Name should be more than 2 symbols!", str(ex.exception))

    def test_setter_age_if_bellow_age_raise_error(self):
        with self.assertRaises(ValueError) as ex:
            player = TennisPlayer('Plamen', 17, 100)
        self.assertEqual("Players must be at least 18 years of age!", str(ex.exception))

    def test_add_new_win_method_if_tour_name_in_wins(self):
        player = TennisPlayer('Plamen', 34, 100)
        player.wins = ['Test']
        self.assertEqual(f"Test has been already added to the list of wins!", player.add_new_win('Test'))

    def test_add_new_win_method_if_tour_name_not_in(self):
        player = TennisPlayer('Plamen', 34, 100)
        player.wins = []
        player.add_new_win('Test')
        self.assertEqual(player.wins[0], 'Test')

    def test__lt__method(self):
        player1 = TennisPlayer('Plamen', 30, 98)
        player2 = TennisPlayer('Anton', 30, 99)
        result = player1.__lt__(player2)
        self.assertEqual(f'{player2.name} is a top seeded player and he/she is better than {player1.name}', result)

        player1 = TennisPlayer('Plamen', 30, 100)
        player2 = TennisPlayer('Anton', 30, 99)
        result = player1.__lt__(player2)

        self.assertEqual(f'{player1.name} is a better player than {player2.name}', result)

    def test__str__method(self):
        player1 = TennisPlayer('Plamen', 30, 98)
        player1.wins = ['Test', 'Test1', 'Test2']
        result = str(player1)
        self.assertEqual(f"Tennis Player: {player1.name}\n" +
                         f"Age: {player1.age}\n" +
                         f"Points: {player1.points:.1f}\n" +
                         f"Tournaments won: {', '.join(player1.wins)}", result)










if __name__ == '__main__':
    main()