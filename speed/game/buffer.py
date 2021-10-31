from game import constants
from game.word import Word

class Buffer(Word):

    def __init__(self):
        super().__init__('', 1, constants.MAX_Y)
        self._letters = ''
        self._word = f'Buffer: {self._letters}'

    def add_letter(self, letter):
        self._letters += letter
        self._word = f'Buffer: {self._letters}'

    def get_letters(self):
        return self._letters

    def clear_letters(self):
        self._letters = ''