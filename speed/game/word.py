import random
from game.point import Point
from game.word_list_service import WordListService

class Word(Point):

    def __init__(self, word, x, y, max_vel=0):
        super().__init__(x, y)
        self._word = word
        self._max_vel = max_vel
        self.rand_word_velocity()
    
    def rand_word_velocity(self):
        if self._max_vel != 0:
            self._velocity_x = random.randint(- self._max_vel, self._max_vel)
            self._velocity_y = random.randint(- self._max_vel, self._max_vel)
    
    @property
    def word(self):
        return self._word
    
    def compare_word(self, other_str: str):
        return other_str == self._word

    @property
    def length(self):
        return len(self._word)
