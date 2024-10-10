import sqlite3

conn = sqlite3.connect('data.db')

cursor = conn.cursor()

query = f"""select * from projects limit 1;"""

cursor.execute(query)

print(cursor.fetchall())

conn.close()