from log_record import LogRecord
from queue import Queue
from threading import Thread


class Destination:
    def __init__(self, formatter, sink, log_level, capacity):
        self.log_level = log_level
        self.formatter = formatter
        self.sink = sink
        self.queue = Queue(capacity)
        self.worker = Thread(target=self.consumer, daemon=True)
        self.worker.start()

    def write(self, log_record: LogRecord):
        if log_record.log_level >= self.log_level:
            formatted_log = self.formatter.format(log_record)
            self.queue.put(formatted_log)

    def consumer(self):
        while True:
            formatted_log = self.queue.get()
            self.sink.write(formatted_log)
            self.queue.task_done()

    def flush(self):
        # waits still queue is empty
        self.queue.join()
