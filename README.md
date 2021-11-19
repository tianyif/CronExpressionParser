# Cron Expression Parser Script

## Introduction

This project develops a Python script which parses a cron command and expands each field to show the times at which it will run.

## How To Use

The usage of this Python script is very simple with these two steps:
1. Navigate to the root directory `CronExpressionParser` of this project.
2. Run command
``python run.py "<your-cron-expression-command>"``. 

For example, run the script with the command:
```
$ python run.py "*/15 0 1,15 * 1-5 /usr/bin/find"
```
Then the output of the script will be:
```
minute         0 15 30 45
hour           0
day of month   1 15
month          1 2 3 4 5 6 7 8 9 10 11 12
day of week    1 2 3 4 5
command        /usr/bin/find
```

## TODOs
There are still couple of things needed to be added into this project, they are:
1. Exception handling for more edge cases. Currently this project only handles these two exceptions:
   * The components in the cron expression expected to be "integer-like" cannot be converted to an integer. For example, `abc` in
   `*/15 abc 1,15 * 1-5 /usr/bin/find` cannot be converted to an integer for `hour` field.
   * The components in the cron expression expected to be "integer-like" can be converted to an integer, 
   but that integer falls beyond the valid range of that time type.
   For example, `40` in `*/15 0 40 * 1-5 /usr/bin/find` is beyond the range of `day of month` field, which is in `[1, 31]`.
   * The components in the cron expression representing a range of time by `a-b`, but the start time is larger than the end time (`a>b`).
   For example, `5-3` in `*/15 0 40 * 5-3 /usr/bin/find` is not a valid range for the field `day of week`.
2. Add more tests for `CronExpressionParser` and `TimeType`.
3. Support for more cron operators. Currently it only supports `,`, `-`, `/` and `*`.

## Reference
* What is Cron Expression? - https://en.wikipedia.org/wiki/Cron




