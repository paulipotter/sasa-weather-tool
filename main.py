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
    new_list = []
    print(row)
#    for i in range(len(row)):
#        if i == 1:
    date = datetime(to_int(row[1][:4]), to_int(row[1][4:6]), to_int(row[1][6:8]), to_int(row[1][8:10]), 30, 00)
#    print(date)
    new_list.insert(0,date)
    for i in range(4,len(row)):
        if row[i] == '*':
            new_list.append(0)
#        elif row[i] == '0.00':
#            new_list.append('0')        
        else:
            new_list.append(row[i])
            print(type(row[i]), row[i])
            #date = timezone('US/Central').localize(date)
  #      if i < 4:
  #          del row[i]
#        elif i >= 4:
#            yield row
    return new_list
columns = ['TEMP','MIN','MAX','DEWP',
                        'DIR','SPD','GUS','PCPXX',
                        'PCP06','PCP24','SD','SKC','CLG',
                        'L','M','H','SLP','STP',
                        'ALT','VSB']
with open('weather-info.csv') as csv_file:
    rw = csv.reader(csv_file)
    next(csv_file)
    testlist = []
    for row in rw:
        data = list(format_list(row))

        cur.execute(  """ INSERT INTO testone
                        (yrmodahrmn,TEMP,MIN,MAX,DEWP,
                        DIR,SPD,GUS,PCP01,PCPXX,
                        PCP06,PCP24,SD,SKC,CLG,
                        L,M,H,SLP,STP,
                        ALT,VSB)
                    VALUES
                       (%s, %s, %s, %s, %s,
                        %s, %s, %s, %s, %s,
                        %s, %s, %s, %s, %s,
                        %s, %s, %s, %s, %s,
                        %s, %s)""", data)
    for item in columns:
        null_if_zero = 'UPDATE testone SET {0}=NULL WHERE {0}=0'.format(item)
        cur.execute(null_if_zero)
# Make the changes to the database persistent
conn.commit()

# Close communication with the database
cur.close()
conn.close()

