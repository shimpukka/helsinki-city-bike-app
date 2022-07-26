# Open DB connection and import data from csv
import sqlite3, csv
import os
import re

connection = sqlite3.connect('db.sqlite3')
cursor = connection.cursor()
data_file_path = os.path.join(os.path.dirname(__file__), "filtered.csv")

# clear database before importing
# cursor.execute("DELETE FROM import_csv_journey")
# connection.commit()

with open(data_file_path, 'r') as file:
    csv_reader = csv.reader(file)
    index = 0
    for line in csv_reader:
        # For now, import only part of the data
        if index < 100:
            cursor.execute("INSERT INTO journey_model_journey VALUES (?,?,?,?,?,?,?,?,?)", line)
            connection.commit()
        index += 1
connection.close()
print("Import completed")