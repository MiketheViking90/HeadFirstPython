import csv
from pprint import pprint
from datetime import datetime
from typing import Dict


def read_csv():
    with open('buzzers.csv') as data:
        for line in csv.DictReader(data):
            print(line)

def convert2ampm(time24: str) -> str:
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')

def read_csv_custom():
    with open('buzzers.csv') as data:
        header = data.readline()
        flights = {}
        for line in data:
            k, v = line.strip().split(',')
            flights[k] = v
    return flights

def format_dict(dict):
    formatted = {}
    for k, v in dict.items():
        formatted[convert2ampm(k)] = v.title()
    return formatted

def list_comprehension_pattern(flights: dict):
    times = []
    for time in flights.keys():
        times.append(time)

    cities = []
    for city in flights.values():
        cities.append(city)
    return times, cities


def dict_comp(flights:dict):
    return {convert2ampm(k): v.title() for k, v in flights.items() if v == 'FREEPORT'}

flights = read_csv_custom()
fflights = format_dict(flights)

times, cities = list_comprehension_pattern(flights)

times = [convert2ampm(time) for time in flights.keys()]
cities = [city.title() for city in flights.values()]

cities_set = set(fflights.values())
west_end_times = [time for time in fflights.keys() if fflights[time] == 'West End']

city_index = {}
for city in cities_set:
    city_index[city] = [time for time in fflights.keys() if fflights[time] == city]
pprint(city_index)

def rev_index(flights: Dict[str, str]) -> Dict[str, str]:
    return {city: [time for time in flights.keys() if flights[time] == city] for city in set(flights.values())}

rev = rev_index(fflights)
pprint(rev)