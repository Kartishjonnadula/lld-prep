from log_level import LogLevel
from datetime import datetime


class LogRecord:
    msg: str
    timestamp: datetime
    log_level: LogLevel
