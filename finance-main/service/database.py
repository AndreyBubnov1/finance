from config import database_path
import csv

def write_database(data):
    with open(database_path, "w") as file:
        writer = csv.writer(file)
        writer.writerow(data.values())