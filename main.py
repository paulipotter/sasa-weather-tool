import psycopg2

conn = psycopg2.connect("dbname= user=")

cur = conn.cursor()
