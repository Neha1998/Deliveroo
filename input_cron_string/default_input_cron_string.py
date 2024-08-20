
from .input_cron_string import CronStringInterface

class DefaultInputCronString(CronStringInterface):
    def __init__(self, cron_string):
        self.cron_string = cron_string
        self.minute_part = ""
        self.hour_part = ""
        self.day_of_month_part = ""
        self.month_part = ""
        self.day_of_week_part = ""
        self.command_part = ""
        self._parse_cron_string()

    def _parse_cron_string(self):
        parts = self.cron_string.split()
        self.minute_part = parts[0]
        self.hour_part = parts[1]
        self.day_of_month_part = parts[2]
        self.month_part = parts[3]
        self.day_of_week_part = parts[4]
        self.command_part = parts[5]

    def get_parts(self):
        return {
            "minute": self.minute_part,
            "hour": self.hour_part,
            "day_of_month": self.day_of_month_part,
            "month": self.month_part,
            "day_of_week": self.day_of_week_part,
            "command": self.command_part,
        }

    def _expand_range(self, expression, range_start, range_end):
        if expression == "*":
            return list(range(range_start, range_end + 1))
        elif "/" in expression:
            base, step = expression.split('/')
            base_range = list(range(range_start, range_end + 1))
            return base_range[::int(step)]
        elif "-" in expression:
            start, end = map(int, part.split('-'))
            return list(range(start, end + 1))
        elif "," in expression:
            return sorted(int(x) for x in expression.split(','))
        else:
            return [int(expression)]

    def parse(self):
        parts = self.get_parts()
        minute = self._expand_range(parts['minute'], 0, 59)
        hour = self._expand_range(parts['hour'], 0, 23)
        day_of_month = self._expand_range(parts['day_of_month'], 1, 31)
        month = self._expand_range(parts['month'], 1, 12)
        day_of_week = self._expand_range(parts['day_of_week'], 0, 6)

        return {
            "minute": minute,
            "hour": hour,
            "day of month": day_of_month,
            "month": month,
            "day of week": day_of_week,
            "command": parts['command']
        }
