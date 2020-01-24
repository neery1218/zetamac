"""Mental math program."""
from collections import defaultdict
import random
import time
import uuid

import click
import pandas as pd


@click.command()
@click.option('--add/--no-add', default=True, help='enable addition questions')
@click.option('--sub/--no-sub', default=True, help='enable subtraction questions')
@click.option('--mul/--no-mul', default=True, help='enable multiplication questions')
@click.option('--div/--no-div', default=True, help='enable division questions')
@click.option('--number-range', default=(2, 100), type=(int, int), help='range of numbers')
@click.option('--duration', default=120, help='Game Length')
@click.option('--name', default='data', help='file output name')
def main(add, sub, mul, div, number_range, duration, name):
    start_time = time.time()
    d = defaultdict(list)
    operators = []

    if add:
        operators.append('+')
    if sub:
        operators.append('-')
    if mul:
        operators.append('*')
    if div:
        operators.append('/')

    while time.time() - start_time < duration:
        first_num = random.randint(number_range[0], number_range[1])
        sec_num = random.randint(number_range[0], number_range[1])
        operator = random.choice(operators)

        if (operator == '-'):
            first_num, sec_num = max(
                first_num, sec_num), min(first_num, sec_num)
        elif (operator == '/'):
            first_num *= sec_num

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

    print("Final score: {}".format(len(d['time_taken'])))
    filename = "{}-{}.csv".format(name, uuid.uuid4())
    df = pd.DataFrame.from_dict(d)
    df.to_csv(filename)


if __name__ == '__main__':
    main()
