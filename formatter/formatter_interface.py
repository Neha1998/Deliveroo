from abc import ABC, abstractmethod
"""
Formatter interface will be used to make formatter extensible.
"""
class FormatterInterface(ABC):
    @abstractmethod
    def format(self, parsed_cron):
        pass
