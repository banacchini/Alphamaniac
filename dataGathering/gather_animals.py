import requests
from bs4 import BeautifulSoup
import json
from unidecode import unidecode
from utils import resource_path


def gather_animals():
    url = "https://a-z-animals.com/animals/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'html.parser')
    animals = []
    ul_elements = soup.find_all('ul', class_='list-unstyled row')
    for ul in ul_elements:
        li_elements = ul.find_all('li')
        for li in li_elements:
            a_tag = li.find('a')
            if a_tag:
                animal_name = a_tag.get_text().strip().lower()
                if animal_name and animal_name[0].isalpha():
                    ascii_animal_name = unidecode(animal_name)
                    if '(' in ascii_animal_name and ')' in ascii_animal_name:
                        base_name, parenthesis_name = ascii_animal_name.split('(', 1)
                        base_name = base_name.strip()
                        parenthesis_name = parenthesis_name.replace(')', '').strip()
                        animals.append(base_name)
                        animals.append(parenthesis_name)
                    else:
                        animals.append(ascii_animal_name)
    animal_dict = {}
    for animal in animals:
        first_letter = animal[0].upper()
        if first_letter not in animal_dict:
            animal_dict[first_letter] = []
        animal_dict[first_letter].append(animal)
    with open(resource_path('backupData/animals.json'), 'w', encoding='ascii') as json_file:
        json.dump(animal_dict, json_file, indent=4, ensure_ascii=True)


if __name__ == "__main__":
    gather_animals()
