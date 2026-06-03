import json

from formatter.formatter import Formatter
from log_record import LogRecord


class JsonFormatter(Formatter):
    def format(self, log_record: LogRecord):
        return json.dumps(
            {
                "message": log_record.msg,
                "timestamp": log_record.timestamp.isoformat(),
                "level": log_record.log_level.name,
            }
        )
