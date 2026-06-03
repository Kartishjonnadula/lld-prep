from logger import Logger
from sink.console_sink import ConsoleSink
from destination import Destination
from formatter.json_formatter import JsonFormatter
from formatter.text_formatter import TextFormatter
from log_level import LogLevel

console_sink = ConsoleSink()
json_formatter = JsonFormatter()
text_formatter = TextFormatter()
console_destination = Destination(json_formatter, console_sink, LogLevel.INFO, 100)

text_destination = Destination(text_formatter, console_sink, LogLevel.WARN, 100)
logger = Logger((console_destination, text_destination))
logger.info("test log 1")
logger.error("error log text3")

console_destination.flush()
text_destination.flush()
