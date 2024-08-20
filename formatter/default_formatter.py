from .formatter_interface import FormatterInterface

"""
In our problem we'll be using Default Formatter.
"""
class DefaultFormatter(FormatterInterface):
    def format(self, parsed_cron):
        output = [
            f"{'minute':<14}{' '.join(map(str, parsed_cron['minute']))}",
            f"{'hour':<14}{' '.join(map(str, parsed_cron['hour']))}",
            f"{'day of month':<14}{' '.join(map(str, parsed_cron['day of month']))}",
            f"{'month':<14}{' '.join(map(str, parsed_cron['month']))}",
            f"{'day of week':<14}{' '.join(map(str, parsed_cron['day of week']))}",
            f"{'command':<14}{parsed_cron['command']}"
        ]
        return "\n".join(output)
