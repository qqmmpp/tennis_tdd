
class TennisGame:
    def __init__(self, player1, player2):
        self.p1_name = player1
        self.p2_name = player2
        self.P1_score = 0
        self.P2_score = 0
        self.score_mapping = {
            0: 'Love',
            1: 'Fifteen',
            2: 'Thirty',
            3: 'Forty'
        }

    def lookup_score(self):
        return '%s-%s' % (self.score_mapping[self.P1_score], self.score_mapping[self.P2_score])

    def score(self):
        if self.is_deuce():
            return 'Deuce'

        if self.is_the_same_score():
            return self.the_same_score()

        if self.is_someone_score_more_than_forty():
            return self.game_point_score()

        return self.lookup_score()

    def game_point_score(self):
        if self.is_win():
            return self.who_is_better('Win')
        else:
            return self.who_is_better('AD')

    def the_same_score(self):
        return '%s-All' % self.score_mapping[self.P1_score]

    def add_score(self, player, times):
        for i in range(0, times):
            if player == self.p1_name:
                self.P1_score = self.P1_score + 1
            else:
                self.P2_score = self.P2_score + 1

    def is_deuce(self):
        if self.is_the_same_score() and self.P1_score >= 3:
            return True
        else:
            return False

    def is_the_same_score(self):
        if self.P1_score == self.P2_score:
            return True
        else:
            return False

    def is_win(self):
        if self.is_someone_score_more_than_forty() and self.is_score_gap_more_than(2):
            return True
        else:
            return False

    def who_is_better(self, status):
        if self.P1_score > self.P2_score:
            return '%s %s' % (self.p1_name, status)
        else:
            return '%s %s' % (self.p2_name, status)

    def is_score_gap_more_than(self, gap):
        if abs(self.P1_score - self.P2_score) >= gap:
            return True
        else:
            return False

    def is_someone_score_more_than_forty(self):
        if self.P1_score > 3 or self.P2_score > 3:
            return True
        else:
            return False

