import sys
from cronExpressionParser import CronExpressionParser

def main(input):
    parser = CronExpressionParser()
    print(parser.parse(input))

if __name__ == "__main__":
   main(sys.argv[1])













