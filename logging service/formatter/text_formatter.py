from formatter.formatter import Formatter
from log_record import LogRecord


class TextFormatter(Formatter):
    def format(self, log_record: LogRecord):
        return f"{log_record.timestamp}|{log_record.msg}|{log_record.log_level}"
