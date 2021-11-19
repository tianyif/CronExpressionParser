import unittest
from cronExpressionParser import CronExpressionParser
from timeType import TimeType

class CronExpressionParserTestCase:
    def __init__(self, input, minute=None, hour=None, dayOfMonth=None, month=None, dayOfWeek=None, command=None):
        self.input = input
        self.expectedMinute = minute
        self.expectedHour = hour
        self.expectedDayOfMonth = dayOfMonth
        self.expectedMonth = month
        self.expectedDayOfWeek = dayOfWeek
        self.expectedCommand = command

class TestCronExpressionParser(unittest.TestCase):

    def test_parse_success(self):
        testCase = CronExpressionParserTestCase("*/15 0 1,15 * 1-5 /usr/bin/find", \
                                                "0 15 30 45", \
                                                "0", \
                                                "1 15", \
                                                "1 2 3 4 5 6 7 8 9 10 11 12", \
                                                "1 2 3 4 5", \
                                                "/usr/bin/find")

        parser = CronExpressionParser()
        result = parser.parse(testCase.input)

        self.__verify(testCase, result)

    def test_parse_failure_invalid_range(self):
        testCase = CronExpressionParserTestCase("*/15 0 1,15 * 7-5 /usr/bin/find", \
                                                "0 15 30 45", \
                                                "0", \
                                                "1 15", \
                                                "1 2 3 4 5 6 7 8 9 10 11 12", \
                                                "1 2 3 4 5", \
                                                "/usr/bin/find")

        parser = CronExpressionParser()

        with self.assertRaises(Exception) as context:
            _ = parser.parse(testCase.input)

        self.assertTrue("[InvalidCronExpressionDomain]" in str(context.exception))

    def __verify(self, testCase, result):
        splittedResult = result.split("\n")
        self.assertTrue(len(splittedResult) == 6)

        minuteLine, hourLine, dayOfMonthLine, monthLine, dayOfWeekLine, commandLine = splittedResult

        self.assertTrue(len(minuteLine) > 14)
        self.assertEqual(minuteLine[:14].find(TimeType.minute.displayString()), 0)
        self.assertEqual(minuteLine[15:], testCase.expectedMinute)

        self.assertTrue(len(hourLine) > 14)
        self.assertEqual(hourLine[:14].find(TimeType.hour.displayString()), 0)
        self.assertEqual(hourLine[15:], testCase.expectedHour)

        self.assertTrue(len(dayOfMonthLine) > 14)
        self.assertEqual(dayOfMonthLine[:14].find(TimeType.dayOfMonth.displayString()), 0)
        self.assertEqual(dayOfMonthLine[15:], testCase.expectedDayOfMonth)

        self.assertTrue(len(monthLine) > 14)
        self.assertEqual(monthLine[:14].find(TimeType.month.displayString()), 0)
        self.assertEqual(monthLine[15:], testCase.expectedMonth)

        self.assertTrue(len(dayOfWeekLine) > 14)
        self.assertEqual(dayOfWeekLine[:14].find(TimeType.dayOfWeek.displayString()), 0)
        self.assertEqual(dayOfWeekLine[15:], testCase.expectedDayOfWeek)

        self.assertTrue(len(commandLine) > 14)
        self.assertEqual(commandLine[:14].find("command"), 0)
        self.assertEqual(commandLine[15:], testCase.expectedCommand)

if __name__ == '__main__':
    unittest.main()
