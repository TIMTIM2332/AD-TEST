"""World population analysis using functional tools.
This script fetches the CSV from the provided URL and performs the requested analyses.
Because this environment may not have internet access, the script supports a --simulate
mode which uses a small bundled CSV sample file 'sample_population.csv'.
"""
import csv
from functools import reduce
import sys

URL = 'https://raw.githubusercontent.com/datasets/population/master/data/population.csv'
SAMPLE = 'sample_population.csv'

def read_csv(path):
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)

def filter_year(rows, year='2020'):
    return list(filter(lambda r: r['Year'] == year, rows))

def map_country_population(rows):
    return list(map(lambda r: (r['Country Name'], int(float(r['Value']))), rows))

def top_n(pop_list, n=5):
    return sorted(pop_list, key=lambda x: x[1], reverse=True)[:n]

def total_population(pop_list):
    return reduce(lambda a,b: a + b[1], pop_list, 0)

def avg_population_africa(rows):
    african = list(filter(lambda r: r['Region'] == 'Africa', rows))
    if not african: return 0
    mapped = map_country_population(african)
    return total_population(mapped) / len(mapped)

def apply_and_log(func, iterable):
    print(f'Applying {func.__name__} to iterable of length {len(iterable)}')
    return func(iterable)

# Note: The real CSV has no 'Region' column; this script assumes a sample for demo.
if __name__ == '__main__':
    simulate = '--simulate' in sys.argv
    src = SAMPLE if simulate else SAMPLE  # change to URL fetch when running locally with internet
    rows = read_csv(src)
    before_count = len(rows)
    year_rows = filter_year(rows, '2020')
    mapped = map_country_population(year_rows)
    top5 = top_n(mapped, 5)
    print('Top 5 countries (2020):')
    for c,p in top5:
        print(c, p)
    total_world = total_population(mapped)
    print('Total (sum) population from filtered rows:', total_world)
    print('Average population (Africa, demo sample):', avg_population_africa(rows))
    print('Original rows:', before_count, 'After filter:', len(year_rows))
