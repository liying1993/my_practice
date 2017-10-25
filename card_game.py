import pdb
class Game():
    KARTS = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13,
             'A': 14}
    _player1deck = ['6H', '7H', '6C', 'QS', '7S', '8D', '6D', '5S', '6S', 'QH', '4D', '3S', '7C', '3C', '4S', '5H', 'QD', '5C', '3H', '3D', '8C', '4H', '4C', 'QC', '5D', '7D']
    _player2deck = ['JH', 'AH', 'KD', 'AD', '9C', '2D', '2H', 'JC', '10C', 'KC', '10D', 'JS', 'JD', '9D', '9S', 'KS', 'AS', 'KH', '10S', '8S', '2S', '10H', '8H', 'AC', '2C', '9H']
    _player1table = []
    _player2table = []
    _winner = "PAT"
    _round = 0
    _war = False

    def __init__(self):
        # for i in range(int(input())):
        #     self._player1deck.append(input())  # the n cards of player 1
        #
        # for i in range(int(input())):
        #     self._player2deck.append(input())  # the m cards of player 2
        self.current_status()

    def current_status(self):
        pass

    def print_result(self):
        # pdb.set_trace()
        if self._winner == "PAT":
            print("PAT")
        else:
            print("{0} {1}".format(self._winner, self._round))

    def drag_karts(self, n=1):
        # pdb.set_trace()
        for i in range(n):
            self._player1table.append(self._player1deck.pop(0))
            self._player2table.append(self._player2deck.pop(0))
        self.current_status()

    def player_got_all(self, np):
        # pdb.set_trace()
        for kart in self._player1table:
            if np == 1:
                self._player1deck.append(kart)
            else:
                self._player2deck.append(kart)

        for kart in self._player2table:
            if np == 1:
                self._player1deck.append(kart)
            else:
                self._player2deck.append(kart)

        self._player1table = []
        self._player2table = []

    def check_carts(self):
        # pdb.set_trace()
        p1_kart = self.KARTS[self._player1table[-1][:-1]]
        p2_kart = self.KARTS[self._player2table[-1][:-1]]
        if p1_kart > p2_kart:
            self.player_got_all(1)
            self._war = False
        elif p1_kart < p2_kart:
            self.player_got_all(2)
            self._war = False
        else:
            self._war = True

    def have_enought_karts(self, n):
        # pdb.set_trace()
        len1, len2 = len(self._player1deck), len(self._player2deck)
        if len1 >= n and len2 >= n:
            return True
        else:
            # set the winner
            if self._war:
                self._winner = "PAT"
            elif len1 - n < 0 and len2 - n < 0:
                self._winner = "PAT"
            elif (len1 > len2):
                self._winner = "1"
            else:
                self._winner = "2"

            return False

    def play(self):
        pdb.set_trace()
        if self._war:
            if self.have_enought_karts(3):
                self.drag_karts(3)
            else:
                return False
        if self.have_enought_karts(1):
            if not (self._war):
                self.round_plus()
            self.drag_karts()
            self.check_carts()
        else:
            return False
        return True

    def pull_3_karts(self):
        self.current_status()

    def round_plus(self):
        self._round = self._round + 1

    def run(self):
        while self.play():
            self.current_status()

game = Game()
game.run()
game.print_result()