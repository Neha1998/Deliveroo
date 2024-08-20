import sys
from input_cron_string.defaut_input_cron_string import DefaultInputCronString
from cron_parser import CronParser
from formatter.default_formatter import DefaultFormatter

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py '<cron_string>'")
        sys.exit(1)

    cron_string_input = sys.argv[1]

    cron_string_obj = DefaultInputCronString(cron_string_input)
    formatter = DefaultFormatter()
    parser = CronParser(cron_string_obj, formatter)

    output = parser.format_parsed_cron()
    print(output)

if __name__ == "__main__":
    main()
