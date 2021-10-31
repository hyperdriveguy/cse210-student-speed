from game import constants
from game.word import Word

class Buffer(Word):
    """holds the buffer information.
    
    stereotype: information holder
    
    attributes:
        _letters (string): letters the user has typed to display to the screen.
    """
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Buffer): An instance of Buffer.
        """
        super().__init__('', 1, constants.MAX_Y)
        self._letters = ''
    
    def _update_word(self):
        """update words showing on buffer.
        
        args:
            self (Buffer): An instance of Buffer.
        """
        self._word = f'Buffer: {self._letters}'

    def add_letter(self, letter):
        """Add letter to letters attribute. Call update_word
        
        Args:
            self (Buffer): An instance of Buffer.
            letter (str): letter to be added
        """
        self._letters += letter
        self._update_word()
    
    def del_letter(self):
        """delete letter from letters attribute. call update_word
        
        args:
            self (Buffer): An instance of Buffer.
        """
        self._letters = self._letters[:-2]
        self._update_word()
    
    @property
    def last_letter(self):
        """get the last letter in the letters attribute.
        
        args:
            self (Buffer): An instance of Buffer.

        returns:
            string: the last letter in the letters attribute
        """
        if len(self._letters) == 0:
            return ''
        return self._letters[-1]

    @property
    def letters(self):
        """get letters from letters attribute.
        
        args:
            self (Buffer): An instance of Buffer.
        
        returns
            string: the letters attribute
        """
        return self._letters

    def clear_letters(self):
        """Clear the letters from the letters attribute. calls update_word
        
        args:
            self (Buffer): An instance of Buffer.
         """
        self._letters = ''
        self._update_word()