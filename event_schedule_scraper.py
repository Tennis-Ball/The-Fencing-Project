import requests
from bs4 import BeautifulSoup
import time


data = ""
with open("FTL_unique_IDs.txt", "r") as f:
    for line in f:
        try:
            ID = line.strip()
            r = requests.get(f"https://fencingtimelive.com/tournaments/eventSchedule/{ID}")
            html = BeautifulSoup(str(r.text.encode("utf-8")), "html.parser")

            tournName = html.find("div", class_="tournName")
            tournName = tournName.text
            eventName = html.find("div", class_="eventName")
            eventName = eventName.text[50:].strip()[:-2]
            print(tournName + ":    " + eventName + "\n")
            data += tournName + ":    " + eventName + "\n"
        except Exception as e:
            print(e, line, "\n")
            data += str(e) + line + "\n"

with open("FTL_basic_tournament_info.txt", "w") as f:
    f.write(data)
f.close()
