import csv
with open("ho.csv",'r')as f:
    dict = csv.DictReader(f, delimiter=',', quotechar='"')
    print (dict)
    for line in dict:
        print(line['NAME'])
