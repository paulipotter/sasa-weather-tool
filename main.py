import psycopg2
import csv

conn = psycopg2.connect("dbname=template1 user=postgres")
cur = conn.cursor()

cur.execute(''' CREATE TABLE testcol 
            (DIR varchar (50),SPD varchar (50), GUS varchar (50), CLG varchar (50), SKC varchar (50), L varchar (50), 
            M varchar (50), H varchar(50), VSB varchar(50), TEMP varchar(50), DEWP varchar(50), SLP varchar(50),
            ALT varchar(50), STP varchar(50), MAX varchar(50), MIN varchar(50), PCP01 varchar(50), PCP06 varchar(50)
            PCP24 varchar(50), PCPXX varchar(50), SD)
            
                VALUES
                (%s, %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s, %s);''')

print("Opening CSV...")

with open('file.csv') as csv_file:
    rw = csv.reader(csv_file)
    for row in rw:
        print (row)
        cur.execute(''' Insert into test 
                        (DIR,SPD,GUS,CLG,SKC,L,M,H,
                        VSB,TEMP,DEWP,SLP,ALT,STP,
                        MAX,MIN,PCP01,PCP06,PCP24,PCPXX,SD)
                        VALUES
                        (%s, %s, %s, %s, %s, %s, %s,
                        %s, %s, %s, %s, %s, %s, %s,
                        %s, %s, %s, %s, %s, %s, %s);''', 
                       row)
                    

# print(cur.fetchone())



# Make the changes to the database persistent
conn.commit()

# Close communication with the database
cur.close()
conn.close()
print("Database connection is closed")
