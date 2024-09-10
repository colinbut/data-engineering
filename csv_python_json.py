import csv
import json

taxables = []

# parse csv file as input...
with open('taxables.csv') as csvFile:
    csvContent = csv.reader(csvFile, delimiter=",")
    for row in csvContent:
        taxable = {
            "index" : row[0],
            "item" : row[1],
            "cost" : row[2],
            "tax" : row[3],
            "total" : row[4]
        }
        # print(taxable)
        taxables.append(taxable)

# print to std out
print(json.dumps(taxables, indent=4))

# print to file
with open('taxables.json', 'w') as jsonFile:
    json.dump(taxables, jsonFile, indent=4)
    
