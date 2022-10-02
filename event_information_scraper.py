from os import times
import re
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
            eventIDs = html.find_all("tr", class_="clickable-row")

            print(tournName)
            data += f"\n{tournName}\n"
            for event in eventIDs:
                event = str(event)
                ID = str(re.search('id="ev_[A-Z0-9]*"', event).group())[7:-1]
                timeStart = str(re.search("<td>[0-9]*:[0-9]* [A-Z]M", event).group())[4:]
                eventName = str(re.search("<strong>.*</strong>", event).group())
                eventName = str(re.search("[A-Z].*     ", eventName).group()).strip()[:-86]
                eventName = eventName.replace("   ", " ")
                timeEnd = str(re.search("Finished at [0-9]*:[0-9]* [A-Z]M", event).group())
                numCompetitors = str(re.search("([0-9]* competitors)", event).group())
                
                data += f"{line}\n{eventName} {timeStart}-{timeEnd}  {numCompetitors}\n{ID}\n\n"

        except Exception as e:
            pass
            # data += str(e) + line + "\n"

with open("FTL_basic_tournament_event_info.txt", "w") as f:
    f.write(data)
f.close()
