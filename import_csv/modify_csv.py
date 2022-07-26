import sqlite3, csv
import os
import pandas as pd
import glob

# merge all csv files to one csv file
files = os.path.join(os.path.dirname(__file__), "2021*.csv")
files = glob.glob(files)
df = pd.concat(map(pd.read_csv, files), ignore_index=True)
df.to_csv(os.path.join(os.path.dirname(__file__), "all.csv"))

# filter journey with duration less than 10s or distance less than 10m
source_file_path = os.path.join(os.path.dirname(__file__), "all.csv")
target_file_path = os.path.join(os.path.dirname(__file__), "filtered.csv")

with open(source_file_path, 'r', encoding="utf-8-sig") as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open(target_file_path, 'w') as new_file:
        fieldnames = ['', 'Departure','Return','Departure station id','Departure station name','Return station id','Return station name','Covered distance (m)','Duration (sec.)']

        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter=",")

        for line in csv_reader: 
            if int(line['Duration (sec.)']) > 10 and float(line['Covered distance (m)']) > 10:
                csv_writer.writerow(line)
              