"""
project_3.py: třetí projekt do Engeto Online Python Akademie
author: Karel Černý
email: karel.cerny@t-mobile.cz
discord: charliebalck
"""
from requests import get
from bs4 import BeautifulSoup
import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "-u", "--url", type=str, help="url okresu", default="https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=1https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=1"
)
parser.add_argument(
    "-f", "--file", type=str, help="název csv souboru", default="volby17.csv"
)

def get_soup(str_url: str) -> BeautifulSoup:
    return BeautifulSoup(get(str_url).text, "html.parser")

def villages(soup: BeautifulSoup) -> dict:
    dict_village = {}
    for t in soup.find_all("table"):
        for x in t.find_all("tr")[2::]:
            try:
                dict_village[x.find_all("td")[1].text] = f"https://volby.cz/pls/ps2017nss/{x.find_all("td")[0].find("a", href=True)["href"]}"
            except:
                continue
    return dict_village

def village_code(str_code: str) -> str:
    str_code = str_code[str_code.index("obec=") + 5:str_code.index("vyber=") - 2]
    return str_code

def votes(soup: BeautifulSoup, dict_data: dict) -> dict:
    dict_data["registred"] = str(soup.find_all("table")[0].find_all("tr")[2].find_all("td")[3].text).replace(u"\xa0", "")
    dict_data["envelopes"] = str(soup.find_all("table")[0].find_all("tr")[2].find_all("td")[4].text).replace(u"\xa0", "")
    dict_data["valid"] = str(soup.find_all("table")[0].find_all("tr")[2].find_all("td")[7].text).replace(u"\xa0", "")
    return dict_data

def parties(soup: BeautifulSoup, dict_data: dict) -> dict:
    for tab in soup.find_all("table")[1::]:
        for tr in tab.find_all("tr")[2::]:
            try:
                dict_data[str(tr.find_all("td")[1].text).replace(",", " ")] = str(tr.find_all("td")[2].text).replace(u"\xa0", "")
            except:
                continue
    return dict_data

def csv_writer(str_filename: str, lst_data: list):
    with open(str_filename, "w", newline="", encoding="UTF-8") as csvfile:
        lst_header = []
        for h in lst_data[0]:
            lst_header.append(h)
        fieldnames: list[str] = lst_header
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for x in lst_data:
            writer.writerow(x)

def main():
    args = parser.parse_args()
    str_url = args.url
    str_filename = args.file
    print(f"Stahuji data u url: {str_url}")
    dict_village = villages(get_soup(str_url))
    lst_data = []
    for x in dict_village:
        dict_data = {}
        dict_data["code"] = village_code(dict_village[x])
        dict_data["location"] = x
        votes(get_soup(dict_village[x]), dict_data)
        parties(get_soup(dict_village[x]), dict_data)
        lst_data.append(dict_data)
    print(f"Ukládám stažená data do souboru: {str_filename}")
    csv_writer(str_filename, lst_data)
    print("Ukončuji progam")

if __name__ == '__main__':
    main()