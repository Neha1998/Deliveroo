class CronParser:
    def __init__(self, cron_string_obj, formatter):
        self.cron_string_obj = cron_string_obj
        self.formatter = formatter

    def format_parsed_cron(self):
        parsed_cron = self.cron_string_obj.parse()
        return self.formatter.format(parsed_cron)
