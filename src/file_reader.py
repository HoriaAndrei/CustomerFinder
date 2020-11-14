class FileReader:
    """Class that handles reading from a file, one line at a time."""
    def __init__(self, input_file: str):
        self._file = input_file
        self._file_handle = None
        try:
            self._file_handle = open(self._file)
        except FileNotFoundError:
            print("File " + input_file + " does not exist")
            raise

    def __del__(self):
        if self._file_handle is not None:
            self._file_handle.close()

    def read_line(self) -> str:
        if self._file_handle is not None:
            line = self._file_handle.readline()
            if line:
                return line.strip()
            else:
                return None
