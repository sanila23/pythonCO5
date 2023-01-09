import csv

#Open the csv file
with open('content.csv','r') as file:
     #Create a csv reader
     reader = csv.reader(file)

     #iterate over the rows of the csv file
     for row in reader:
        #Print the row as a list of strings
        print(row)