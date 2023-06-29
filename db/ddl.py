import sqlite3

conn = sqlite3.connect('db/database.db')

cursor = conn.cursor()

cursor.execute('alter table user add column bio text')

conn.close()