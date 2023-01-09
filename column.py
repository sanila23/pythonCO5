import csv

#Specify the column indices that you want to read
#Eg: Colum 0 is the first column, Column 1 is the 2nd column, etc.
columns_to_read = [0, 2]

#open the csv file and read the contents
with open('cont.csv','r')as f:
    clmn_reader = csv.reader(f)

    #iterate over the rows of the csv
    for row in clmn_reader:
        #Print the contents of the specified columns
        print([row[i] for i in columns_to_read])