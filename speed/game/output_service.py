import sys
from game import constants
from asciimatics.widgets import Frame

class OutputService:
    """Outputs the game state. The responsibility of the class of objects is to draw the game state on the terminal. 
    
    Stereotype: 
        Service Provider

    Attributes:
        _screen (Screen): An Asciimatics screen.
    """

    def __init__(self, screen):
        """The class constructor.
        
        Args:
            self (OutputService): An instance of OutputService.
            screen (Screen): An Asciimatics Screen.
        """
        self._screen = screen
        
    def clear_screen(self):
        """Clears the Asciimatics buffer in preparation for the next rendering.

        Args:
            self (OutputService): An instance of OutputService.
        """ 
        self._screen.clear_buffer(7, 0, 0)
        self._screen.print_at("-" * constants.MAX_X, 0, 0, 7)
        self._screen.print_at("-" * constants.MAX_X, 0, constants.MAX_Y, 7)
        
    def place_word(self, word):
        """Renders the given word on the screen.

        Args:
            self (OutputService): An instance of OutputService.
            word (Word): The word to render on screen.
        """ 
        text = word.get_word()
        x = word.get_x()
        y = word.get_y()
        self._screen.print_at(text, x, y, 7) # WHITE
    
    def del_word(self, word):
        """Overwrites the given word on the screen.

        Args:
            self (OutputService): An instance of OutputService.
            word (Word): The word to delete from the screen.
        """
        length = word.length()
        x = word.get_x()
        y = word.get_y()
        self._screen.print_at((constants.BACKGROUND * length), x, y, 7) # WHITE
    
    def flush_buffer(self):
        """Renders the screen.

        Args:
            self (OutputService): An instance of OutputService.
        """ 
        self._screen.refresh()    
