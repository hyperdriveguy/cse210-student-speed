import linecache
from typing import Iterable

class FileService:
    """Handles file inputs and outputs.
    
    Stereotype:
        Service Provider
        
    Attributes: 
        _file_name (file): The file to read"""
    def __init__(self, file_name):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
            file_name (file): The file
        """
        self._file_name = file_name
        self._calc_lines()
    
    def _calc_lines(self):
        """Open file - calculate lines.
        
        Args:
            self (FileService): An instance of FileService"""
        with open(self._file_name, 'r') as f:
            self._num_lines = len([0 for _ in f])
    
    @property
    def num_lines(self):
        """Gets number of lines
        
        Args:
            self (FileService): An instance of FileService
            
        Returns:
            integer: the number of  lines in the file    
        """
        return self._num_lines

    def read_line(self, line_num, check_cache=False, strip=False):
        """Read the line in the file
        
        Args:
            self (FileService): An instance of FileService
            line_num (int): the line number

        Returns:
            (str): the line in the file
        """
        if check_cache:
            linecache.checkcache(self._file_name)
        line = linecache.getline(self._file_name, line_num)
        if strip:
            line = line.strip()
        return line
    
    def read_file(self):
        """Reads the file
        
        Args:
            self (FileService): An instance of FileService
        
        Returns:
            lines from file
        """
        try:
            with open(self._file_name, 'r') as f:
                lines = f.readlines()
        except MemoryError:
            raise MemoryError(f'File {self._file_name} is too large to be stored in memory.')
        return lines
    
    def overwrite_file(self, content):
        """overwrites the file.
        
        Args:
            self (FileService): An instance of FileService
            content: the content to write
        
        """
        with open(self._file_name, 'w') as f:
            if type(content) == str:
                f.write(content)
            elif type(content) == list or type(content) == tuple:
                f.writelines(content)
            else:
                raise TypeError(f'Type "{type(content)}" is not writable to file.')
    
    @property
    def content(self):
        """get content
        
        Args:
            self (FileService): An instance of FileService

        returns:
            read_file method    
            """
        return self.read_file()
    
    @content.setter
    def content(self, content: Iterable):
        """set the content
        
        Args:
            self (FileService): An instance of FileService
            content as an iterable
            """
        self.overwrite_file(content)
