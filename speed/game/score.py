from game.word import Word

class Score(Word):
    """Points earned. The responsibility of Score is to keep track of the player's points.

    Stereotype:
        Information Holder

    Attributes: 
        _points (integer): The number of points the word is worth.
        _total_points (integer): The number of total points the player has.
        _word (string): The text to display the player's score.
    """
    def __init__(self):
        """The class constructor. Invokes the superclass constructor, initializes points to zero, sets the position and updates the text.
        
        Args:
            self (Score): an instance of Score.
        """
        super().__init__('', 1, 0)
        self._points = 0
        self._total_points = 0
        self._word = f"Score: {self._total_points}"
    
    def set_points(self, other_str):
        """Sets the points for a word the player has correctly typed.
        
        Args:
            self (Score): an instance of Score
        """
        if self.compare_word(other_str):
            for i in self.length():
                self._points += 1

    def get_points(self):
        """Retrieves the points for a word the player has correctly typed.
        
        Args:
            self (Score): An instance of Score
        
        Returns: 
            Integer: the points for a word
        """
        return self._points             

    def add_points(self, points):
        """Adds the given points to the running total and updates the text.
        
        Args:
            self (Score): An instance of Score.
            points (integer): The points to add.
        """
        self._total_points += points
        self._word = f"Score: {self._total_points}"

