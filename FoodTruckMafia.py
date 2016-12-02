import json
import requests

page = requests.get("https://inffuse-calendar2.appspot.com/api/events?calendar=c5e62u6tbl7tim98ih3un6br40@group.calendar.google.com&count=50&from=1480593600000&project=proj_RAgpzKo1sUH1SUZkEZJQW&user=user_wqFcnSSVRclUK3N6Dm0CS")
page_json = page.json()

def foodTruckMafia():
    events = page_json.get('events')
    for event in events:
      if event.get("title") == "Stoneridge Street Eats":
          trucks = event.get('description')
          break
    truck_split = trucks.splitlines()
    trucks = ""
    for truck in truck_split:
        trucks = trucks + "\t" + truck + "\n"
    return trucks[:-1]
