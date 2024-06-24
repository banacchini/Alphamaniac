import pandas as pd
import json

from utils import resource_path


def gather_cities():
    cities_data = pd.read_csv(resource_path('dataGathering/worldcities.csv'))
    cities = {}

    for index, row in cities_data.iterrows():
        city = row['city_ascii']
        if pd.isna(city):
            continue  # Skip NaN values
        first_letter = city[0].upper()
        if first_letter not in cities:
            cities[first_letter] = []
        cities[first_letter].append(city.lower())

    with open(resource_path('backupData/cities.json'), 'w') as file:
        json.dump(cities, file, indent=4)


if __name__ == "__main__":
    gather_cities()
