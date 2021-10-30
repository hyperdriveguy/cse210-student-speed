from linecache import checkcache
from game.file_service import FileService
import random

class WordListService(FileService):

    def __init__(self, wordlist, user_list=True):
        super().__init__(wordlist)
        self._user_list = user_list
    
    @property
    def new_word(self):
         return super().read_line(
            random.randint(1, super().num_lines),
            check_cache=self._user_list,
            strip=True)
