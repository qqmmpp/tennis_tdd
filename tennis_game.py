
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

    def score(self):
        if self.is_game_start():
            return 'Love-All'
        else:
            if self.is_win():
                return self.who_is_better('Win')

            elif self.is_ad():
                return self.who_is_better('AD')

            elif self.is_deuce():
                return 'Deuce'

            elif self.is_the_same_score():
                return '%s-All' % self.score_mapping[self.P1_score]

            else:
                return '%s-%s' % (self.score_mapping[self.P1_score], self.score_mapping[self.P2_score])

    def add_score(self, player, times):
        for i in range(0, times):
            if player == self.p1_name:
                self.P1_score = self.P1_score + 1
            else:
                self.P2_score = self.P2_score + 1

    def is_game_start(self):
        if self.is_the_same_score() and self.P1_score == 0:
            return True
        else:
            return False

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

    def is_ad(self):
        if self.is_score_more_than_forty() and self.is_score_gap_more_than(1):
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

    def is_score_more_than_forty(self):
        if self.P1_score >= 3 and self.P2_score >= 3:
            return True
        else:
            return False
