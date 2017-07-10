import psycopg2
import csv
from datetime import datetime 
from pytz import timezone
from engine import format
from constants import *

#  Connect to PostgreSQL Database
conn = psycopg2.connect("dbname=template1 user=postgres")
cur = conn.cursor()
print("connected to db")

# Open CSV File
with open(FILE_NAME) as csv_file:
    rw = csv.reader(csv_file)
    # Ignore first line of CSV File (Header)
    next(csv_file)

    #For every row in the CSV
    for row in rw:
        #Create a new list that discards the first 4 columns and reformats the date
        data = list(format_list(row))

        #Insert the new list to the corresponding table
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

    # Set Zeroes to NULL
    for item in COLUMNS:
        query = UPDATE_NULL_IF_ZERO.format(item)
        cur.execute(query)

# Make the changes to the database persistent
conn.commit()

# Close communication with the database
cur.close()
conn.close()

