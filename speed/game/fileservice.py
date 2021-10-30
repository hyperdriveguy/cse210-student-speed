import linecache
from os import EX_PROTOCOL
from typing import Iterable

class FileService:

    def __init__(self, file_name):
        self._file_name = file_name
        self._calc_lines()
    
    def _calc_lines(self):
        with open(self._file_name, 'r') as f:
            self._num_lines = len([0 for _ in f])
    
    @property
    def num_lines(self):
        return self._num_lines

    def read_line(self, line_num, check_cache=False, strip=False):
        if check_cache:
            linecache.checkcache(self._file_name)
        line = linecache.getline(self._file_name, line_num)
        if strip:
            line = line.strip()
        return line
    
    def read_file(self):
        try:
            with open(self._file_name, 'r') as f:
                lines = f.readlines()
        except MemoryError:
            raise MemoryError(f'File {self._file_name} is too large to be stored in memory.')
        return lines
    
    def overwrite_file(self, content):
        with open(self._file_name, 'w') as f:
            if type(content) == str:
                f.write(content)
            elif type(content) == list or type(content) == tuple:
                f.writelines(content)
            else:
                raise TypeError(f'Type "{type(content)}" is not writable to file.')
    
    @property
    def content(self):
        return self.read_file()
    
    @content.setter
    def content(self, content: Iterable):
        self.overwrite_file(content)
