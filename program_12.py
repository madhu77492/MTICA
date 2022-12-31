import sqlite3 as lite
con=lite.connect('mtica.db')
cur=con.cursor()
cur.execute('''
UPDATE Cars SET Name='Mp' WHERE Id=2
''')
con.commit()
con.close()
print("Data UPDATED.")


