from datetime import datetime
import requests

def get_historic_tr(player, timestamp):
    try:
        timestamp *= 1000
        url = "https://ch.tetr.io/api/labs/leagueflow/" + player
        data = requests.get(url)
        data = data.json()
        tr = -1
        base_timestamp = data["data"]["startTime"]
        finished = False
        ptr = 0
        while not finished:
            if (ptr == len(data["data"]["points"])):
                finished = True
            else:
                if(data["data"]["points"][ptr][0] + base_timestamp < timestamp):
                    tr = data["data"]["points"][ptr][2]
                    print(data["data"]["points"][ptr][0] + base_timestamp - timestamp)
                else:
                    finished = True
            ptr += 1

    except: 
        return -1
    finally:
        return tr
    
def get_max_tr(player):
    try:
        url = "https://ch.tetr.io/api/labs/leagueflow/" + player
        data = requests.get(url)
        data = data.json()
        max_read = -1
        for i in range(len(data["data"]["points"])):
            if(data["data"]["points"][i][2] > max_read):
                max_read = data["data"]["points"][i][2]
    except:
        return -1
    finally:
        return max_read

