from abc import ABC, abstractmethod
"""
Blueprint interface for input cron string.
The class implementing this interface will take cron_string as an input and implement the parsing logic into it.
"""
class CronStringInterface(ABC):
    @abstractmethod
    def _parse_cron_string(self):
        pass

    @abstractmethod
    def get_parts(self):
        pass

    @abstractmethod
    def _expand_range(self, expression, range_start, range_end):
        pass

    @abstractmethod
    def parse(self):
        pass