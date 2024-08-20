import unittest
from unittest.mock import patch
import sys
from io import StringIO

from main import main

class TestCronParserIntegration(unittest.TestCase):
    
    @patch('sys.argv', ['main.py', '*/15 0 1,15 * 1-5 /usr/bin/find'])
    def test_default_cron_string(self):
        expected_output = (
            "minute        0 15 30 45\n"
            "hour          0\n"
            "day of month  1 15\n"
            "month         1 2 3 4 5 6 7 8 9 10 11 12\n"
            "day of week   1 2 3 4 5\n"
            "command       /usr/bin/find\n"
        )
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            main()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.argv', ['main.py', '0 0 1 * * /usr/bin/find'])
    def test_daily_cron_string(self):
        expected_output = (
            "minute        0\n"
            "hour          0\n"
            "day of month  1\n"
            "month         1 2 3 4 5 6 7 8 9 10 11 12\n"
            "day of week   0 1 2 3 4 5 6\n"
            "command       /usr/bin/find\n"
        )
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            main()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.argv', ['main.py', '0 0 1 1 * /usr/bin/backup'])
    def test_yearly_backup_cron_string(self):
        expected_output = (
            "minute        0\n"
            "hour          0\n"
            "day of month  1\n"
            "month         1\n"
            "day of week   0 1 2 3 4 5 6\n"
            "command       /usr/bin/backup\n"
        )
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            main()
            self.assertEqual(mock_stdout.getvalue(), expected_output)
    
    @patch('sys.argv', ['main.py', '*/5 * * * 1-5 /usr/bin/sync'])
    def test_frequent_sync_cron_string(self):
        expected_output = (
            "minute        0 5 10 15 20 25 30 35 40 45 50 55\n"
            "hour          0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23\n"
            "day of month  1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31\n"
            "month         1 2 3 4 5 6 7 8 9 10 11 12\n"
            "day of week   1 2 3 4 5\n"
            "command       /usr/bin/sync\n"
        )
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            main()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
