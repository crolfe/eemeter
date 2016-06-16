import json

import requests

from bs4 import BeautifulSoup


url = "http://rredc.nrel.gov/solar/old_data/nsrdb/1991-2005/tmy3/by_USAFN.html"


def _parse_name(element):
    stripped_name = element.text.replace("\n", "").replace("\t", "").strip()
    return "".join(stripped_name).split(",")[:-1]


if __name__ == "__main__":
    soup = BeautifulSoup(requests.get(url).text)
    stations = soup.select('td .hide')

    station_data = {}
    for station_el in stations:
        station_name_el = station_el.findNext('td').findNext('td')
        station_class_el = station_name_el.findNext('td')
        station_data[station_el.text.strip()] = {
            "name": _parse_name(station_name_el),
            "state": station_name_el.text.split(",")[-1].strip(),
            "class": station_class_el.text.split()[1].strip(),
        }

    with open('tmy3_stations.json', 'w') as f:
        json.dump(station_data, f)
