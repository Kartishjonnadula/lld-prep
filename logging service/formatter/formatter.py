from abc import ABC, abstractmethod


class Formatter:
    @abstractmethod
    def format(self, log_record):
        pass
