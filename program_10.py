import sqlite3
carData=[
    (1, 'Audi', 52642),
    (2, 'Mercedes', 52643),
    (3, 'Volvo', 52644),
    (4, 'Citroen', 52646),
    (5, 'Hummer', 52645),
    (6, 'Volkswagen', 52649)
    ]
con=sqlite3.connect('mtica.db')
cur=con.cursor()
cur.execute("DROP TABLE IF EXISTS Cars")
cur.execute("CREATE TABLE Cars(Id INT,Name TEXT,Price INT)")
cur.executemany("INSERT INTO Cars VALUES(?,?,?)",carData)
con.commit()
con.close()
print("Values inserted.")
