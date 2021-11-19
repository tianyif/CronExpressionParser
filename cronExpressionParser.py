from timeType import TimeType

class CronExpressionParser:

    # Parse the command with cron expression into a formatted table.
    # Inputs:
    #   `input` - A string of command with cron expression.
    # Output: A string of formatted table as described in the problem statement.
    def parse(self, input):

        minuteRaw, hourRaw, dayOfMonthRaw, monthRaw, dayOfWeekRaw, commandRaw = input.split(" ")

        outputArray = []

        minuteFormattedLine = self.__parseTimeStringIntoFormattedLine(minuteRaw, TimeType.minute)
        outputArray.append(minuteFormattedLine)

        hourFormattedLine = self.__parseTimeStringIntoFormattedLine(hourRaw, TimeType.hour)
        outputArray.append(hourFormattedLine)

        dayOfMonthFormattedLine = self.__parseTimeStringIntoFormattedLine(dayOfMonthRaw, TimeType.dayOfMonth)
        outputArray.append(dayOfMonthFormattedLine)

        monthFormattedLine = self.__parseTimeStringIntoFormattedLine(monthRaw, TimeType.month)
        outputArray.append(monthFormattedLine)

        dayOfWeekFormattedLine = self.__parseTimeStringIntoFormattedLine(dayOfWeekRaw, TimeType.dayOfWeek)
        outputArray.append(dayOfWeekFormattedLine)

        commandFormattedLine = self.__parseCommandStringIntoFormattedLine(commandRaw)
        outputArray.append(commandFormattedLine)

        return "\n".join(outputArray)


    # Parse the string of command into a formatted string.
    # Inputs:
    #   `input`     - A string of command.
    # Output: A formatted string.
    def __parseCommandStringIntoFormattedLine(self, input):

        formattedLine = self.__getFormattedLine("command", input)

        return formattedLine


    # Parse the string of cron expression for one time type into a formatted string.
    # Inputs:
    #   `input`     - A string of cron expression for one time type.
    #   `timeType`  - A type from enum `TimeType`.
    # Output: A formatted string.
    def __parseTimeStringIntoFormattedLine(self, input, timeType):

        if input.find(",") != -1:
            arr = input.split(",") # I didn't sort this arr, will figure out if sorting is needed here.

            for time in arr:
                try:
                    timeInInt = int(time)
                except:
                    errorString = "[CronExpressionParserError][IntValueParseFailedDomain] Given input [{input}] is invalid for time type [{timeType}]".format(input=input, timeType=timeType.displayString())
                    raise Exception(errorString)
                else:
                    if timeInInt < timeType.start() or timeInInt > timeType.end():
                        errorString = "[CronExpressionParserError][InvalidCronExpressionDomain] Given input [{input}] is invalid for time type [{timeType}]".format(input=input, timeType=timeType.displayString())
                        raise Exception(errorString)

        elif input.find("-") != -1:
            timeRange = input.split("-")

            try:
                start, end = int(timeRange[0]), int(timeRange[-1])
            except:
                errorString = "[CronExpressionParser][IntValueParseFailedDomain] Given input [{input}] is invalid for time type [{timeType}]".format(input=input, timeType=timeType.displayString())
                raise Exception(errorString)
            else:
                if start > end or start < timeType.start() or end > timeType.end():
                    errorString = "[CronExpressionParser][InvalidCronExpressionDomain] Given input [{input}] is invalid for time type [{timeType}]".format(input=input, timeType=timeType.displayString())
                    raise Exception(errorString)

                arr = self.__getTimeArrayWithRange(start, end)

        elif input.find("/") != -1:
            startAndInterval = input.split("/")

            try:
                if startAndInterval[0] == "*":
                    start = timeType.start()
                else:
                    start = int(startAndInterval[0])

                interval = int(startAndInterval[1])
            except:
                errorString = "[CronExpressionParser][IntValueParseFailedDomain] Given input [{input}] is invalid for time type [{timeType}]".format(input=input, timeType=timeType.displayString())
                raise Exception(errorString)
            else:
                arr = self.__getTimeArrayWithRange(start, timeType.end(), interval)

        elif input.find("*") != -1:
            if len(input) > 1:
                errorString = "[CronExpressionParser][InvalidCronExpressionDomain] Given input [{input}] is invalid for time type [{timeType}]".format(input=input, timeType=timeType.displayString())
                raise Exception(errorString)

            arr = self.__getTimeArrayWithRange(timeType.start(), timeType.end(), timeType.unit())

        else:
            try:
                timeInInt = int(input)
            except:
                errorString = "[CronExpressionParser][IntValueParseFailedDomain] Given input [{input}] is invalid for time type [{timeType}]".format(input=input, timeType=timeType.displayString())
                raise Exception(errorString)
            else:
                if int(input) < timeType.start() or int(input) > timeType.end():
                    errorString = "[CronExpressionParser][InvalidCronExpressionDomain] Given input [{input}] is invalid for time type [{timeType}]".format(input=input, timeType=timeType.displayString())
                    raise Exception(errorString)

                arr = [input]

        formattedLine = self.__getFormattedLine(timeType.displayString(), " ".join(arr))

        return formattedLine


    # List the times for firing the command based on the start time, end time and the interval.
    # Inputs:
    #   `start`     - An int value of the start time.
    #   `end`      - An int value of the end time.
    #   `interval`  - An optional int value of the interval. Default value is 1.
    # Output: A list of times for firing the command.
    def __getTimeArrayWithRange(self, start, end, interval=1):
        arr = []

        curr = start
        while curr <= end:
            arr.append(str(curr))
            curr += interval

        return arr


    # Get the formatted line for a field.
    # Inputs:
    #   `fieldName`     - A string of the field name.
    #   `fieldContent`  - A string of the field content.
    # Output: A formatted string.
    def __getFormattedLine(self, fieldName, fieldContent):

        return fieldName.ljust(14, " ") + " " + fieldContent
