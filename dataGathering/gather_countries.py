import requests
from bs4 import BeautifulSoup
import json
import unicodedata
import re

from utils import resource_path


def fetch_countries():
    url = "https://www.worldometers.info/geography/alphabetical-list-of-countries/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    countries = {}

    # Find the table containing the list of countries
    rows = soup.select("table.table tbody tr")

    for row in rows:
        country = row.select_one("td:nth-child(2)").get_text().strip()
        primary_name, alt_names = clean_country_name(country)
        add_country_to_dict(countries, primary_name)
        for alt_name in alt_names:
            add_country_to_dict(countries, alt_name)

    return countries


def clean_country_name(name):
    # Extract text within parentheses as alternative names
    alt_names = re.findall(r'\(([^)]+)\)', name)
    # Remove text within parentheses
    primary_name = re.sub(r'\(.*?\)', '', name).strip()
    # Normalize all names
    primary_name = clean_and_normalize(primary_name)
    alt_names = [clean_and_normalize(alt) for alt in alt_names]
    return primary_name, alt_names


def clean_and_normalize(text):
    # Normalize text and remove special characters
    text = unicodedata.normalize('NFKD', text)
    return re.sub(r'[^a-zA-Z\s]', '', text).strip()


def add_country_to_dict(countries, country):
    if country:
        first_letter = country[0].upper()
        countries.setdefault(first_letter, []).append(country.lower())


def save_countries_to_file(countries, filename=resource_path('backupData/countries.json')):
    with open(filename, 'w') as file:
        json.dump(countries, file, indent=4)


def gather_countries():
    countries = fetch_countries()
    save_countries_to_file(countries)


if __name__ == "__main__":
    gather_countries()
