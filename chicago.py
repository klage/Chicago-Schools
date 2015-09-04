import csv
with open("ho.csv",'r')as f:
    with open("Sc.csv",'r')as g:
        dict = csv.DictReader(f, delimiter=',', quotechar='"')
        dict2 = csv.DictReader (g, delimiter=',', quotechar='"')
        print (dict)
        for line in dict2:
            print(line['SCHOOL NAME'])
        for line in dict:
            print(line['NAME'])
