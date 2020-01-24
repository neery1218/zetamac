"""Mental math program."""
from collections import defaultdict
import random
import time
import uuid

import pandas as pd


def main():
    name = input("Name? ")
    duration = None

    while not isinstance(duration, int) or duration < 0:
        duration = int(input("Duration? (seconds) "))

    input("Ready? (Press any key) ")

    start_time = time.time()
    total = 0
    d = defaultdict(list)

    while time.time() - start_time < duration:
        first_num = random.randint(2, 100)
        sec_num = random.randint(2, 100)
        operator = random.choice(['+', '-'])

        expr = "{} {} {}".format(first_num, operator, sec_num)
        answer = eval(expr)
        user_input = None

        question_start_time = time.time()
        while user_input != answer:
            try:
                user_input = int(input(expr + "="))
            except Exception as e:
                print(e)
        question_end_time = time.time()

        d['time_taken'].append(question_end_time - question_start_time)
        d['time_start'].append(question_start_time)
        d['first_num'].append(first_num)
        d['operator'].append(operator)
        d['second_num'].append(sec_num)
        d['time_since_quiz_start'].append(question_start_time - start_time)

        total += 1

    print("Final score: {}".format(total))
    filename = "{}-{}.csv".format(name, uuid.uuid4())
    df = pd.DataFrame.from_dict(d)
    df.to_csv(filename)


if __name__ == '__main__':
    main()
