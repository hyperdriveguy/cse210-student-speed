import random
from game import constants
from game.word import Word
from game.word_list_service import WordListService

class CurWords:
    """Contains information for all words on screen.
    
    Stereotype: INformation Holder
    
    Attributes:
        _word_lists (list): list of words
        _max_words (int): max number of words to start with
        _word_store (list): list of words to be displayed to screen
    """
    def __init__(self, user_lists=()):
        """The class constructor.
        
        Args:
            self (CurWords): An instance of CurWords.
        """

        self._word_lists = [WordListService(constants.LIBRARY, user_list=False)]
        for word_list in user_lists:
            try:
                self._word_lists.append(WordListService(word_list, user_list=True))
            except FileNotFoundError:
                pass
        self._max_words = constants.STARTING_WORDS
        self._word_store = []

    @property
    def max_words(self):
        """Get max number of words
        
        Args:
            self (CurWords): An instance of CurWords.
        
        Returns max number of words as int
        """
        return self._max_words
    
    @max_words.setter
    def max_words(self, max_words: int):
        """Set max number of words
        
        Args:
            self (CurWords): An instance of CurWords.
            max_words: max words as int
        """
        if max_words < 1:
            return
        self._max_words = max_words

    def add_new_word(self, vel):
        """Add word to word store.
        
        Args:
            self (CurWords): An instance of CurWords.
            vel: velocity
        """
        if len(self._word_store) == self._max_words:
            return
        x = random.randint(1, constants.MAX_X - 2)
        y = random.randint(1, constants.MAX_Y - 2)
        rand_list = random.choice(self._word_lists)
        word_fetch = ''
        while word_fetch == '' or self.check_word_match(word_fetch):
            word_fetch = rand_list.new_word
        built_word = Word(word_fetch, x, y, max_vel=vel)
        self._word_store.append(built_word)

    def check_word_match(self, compare_str):
        """check if word matches string of letters.
        
        args:
            self (CurWords): An instance of CurWords.
            compare_str (str): string to be compared

        Returns:
            (bool) true if word and string match. False if not.
        """
        for w in self._word_store:
            if w.compare_word(compare_str):
                return True
        return False
    
    def remove_word(self, to_remove):
        """Remove word from word store.
        
        Args:
            self (CurWords): An instance of CurWords.
            to_remove: word to remove

        Return:
            word store with word removed    
        """
        for w_index, w in enumerate(self._word_store):
            if w.word == to_remove:
                popped = self._word_store.pop(w_index)
                return popped
    
    def move_words(self):
        """move the words
        
        args:
            self (CurWords): An instance of CurWords.
        """
        for word in self._word_store:
            word.update_position()
    
    @property
    def empty_word_store(self):
        """Check if word store is empty.
        
        args:
            self (CurWords): An instance of CurWords.
        Return true if word store is empty.
        """
        return len(self._word_store) == 0
