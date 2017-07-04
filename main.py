import psycopg2
import csv

conn = psycopg2.connect("dbname=template1 user=postgres")
cur = conn.cursor()
# cur.execute(" CREATE TABLE test ( num integer, data varchar(55));")
cur.execute(" INSERT INTO test (num, data)  VALUES (%s,%s)", (100, "abcdef"))
with open('file.csv') as csv_file:
    rw = csv.reader(csv_file)
    for row in rw:
        print (row)
        cur.execute("Insert into test (num,data) Values (%s, %s);", row)


# print(cur.fetchone())



# Make the changes to the database persistent
conn.commit()

# Close communication with the database
cur.close()
conn.close()
