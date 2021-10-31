import random
from game.point import Point
from game.word_list_service import WordListService

class Word(Point):
    """	Holds information for a given word on screen.
    
    stereotype: Information Holder
    
    attributes:
        _word: the word passed in
        _max_vel: the max velocity. default 0
    """
    def __init__(self, word, x, y, max_vel=0):
        """The class constructor.
        
        Args:
            self (Word): An instance of Word.
        """

        super().__init__(x, y)
        self._word = word
        self._max_vel = max_vel
        self.rand_word_velocity()
    
    def rand_word_velocity(self):
        """get random velocity if max velocity doesn't equal zero.
        
        args:
           self (Word): An instance of Word. 
        """
        if self._max_vel != 0:
            self._velocity_x = random.randint(- self._max_vel, self._max_vel)
            self._velocity_y = random.randint(- self._max_vel, self._max_vel)
    
    @property
    def word(self):
        """get word.
        
        args:
            self (Word): An instance of Word.

        returns
            string: the word
        """
        return self._word
    
    def compare_word(self, other_str: str):
        """compares word with other string
        
        args:
            self (Word): An instance of Word.
        
        Returns:
            (bool). if other string equals word return true.
        """
        return other_str == self._word

    @property
    def length(self):
        """get length of the word.
        
        args:
            self (Word): An instance of Word.
        
        returns:
            integer: the length of the word
        """
        return len(self._word)
