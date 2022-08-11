# Open DB connection and import data from csv
import sqlite3, csv
import os
import re

connection = sqlite3.connect('db.sqlite3')
cursor = connection.cursor()
data_file_path = os.path.join(os.path.dirname(__file__), "filtered.csv")
station_file_path = os.path.join(os.path.dirname(__file__), "stations.csv")

# clear database before importing
cursor.execute("DELETE FROM journey_model_journey")
cursor.execute("DELETE FROM journey_model_station")
connection.commit()

# Import journeys
with open(data_file_path, 'r') as file:
    csv_reader = csv.reader(file)

    for line in csv_reader:
        # print(line)
        cursor.execute("INSERT INTO journey_model_journey VALUES (?,?,?,?,?,?,?,?,?)", line)
        connection.commit()

print('Journey imported')

# Import stations
with open(station_file_path, 'r') as station_csv:
    station_csv_reader = csv.reader(station_csv)
    
    j = 0
    for line in station_csv_reader:
        
        if (j > 0):
            # cursor.execute("INSERT OR IGNORE INTO journey_model_station VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)", line)
            cursor.execute("INSERT INTO journey_model_station VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)", line)
            connection.commit()
        j += 1
        

connection.close()
print("Import completed")