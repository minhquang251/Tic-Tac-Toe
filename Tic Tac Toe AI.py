class Game:
    def __init__(self):
        self.board = ["_" for i in range(9)]
        self.winner = ""
        self.first_turn = ""
        self.last_move = []

    def print_board(self):
        for i in range(9):
            print(i,self.board[i], end="\t")
            if i == 2 or i == 5 or i == 8:
                print()

    def determine_first_turn(self):
        decision = ''
        while decision != "Human" and decision != "AI":
            decision = input("Who will move first: Human or AI?")
            self.first_turn = decision

    def is_game_over(self):
        win_case = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
        for i,j,k in win_case:
            if self.board[i] == self.board[j] == self.board[k] and self.board[i] != "_":
                if self.board[i] == "O":
                    self.winner = "AI"
                    return True
                elif self.board[i] == "X":
                    self.winner = "Human"
                    return True
        if "_" not in self.board:
            self.winner = "_"
            return True
        return False

    def get_free_square(self):
        lst = []
        for i in range(9):
            if self.board[i] == "_":
                lst.append(i)
        return lst

    def undo_move(self):
        i = self.last_move.pop()
        self.board[i] = "_"
        self.winner = None

    def mark(self, square, mark):
        self.board[square] = mark
        self.last_move.append(square)

    def play(self, player_1, player_2):
        self.determine_first_turn()
        self.print_board()
        if self.first_turn == "Human":
            for i in range(9):
                if i % 2 == 0:
                    player_1.choose_square(self)
                else:
                    player_2.choose_square(self)
                self.print_board()
                print("\n")
                if self.is_game_over():
                    if self.winner != "_":
                        print(self.winner,"wins the game")
                    else:
                        print("Tide")
        else:
            for i in range(9):
                if i % 2 == 0:
                    player_2.choose_square(self)
                    self.print_board()
                else:
                    player_1.choose_square(self)
                    self.print_board()
                print("\n")
                if self.is_game_over():
                    if self.winner != "_":
                        print(self.winner,"wins the game")
                    else:
                        print("Tide")


class Human:
    def __init__(self):
        self.mark = "X"

    def choose_square(self, game):
        move = int(input("Human's decision:"))
        if move < 0 or move > 8:
            print("Invalid Input")
            return self.choose_square(Game)
        else:
            if move in game.get_free_square():
                game.mark(move, self.mark)
            else:
                print("Invalid Input")
                return self.choose_square(Game)


class AI:
    def __init__(self):
        self.ai_mark = "O"
        self.human_mark = "X"

    def calc_score(self, game):
        if game.winner == "Human":
            return -10
        elif game.winner == "AI":
            return 10
        elif game.winner == "_":
            return 0

    def maximize(self, game):
        best_score = None
        best_move = None
        for move in game.get_free_square():
            game.mark(move, self.ai_mark)
            if game.is_game_over():
                score = self.calc_score(game)
            else:
                score, move_position = self.minimize(game)
            game.undo_move()
            if best_score is None or score > best_score:
                best_score = score
                best_move = move
        return best_score, best_move

    def minimize(self, game):
        best_score = None
        best_move = None
        for move in game.get_free_square():
            game.mark(move, self.human_mark)
            if game.is_game_over():
                score = self.calc_score(game)
            else:
                score, move_position = self.maximize(game)
            game.undo_move()
            if best_score is None or score < best_score:
                best_score = score
                best_move = move
        return best_score, best_move

    def choose_square(self, game):
        score, move_position = self.maximize(game)
        game.mark(move_position, self.ai_mark)


new_game = Game()
player_I = Human()
player_II = AI()
new_game.play(player_I,player_II)
