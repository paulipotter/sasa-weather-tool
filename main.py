import psycopg2
import csv
date = 0
def skip_first(seq, n):
for i, item in enumerate(seq):
    if i == 1:
        print(item)
        date = datetime.strptime
    if i >= n:
        yield item

conn = psycopg2.connect("dbname=template1 user=postgres")
cur = conn.cursor()
# cur.execute(" CREATE TABLE test ( num integer, data varchar(55));")
print("connected to db")
cur.execute(" create table testone (DIR varchar(50),SPD varchar(50),GUS varchar(50),CLG varchar(50),SKC varchar(50),L varchar(50),M varchar(50),H varchar(50),VSB varchar(50),TEMP varchar(50),DEWP varchar(50),SLP varchar(50),ALT varchar(50),STP varchar(50),MAX varchar(50),MIN varchar(50),PCP01 varchar(50),PCP06 varchar(50),PCP24 varchar(50),PCPXX varchar(50),SD varchar(50));")
with open('weather-info.csv') as csv_file:
    rw = csv.reader(csv_file)
    print("start of execution")
    next(csv_file)
        for row in skip_first(rw,3):
        print (row)
        cur.execute(''' Insert into testone
                        (yrmodahrmn,DIR,SPD,GUS,CLG,SKC,L,M,H,
                        VSB,TEMP,DEWP,SLP,ALT,STP,
                        MAX,MIN,PCP01,PCP06,PCP24,PCPXX,SD") 
                        Values (%s, %s, %s, %s, %s, %s, %s, 
                        %s, %s, %s, %s, %s, %s, %s, %s, 
                        %s, %s, %s, %s, %s,%s);''',
                        row)

# print(cur.fetchone())



# Make the changes to the database persistent
conn.commit()

# Close communication with the database
cur.close()
conn.close()

#     from datetime import datetime
#     from pytz import timezone
#     line="2013052322"
#     d = datetime(int(line[:4]),int(line[4:6]),int(line[6:8]),int(line[8:]),30,00)
#      d=timezone('US/Central').localize(d)
#      print(d.strftime("%Y-%m-%d %H:%M:%S %Z%z"))
