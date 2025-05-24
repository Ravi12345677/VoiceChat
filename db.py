import sqlite3

conn = sqlite3.connect("rk.db")
cursor = conn.cursor()

# query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primayr key, name VARCHAR(100), path VARCHAR(1000))"
# cursor.execute(query)

# query = "INSERT INTO sys_command VALUES (null, 'one note', 'C:\\Program Files\\Microsoft Office\\root\\Office16\\ONENOTE.exe')"
# cursor.execute(query)
# conn.commit()

# query = "DELETE FROM sys_command where name = canva"
# cursor.execute(query)
# conn.commit()

# query = "CREATE TABLE IF NOT EXISTS web_command(id integer primayr key, name VARCHAR(100), url VARCHAR(1000))"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null, 'canva', 'https://www.canava.com/')"
# cursor.execute(query)
# conn.commit()

app_name = "one note"
cursor.execute('SELECT path FROM sys_command WHERE name IN (?)',(app_name,))
results = cursor.fetchall()
print(results)