# Requests
import requests
import csv
# BeautifulSoup
from bs4 import BeautifulSoup

# url to scrape
url = "https://www.gov.uk/search/news-and-communications"

page = requests.get(url)

# See html source
# print(page.content)

# Turn HTML to BeautifulSoup object
soup = BeautifulSoup(page.content, 'html.parser')

# Get all titles with gem-c-document-list__item-title class
bs_titles = soup.find_all("a", class_="gem-c-document-list__item-title")

# Get all descriptions with class gem-c-document-list__item-description
bs_descriptions = soup.find_all("p", class_="gem-c-document-list__item-description")

# Save titles and descriptions as lists of strings
titles = []
for title in bs_titles:
    titles.append(title.string)

descriptions = []
for desc in bs_descriptions:
    descriptions.append(desc.string)

# write data to a csv file
headers = ["title", "description"]

with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(headers)
    for i in range(len(titles)):
        row = [titles[i], descriptions[i]]
        writer.writerow(row)


