from sink.sink import Sink


class FileSink(Sink):
    def __init__(self):
        self.file = open("file_name", "a")

    def write(self, formatted_log):
        self.file.write(formatted_log)
        self.file.flush()
        return
