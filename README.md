# Deliveroo
Cron Expression Parser

# integration testing
run the integration tests using
python3 -m unittest cron_parser.tests.test_integration

# main file
run the main file using
python3 main.py "*/15 0 1,15 * 1-10 /usr/bin/find"

# File structure
-formatter
This module takes care of the extensibility of the ways in which we can format the output. Specifically for the current problem, we are using "default_formatter" which is implemented using "formatter_interface".

-input_cron_string
This module takes care of the extensibility of the ways in which we can have input format.
For the current problem we are using "deafault_input_cron_string" which takes input
considering the standard cron format with five time fields (minute, hour, day of
month, month, and day of week) plus a command, and do not handle the special
time strings such as "@yearly".

To accomodate special strings, we can extend the input_cron_string accordingly.

-tests
This module contains the integration tests to test the complete functionality.

- cron_parser.py
This file uses the cron_string_obj and formatter_obj, to call the main parsing function.

-main
This is the deriving file which takes user's input and by creating DefaultInputCronString and DefaultFormatter, calls the parser and then displays the output.

# P.S.
For now the validations are not handled.
And Exception handling and logging is not done.

