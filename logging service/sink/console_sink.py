from sink.sink import Sink


class ConsoleSink(Sink):
    def write(self, formatted_log):
        print(formatted_log)
        return
