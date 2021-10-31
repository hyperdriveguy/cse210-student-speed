from game.file_service import FileService
import random

class WordListService(FileService):
    """Fetches words from given wordlists to put on the screen.
    
    Stereotype:
        Service Provider
    
    Attributes:
        _user_list (bool): default set to true
    """
    def __init__(self, wordlist, user_list=True):
        """The class constructor.
        
        Args:
            self (WordListService): An instance of WordListService.
        """

        super().__init__(wordlist)
        self._user_list = user_list
    
    @property
    def new_word(self):
        """Fetches word from line in file.
        
        Args:
            self (WordListService): an instance of WordListService

        Returns:
            string: word from file
        """
        return self.read_line(
            random.randint(1, super().num_lines),
            check_cache=self._user_list,
            strip=True)
