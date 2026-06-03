from destination import Destination
from typing import Tuple
from log_record import LogRecord
from log_level import LogLevel

from datetime import datetime


class Logger:

    destinations: Tuple[Destination]

    def __init__(self, destinations: Tuple[Destination]):
        self.destinations = destinations

    def log(self, msg, log_level):
        log_record = LogRecord()
        log_record.msg = msg
        log_record.log_level = log_level
        log_record.timestamp = datetime.now()
        for destination in self.destinations:
            destination.write(log_record)

    def info(self, msg):
        self.log(msg, LogLevel.INFO)

    def debug(self, msg):
        self.log(msg, LogLevel.DEBUG)

    def warn(self, msg):
        self.log(msg, LogLevel.WARN)

    def error(self, msg):
        self.log(msg, LogLevel.ERROR)

    def fatal(self, msg):
        self.log(msg, LogLevel.FATAL)
