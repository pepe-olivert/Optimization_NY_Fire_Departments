import requests
import json
import pandas as pd


def get_min_distances(nine=9*60):

    response = requests.get("https://gitlab.com/drvicsana/cop-proyecto-2023/-/raw/main/project_data/distancias_estaciones_barrios.json")
    distances_stations_ntas_db = json.loads(response.text)
    neighbors = distances_stations_ntas_db["42 South Street"].keys() 
    neighbors_with_9_minute_station = {}
    df = pd.DataFrame(distances_stations_ntas_db).transpose()
    for elem in neighbors:
        aux = df[elem]
        flag = 0
        for v in aux:
            if v <= 540:
                flag +=1
            else:
                flag +=0

        if flag >0:neighbors_with_9_minute_station[elem]=540
        else: neighbors_with_9_minute_station[elem]=min(aux)

    return neighbors_with_9_minute_station