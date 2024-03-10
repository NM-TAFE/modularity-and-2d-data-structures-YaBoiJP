#making board for new tictactoe
class Board:
    def __init__(self):
        self.cells = [[" " for _ in range(3)] for _ in range(3)]
    
    def display(self):
        for row in self.cells:
            print(" | ".join(row))
            print("---------")
    def count(self, value):
        return sum(row.count(value) for row in self.cells)