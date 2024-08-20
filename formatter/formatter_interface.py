from abc import ABC, abstractmethod

class FormatterInterface(ABC):
    @abstractmethod
    def format(self, parsed_cron):
        pass
