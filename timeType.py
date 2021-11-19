from enum import Enum

class TimeType(Enum):
    minute = 0
    hour = 1
    dayOfMonth = 2
    month = 3
    dayOfWeek = 4

    # Get the start time of the time type.
    # Output: An int value of the start time.
    def start(self):
        if self == TimeType.minute or self == TimeType.hour:
            return 0
        else:
            return 1

    # Get the end time of the time type.
    # Output: An int value of the end time.
    def end(self):
        if self == TimeType.minute or self == TimeType.hour:
            return 59
        elif self == TimeType.dayOfMonth:
            return 31
        elif self == TimeType.month:
            return 12
        else:
            return 7

    # Get the unit of the time type.
    # Output: An int value of the time unit.
    def unit(self):
        return 1

    # Get the display string of the time type.
    # Output: A string to display the time type.
    def displayString(self):
        if self == TimeType.minute:
            return "minute"
        elif self == TimeType.hour:
            return "hour"
        elif self == TimeType.dayOfMonth:
            return "day of month"
        elif self == TimeType.month:
            return "month"
        elif self == TimeType.dayOfWeek:
            return "day of week"