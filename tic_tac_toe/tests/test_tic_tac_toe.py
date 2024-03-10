#Had to use an import sys function to make it work properly, I kept getting the No module named 'src' error when trying to run the test.
import unittest
import sys
project_path = r'C:\Users\Joe\OneDrive\Desktop\Cyber Secuirty\2024\Semester 1\IPOS 40120 Python\modularity-and-2d-data-structures-YaBoiJP\tic_tac_toe'
sys.path.insert(0, project_path)
from src.game import Board, check_tie

class TestTicTacToe(unittest.TestCase):
    def test_game_check_tie(self):
        board = Board()
        board.cells = [['X', 'O', 'X'],
                       ['O', 'X', 'O'],
                       ['O', 'X', 'O']]
        
        self.assertTrue(check_tie(board.cells))

if __name__ == '__main__':
    unittest.main()