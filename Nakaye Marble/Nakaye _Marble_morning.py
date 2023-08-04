#What we did in class
from bs4 import BeautifulSoup
import requests

url = 'https://xeno-canto.org/'  # Corrected URL assignment
response = requests.get(url)

# Get title of the page
soup = BeautifulSoup(response.text, 'html.parser')
title = soup.find('title')
print(title)

print("********************************************************************")

import csv
import requests
from bs4 import BeautifulSoup

def extract_bird_species(url):
    response = requests.get(url)
    if response.status_code == 200:
        bird_species_data = response.json().get('recordings')
        # soup = BeautifulSoup(response.content, 'html.parser')
        # bird_species_data = []

        # for row in soup.find_all('div', class_='taxon'):
        #     species = row.find('span', class_='species').text.strip()
        #     family = row.find('span', class_='family').text.strip()

        #     bird_species_data.append({
        #         'Species': species,
        #         'Family': family
        #     })

        return bird_species_data
    else:
        print("Failed to fetch the webpage.")
        return None

def save_to_csv(data, filename):
    if data:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = list(data[0].keys())
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        print(f"Data saved to {filename} successfully.")
    else:
        print("No data to save.")

if __name__ == "__main__":
    url = "https://xeno-canto.org/api/2/recordings?query=cnt:uganda"
    bird_species_data = extract_bird_species(url)
    if bird_species_data:
        save_to_csv(bird_species_data, "bird_species.csv")


#JASON file
from bs4 import BeautifulSoup
import requests
import json

url = "https://xeno-canto.org/explore?query=grp%3Abirds&pg={}&dir=0&order=en"

# Getting the audio list and species.
audio_list = []
species_list = []
for i in range(10):
    request_result = requests.get(url.format(str(i)))
    soup = BeautifulSoup(request_result.text, "html.parser")
    links = soup.find_all("audio")
    for link in links:
        audio_list.append("https:" + link.attrs["src"])
    names = soup.find_all("span", class_="common-name")
    for name in names:
        speciesData = name.find("a")
        species_list.append(
            {"species": speciesData.text, "species_link": speciesData.attrs["href"]}
        )

# Dumping them into a json file.
with open("bird_songs.json", "+a") as file:
    json.dump({"bird_songs": audio_list, "bird_species": species_list}, file)

# Using the api.
result = requests.get("https://xeno-canto.org/api/2/recordings?query=cnt:brazil&page=5")

# Prints values from the API in json format
print(result.json())
