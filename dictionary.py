import csv

# Data to be inserted
data = [{'Name': 'John', 'Age': 25, 'Country': 'United States'},
      {'Name': 'Ren', 'Age': 20, 'Country': 'South Korea'},
      {'Name': 'Sierra', 'Age': 24, 'Country': 'Australia'}]

# Write to csv file
with open('aa.csv', 'w') as csvfile:
    headernames = ['Name', 'Age', 'Country']
    csvwriter = csv.DictWriter(csvfile, fieldnames=headernames)
    csvwriter.writeheader()
    for row in data:
       csvwriter.writerow(row)

# Read from CSV file and print contents
with open('aa.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
       print(row)