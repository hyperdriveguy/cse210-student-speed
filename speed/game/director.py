import random
from time import sleep
from game import constants
from game.score import Score
from game.word import Word
from game.buffer import Buffer
from game.cur_words import CurWords

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        
        input_service (InputService): The input mechanism.
        keep_playing (boolean): Whether or not the game can continue.
        output_service (OutputService): The output mechanism.
        _speed_mod = set speed
        _score (Score): The current score
        _buffer (Buffer): state of the buffer
        _cur_words (CurWords): words on the screen        
    """

    def __init__(self, input_service, output_service):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self._input_service = input_service
        self._keep_playing = True
        self._output_service = output_service
        self._speed_mod = 1
        self._score = Score()
        self._buffer = Buffer()
        self._cur_words = CurWords()
        
    def _prepare_game(self):
        """Prep for the game. Adding words to be displayed.
        
        Args:
            self (Director): An instance of Director"""
        for _ in range(self._cur_words.max_words):
            self._cur_words.add_new_word(random.randint(1, 2 + self._speed_mod))
    
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """

        self._prepare_game()
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
            sleep(constants.FRAME_LENGTH)

    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the letters the user types and adding it to the buffer to be displayed.

        Args:
            self (Director): An instance of Director.
        """
        letter = self._input_service.get_letter()
        self._buffer.add_letter(letter)

    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means checking for a word submission, updating the score, and clearing the buffer.

        Args:
            self (Director): An instance of Director.
        """
        if self._buffer.last_letter == '*':
            letters = self._buffer.letters[:-1]
            if self._cur_words.empty_word_store:
                if letters == 'y':
                    self._speed_mod += 1
                    self._prepare_game()
                else:
                    self._keep_playing = False
            if self._cur_words.check_word_match(letters):
                self._score.set_points(letters, self._speed_mod)
                points = self._score.points
                self._score.add_points(points)
                removed = self._cur_words.remove_word(letters)
                self._output_service.del_word(removed)
            self._buffer.clear_letters()
        elif self._buffer.last_letter == '\x08':
            self._buffer.del_letter()
        self._cur_words.move_words()
            


    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, this means displaying the score, words, and buffer. 
        If the user guess all the words, see if they want to keep playing. 

        Args:
            self (Director): An instance of Director.
        """
        self._output_service.clear_screen()
        for w in self._cur_words._word_store:
            self._output_service.place_word(w)
        self._output_service.place_word(self._score)
        self._output_service.place_word(self._buffer)
        if self._cur_words.empty_word_store:
            self._output_service.place_word(Word('Keep playing? (y/N)', 1, constants.MAX_Y - 1))
        self._output_service.flush_buffer()
