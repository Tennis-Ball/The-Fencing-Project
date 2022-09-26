# Scrapes fencingtimelive for past tournament results data

# date: location: tournamentname: event:
# ["start:stop:size",[name by initial seed], [name by PRs], [name by FRs]]

# date: location: tournamentname: event: fencername:




# What would be interesting??
# Distribution of fencing scores, also by age, region, rating, etc.
# Percentage of timed out bouts based on age, region, rating, etc.
# history of historically dominant/recessive fencers vs. each other
# average length of event based on event and size
# ^ all above by country/club
import requests


r = requests.get("fencingtimelive.com")

