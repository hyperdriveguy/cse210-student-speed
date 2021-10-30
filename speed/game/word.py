from game.point import Point
from game.word_list_service import WordListService

class Word(Point):

    def __init__(self, word, x, y):
        super().__init__(x, y)
        self._word = word
    
    @property
    def word(self):
        return self._word
    
    def compare_word(self, other_str: str):
        return other_str == self._word

    @property
    def length(self):
        return len(self._word)
