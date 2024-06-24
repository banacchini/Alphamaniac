import requests
from bs4 import BeautifulSoup
import json
import unicodedata
from utils import resource_path


def fetch_sports():
    url = "https://www.topendsports.com/sport/list/index.htm"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    sports = []

    # Find the list containing sports
    content_div = soup.find("div", {"id": "content"})
    lists = content_div.find_all("ul")

    for ul in lists:
        for li in ul.find_all("li"):
            # Extract only the text within the <a> tag
            a_tag = li.find("a")
            if a_tag:
                sport_name = a_tag.get_text().strip()
                sport_name = remove_special_characters(sport_name)
                sports.append(sport_name)

    return sports


def remove_special_characters(text):
    # Normalize text and remove special characters
    normalized_text = unicodedata.normalize('NFKD', text)
    ascii_text = normalized_text.encode('ASCII', 'ignore').decode('ASCII')
    return ascii_text


def save_sports_to_file(sports, filename=resource_path('backupData/sports.json')):
    sports_dict = {}
    for sport in sports:
        if sport:  # ensure sport is not an empty string
            first_letter = sport[0].upper()
            sport = sport.lower()
            if first_letter not in sports_dict:
                sports_dict[first_letter] = []
            sports_dict[first_letter].append(sport)

    with open(filename, 'w') as json_file:
        json.dump(sports_dict, json_file, indent=4)


def gather_sports():
    sports = fetch_sports()
    save_sports_to_file(sports)


if __name__ == "__main__":
    gather_sports()
