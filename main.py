import psycopg2
import csv
from datetime import datetime 
from pytz import timezone

date = ""


conn = psycopg2.connect("dbname=template1 user=postgres")
cur = conn.cursor()
print("connected to db")


def to_int(list):
    return int(''.join(list))


def format_list(row):
    new_list = row[4:]
#    for i in range(len(row)):
#        if i == 1:
    date = datetime(to_int(row[1][:4]), to_int(row[1][4:6]), to_int(row[1][6:8]), to_int(row[1][8:10]), 30, 00)
    print("Processing date", date)
            #date = timezone('US/Central').localize(date)
    new_list.append(row)
  #      if i < 4:
  #          del row[i]
#        elif i >= 4:
#            yield row
    new_list.append(row)
    return new_list

with open('weather-info.csv') as csv_file:
    rw = csv.reader(csv_file)
    next(csv_file)
    testlist = []
    for row in rw:
        data = list(format_list(row))
        print(data)
        command = """ INSERT INTO testone
                        (yrmodahrmn,DIR,SPD,GUS,CLG,
                        SKC,L,M,H,VSB,
                        TEMP,DEWP,SLP,ALT,STP,
                        MAX,MIN,PCP01,PCP06,PCP24,
                        PCPXX,SD)
                    VALUES
                        (%s, %s, %s, %s, %s,
                        %s, %s, %s, %s, %s,
                        %s, %s, %s, %s, %s,
                        %s, %s, %s, %s, %s,
                        %s, %s)"""
        print(cur.mogrify(command, (data,)))
        cur.execute(cur.mogrify(command, (data,)))
# Make the changes to the database persistent
conn.commit()

# Close communication with the database
cur.close()
conn.close()

