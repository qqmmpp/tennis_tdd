import unittest
import tennis_game

class Tennis(unittest.TestCase):
    def setUp(self):
        self.tennis_game = tennis_game.TennisGame('Peter', 'Daniel')

    def test_love_all(self):
        self.score_should_be('Love-All')

    def test_fifteen_love(self):
        self.tennis_game.add_score('Peter', 1)
        self.score_should_be('Fifteen-Love')

    def test_thirty_love(self):
        self.tennis_game.add_score('Peter', 2)
        self.score_should_be('Thirty-Love')

    def test_forty_love(self):
        self.tennis_game.add_score('Peter', 3)
        self.score_should_be('Forty-Love')

    def test_love_fifteen(self):
        self.tennis_game.add_score('Daniel', 1)
        self.score_should_be('Love-Fifteen')

    def test_love_thirty(self):
        self.tennis_game.add_score('Daniel', 2)
        self.score_should_be('Love-Thirty')

    def test_love_forty(self):
        self.tennis_game.add_score('Daniel', 3)
        self.score_should_be('Love-Forty')

    def test_fifteen_all(self):
        self.tennis_game.add_score('Peter', 1)
        self.tennis_game.add_score('Daniel', 1)
        self.score_should_be('Fifteen-All')

    def test_Thirty_all(self):
        self.tennis_game.add_score('Peter', 2)
        self.tennis_game.add_score('Daniel', 2)
        self.score_should_be('Thirty-All')

    def test_Deuce(self):
        self.tennis_game.add_score('Peter', 3)
        self.tennis_game.add_score('Daniel', 3)
        self.score_should_be('Deuce')

    def test_player1_AD(self):
        self.tennis_game.add_score('Peter', 4)
        self.tennis_game.add_score('Daniel', 3)
        self.score_should_be('Peter AD')

    def test_player2_AD(self):
        self.tennis_game.add_score('Peter', 3)
        self.tennis_game.add_score('Daniel', 4)
        self.score_should_be('Daniel AD')

    def test_player1_win_type1(self):
        self.tennis_game.add_score('Peter', 4)
        self.tennis_game.add_score('Daniel', 0)
        self.score_should_be('Peter Win')

    def test_player1_win_type2(self):
        self.tennis_game.add_score('Peter', 6)
        self.tennis_game.add_score('Daniel', 4)
        self.score_should_be('Peter Win')

    def test_player2_win_type1(self):
        self.tennis_game.add_score('Peter', 0)
        self.tennis_game.add_score('Daniel', 4)
        self.score_should_be('Daniel Win')

    def test_player2_win_type2(self):
        self.tennis_game.add_score('Peter', 4)
        self.tennis_game.add_score('Daniel', 6)
        self.score_should_be('Daniel Win')

    def score_should_be(self, expect_string):
        score = self.tennis_game.score()
        self.assertEqual(expect_string, score)


if __name__ == '__main__':
    unittest.main()
