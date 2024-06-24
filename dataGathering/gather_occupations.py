import requests
from bs4 import BeautifulSoup
import json

from utils import resource_path

def gather_occupations():
    # URL of the webpage to scrape
    url = "https://list.fandom.com/wiki/List_of_occupations"

    # Send a request to fetch the HTML content of the webpage
    response = requests.get(url)
    response.raise_for_status()  # Check if the request was successful

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the main content div that contains the list of occupations
    content_div = soup.find('div', class_='mw-parser-output')

    # Extract all the occupation names
    occupations = []
    for li in content_div.find_all('li'):
        occupation = li.get_text().strip().lower()
        if occupation and occupation[0].isalpha():
            occupations.append(occupation)

    # Create a dictionary where the key is the first letter of each occupation
    occupation_dict = {}
    for occupation in occupations:
        first_letter = occupation[0].upper()
        if first_letter not in occupation_dict:
            occupation_dict[first_letter] = []
        occupation_dict[first_letter].append(occupation)

    # Save the dictionary to a JSON file
    with open(resource_path('backupData/occupations.json'), 'w') as json_file:
        json.dump(occupation_dict, json_file, indent=4)


if __name__ == "__main__":
    gather_occupations()