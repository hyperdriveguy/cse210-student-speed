from game import constants
from game.word import Word

class Buffer(Word):

    def __init__(self):
        super().__init__('', 1, constants.MAX_Y)
        self._letters = ''
    
    def _update_word(self):
        self._word = f'Buffer: {self._letters}'

    def add_letter(self, letter):
        self._letters += letter
        self._update_word()
    
    def del_letter(self):
        self._letters = self._letters[:-1]
        self._update_word()
    
    @property
    def last_letter(self):
        if len(self._letters) == 0:
            return ''
        return self._letters[-1]

    @property
    def letters(self):
        return self._letters

    def clear_letters(self):
        self._letters = ''
        self._word = f'Buffer: {self._letters}'