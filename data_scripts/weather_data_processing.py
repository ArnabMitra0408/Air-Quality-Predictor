import pandas as pd
import json
from datetime import datetime
from coordinates import states
import os
from dotenv import load_dotenv
load_dotenv()


json_data_path=os.getenv('json_weather_data_path')
csv_folder_path=os.getenv('csv_weather_folder_path')
csv_data_path=os.getenv('csv_weather_data_path')

if __name__=='__main__':

    print('******************Converting To DataFrame Now*********************')
    temperature = []
    humidity = []
    pressure = []
    wind_speed = []
    timestamp = []
    state_name=[]
    timestamp=[]
    if os.path.exists(csv_folder_path):
        print(f"{csv_folder_path} Folder Path Exists. Starting Data Parsing Now")
    else:
        os.makedirs(csv_folder_path)
        print(f"{csv_folder_path} Folder Created: Starting Data Parsing")
        
    for state in states:
        print(f"parsing {state} data")
        read_file_path=json_data_path+state+'.json'
        with open(read_file_path) as f:
            data = json.load(f)
            for i in range(len(data['list'])):
                temperature.append(data['list'][i]['main']['temp'])
                humidity.append(data['list'][i]['main']['humidity'])
                pressure.append(data['list'][i]['main']['pressure'])
                wind_speed.append(data['list'][i]['wind']['speed'])
                temp_date=int(data['list'][i]['dt'])
                date=datetime.utcfromtimestamp(temp_date).strftime('%Y-%m-%d %H:%M:%S')
                timestamp.append(date)
                state_name.append(state)
            del data


    weather_data = pd.DataFrame({
        'temperature': temperature,
        'humidity': humidity,
        'pressure': pressure,
        'wind_speed': wind_speed,
        'state': state_name,
        'timestamp': timestamp,
    })
    weather_data.to_csv(csv_data_path)