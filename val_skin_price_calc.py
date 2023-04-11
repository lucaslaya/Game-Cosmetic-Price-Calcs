import requests
from bs4 import BeautifulSoup

wiki_url = 'https://valorant.fandom.com/wiki/Weapon_Skins'
html = requests.get(wiki_url).text
soup = BeautifulSoup(html, 'html.parser')

table_tabs = soup.find_all("div", "wds-tab__content")

normal_skins = table_tabs[0]
legacy_skins = table_tabs[3]

normal_skins_rows = normal_skins.find_all("tr")
normal_skins_rows.pop(0)

all_prices = []
for row in normal_skins_rows:
    cols = row.find_all("td")

    temp = cols[4].get("data-sort-value")
    all_prices.append(float(temp))

print("Current cost to buy all non-legacy skins")
print("Valorant Point: ", int(sum(all_prices)))
print("USD (Conversion is 1VP:$0.01050, found online): $", (sum(all_prices) * 0.010505))