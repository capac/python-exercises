#! /usr/bin/env python

import re
import pandas as pd
from numpy import interp
import os
from pathlib import Path

home = os.environ['HOME']
home_dir = Path(home)
work_dir = home_dir / 'Programming/Python/python-exercises/hackerrank'

# 12/14/2012 16:00:00 Missing_19
pattern = re.compile(r'(\d{1,2}/\d{1,2}/2012)\s+(16:00:00)\s+(Missing_\d{1,2})')
missing_list = []

with open(work_dir / 'data/readings.txt', 'r') as f:
    lines = f.readlines()
    for index, line in enumerate(lines):
        # print(f'line: {line}')
        missing_item = pattern.findall(line)
        if missing_item:
            # print(f'missing_item: {missing_item}')
            date = pattern.sub(r'\1', line)
            # print(f'date: {date}')
            missing_list.append(date.rstrip())


reading_df = pd.read_csv(work_dir / 'data/readings.txt', sep=r'\s+',
                         names=['date', 'time', 'measurements'])

reading_df['date_time'] = reading_df[['date', 'time']].agg(' '.join, axis=1)
reading_df.drop(['date', 'time'], axis=1, inplace=True)
reading_df['date_time'] = pd.to_datetime(reading_df['date_time'], format=r'%m/%d/%Y %H:%M:%S')
# reading_df.set_index('date_time', inplace=True)
reading_df = reading_df[['date_time', 'measurements']]
print(reading_df.head())
print(reading_df.info())
# new_interp = interp(missing_list)

# print(f'missing_list: {missing_list}')


def calcMissing(readings):
    pass


# if __name__ == '__main__':
#     readings_count = int(input().strip())

#     readings = []

#     for _ in range(readings_count):
#         readings_item = input()
#         readings.append(readings_item)

#     calcMissing(readings)
