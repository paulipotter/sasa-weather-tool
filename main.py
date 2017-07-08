import psycopg2
import csv
from datetime import datetime 
from pytz import timezone

date = ""


conn = psycopg2.connect("dbname=template1 user=postgres")
cur = conn.cursor()
print("connected to db")


def skip_first(seq, n):
    for i, item in enumerate(seq):
        if i == 1:
            print(item)
            date = datetime(int(item[:4]), int(item[4:6]), int(item[6:8]), int(item[8:]), 30, 00)
            date = timezone('US/Central').localize(date)
            date = date.strftime("%Y-%m-%d %H:%M:%S %Z%z")
            print(date)
        if i >= n:
            yield item


with open('weather-info.csv') as csv_file:
    rw = csv.reader(csv_file)
    print("start of execution")
    next(csv_file)
    for row in skip_first(rw, 3):
        print (row)
        cur.execute(''' Insert into testone
                        (yrmodahrmn,DIR,SPD,GUS,CLG,SKC,L,M,H,
                        VSB,TEMP,DEWP,SLP,ALT,STP,
                        MAX,MIN,PCP01,PCP06,PCP24,PCPXX,SD)
                        Values (%s, %s, %s, %s, %s, %s, %s,
                        %s, %s, %s, %s, %s, %s, %s, %s,
                        %s, %s, %s, %s, %s,%s);''',
                    date, row)


# Make the changes to the database persistent
conn.commit()

# Close communication with the database
cur.close()
conn.close()

