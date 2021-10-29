import linecache

class FileService:

    def __init__(self, file_name):
        self._file_name = file_name

    def read_line(self, line):
        