import psycopg2
import csv
cur = conn.cursor()

conn = psycopg2.connect("dbname=template1 user=paulipotter")
cur.execute(" CREATE TABLE test (idserial PRIMARYKEY, numinteger, data);")
cur.execute(" INSERT INTO test (num, data) VALUES (%s,%s)", (100, "abcdef"))
with open('file.csv') as csv_file:
    rw = csv.reader(csv_file, delimeter=',', quotechar)
    rw = csv.reader(csv_file, delimeter=',')
    rw.next()
    for row in read_csv:
        cur.execute("Insert into test (num,data)",row)


# print(cur.fetchone())



#Make the changes to the database persistent
conn.commit()

#Close communication with the database
cur.close()
conn.close()
