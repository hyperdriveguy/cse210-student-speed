from game.file_service import FileService
import random

class WordListService(FileService):

    def __init__(self, wordlist):
        super().__init__(wordlist)
    
    @property
    def new_word(self):
         return super().read_line(
            random.randint(1, super().num_lines),
            strip=True)