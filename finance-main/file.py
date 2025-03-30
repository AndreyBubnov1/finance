import csv

fieldnames = ["chat_id", "date", "type", "category", "amount"]
data = {
    "chat_id":5941892004,
    "date": "30.03.2025",
    "type": "Доход",
    "category":"gift_income",
    "amount": 123
}
#with open("database.csv", "a", encoding="utf-8") as file:
#   writer = csv.DictWriter(file, fieldnames=fieldnames)
#   writer.writerow(data)


with open("database.csv", "r", encoding="utf-8") as file:
    data = []
    reader =  csv.DictReader(file)
    for row in reader:
        data.append(row)

print(data)