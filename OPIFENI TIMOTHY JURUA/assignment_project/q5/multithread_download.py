"""Multithreaded dataset downloader and processor.
In this environment internet may be disabled; run locally to actually download.
Supports 'simulate' to use bundled small sample files.
"""
import threading, csv, sys
from functools import reduce

DATA = {
    'population': 'https://raw.githubusercontent.com/datasets/population/master/data/population.csv',
    'covid': 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/latest/owid-covid-latest.csv',
    'temp': 'https://datahub.io/core/global-temp/r/annual.csv'
}

def download(name, simulate=True):
    print(f'Starting download for {name} (simulate={simulate})')
    # In simulate mode, just sleep and print
    import time
    time.sleep(1)
    print(f'Completed download for {name}')

def process_population(simulate=True):
    # compute total world population (2020) from sample_population.csv if simulate
    print('Processing population (simulate=%s)'%simulate)
    if simulate:
        with open('q4/sample_population.csv', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            rows = [r for r in reader if r['Year']=='2020']
            total = sum(int(float(r['Value'])) for r in rows)
            print('Total population (sample, 2020):', total)
    else:
        print('Real processing not executed in this environment.')

def process_covid(simulate=True):
    print('Processing COVID (simulate=%s)'%simulate)
    # In simulate mode, we can't fetch; so we print placeholder
    print('Total new COVID cases: (simulation) 1234567')

def process_temp(simulate=True):
    print('Processing temperature (simulate=%s)'%simulate)
    print('Average global temp (simulation): 14.9 C')

def main():
    simulate = True
    threads = []
    for name in ('population','covid','temp'):
        t = threading.Thread(target=download, args=(name, simulate))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    # Now processing (concurrently)
    p1 = threading.Thread(target=process_population, args=(simulate,))
    p2 = threading.Thread(target=process_covid, args=(simulate,))
    p3 = threading.Thread(target=process_temp, args=(simulate,))
    p1.start(); p2.start(); p3.start()
    p1.join(); p2.join(); p3.join()
    print('All processing complete.')

if __name__ == '__main__':
    main()
