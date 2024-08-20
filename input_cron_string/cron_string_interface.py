from abc import ABC, abstractmethod

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