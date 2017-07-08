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


def skip_first(seq, n):
    for i, item in enumerate(seq):
        if i == 1:
            date = datetime(to_int(item[1][:4]), to_int(item[1][4:6]), to_int(item[1][6:8]), to_int(item[1][8:]), 30, 00)
            date = timezone('US/Central').localize(date)
            date = date.strftime("%Y-%m-%s %H:%M:%S %Z%z")
        if i >= n:
            yield item


with open('weather-info.csv') as csv_file:
    rw = csv.reader(csv_file)
    next(csv_file)
    for row in skip_first(rw, 3):
        new_row = ([date] + row)
        cur.execute(""" INSERT INTO testone
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
                        %s, %s);""", new_row) 


# Make the changes to the database persistent
conn.commit()

# Close communication with the database
cur.close()
conn.close()

