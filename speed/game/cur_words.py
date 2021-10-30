import random
from game import constants
from game.word import Word
from game.word_list_service import WordListService

class CurWords:

    def __init__(self, user_lists=()):
        self._word_lists = [WordListService(constants.LIBRARY, user_list=False)]
        for word_list in user_lists:
            try:
                self._word_lists.append(WordListService(word_list, user_list=True))
            except FileNotFoundError:
                pass
        self._max_words = constants.STARTING_WORDS
        self._word_store = set()
    
    def add_new_word(self, x, y):
        rand_list = random.choice(self._word_lists)
        word_fetch = ''
        while word_fetch == '' or self.check_word_match(word_fetch):
            word_fetch = rand_list.new_word
        built_word = Word(word_fetch, x, y)
        self._word_store.add(built_word)

    def check_word_match(self, compare_str):
        for w in self._word_store:
            if w.compare_word(compare_str):
                return True
        return False
    
    def remove_word(self, to_remove):
        self._word_store.remove(to_remove)
    
    def move_words(self):
        for word in self._word_store:
            word.update_position()

