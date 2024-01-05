import sqlite3
conn = sqlite3.connect('first.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT,
col_1 TEXT, col_2 TEXT)''')
cursor.execute('''INSERT INTO tab_1(col_1, col_2) VALUES('black', 'red') ''')
conn.commit()
cursor.execute('''INSERT INTO tab_1(col_1, col_2) VALUES('white', 'blue')''')
conn.commit()
cursor.execute(('''INSERT INTO tab_1(col_1, col_2) VALUES('green', 'yellow')'''))
conn.commit()
cursor.execute('''DELETE FROM tab_1 WHERE id=2''')
conn.commit()
cursor.execute('''UPDATE tab_1 SET col_1='hello', col_2='world' WHERE id=3''')
conn.commit()
with open('task_5.txt', 'w', encoding='utf-8') as f:
    for item in cursor.fetchall():
        f.write(f'{item}{item[1]}')




data = [1, 26, 34, 'fafaf', 47, 'sdfsdfh', 'sgdfg', 5557]
con = sqlite3.connect('hw.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS txt_tab(id INTEGER PRIMARY KEY AUTOINCREMENT, t TEXT) ''')
cur.execute('''CREATE TABLE IF NOT EXISTS num_tab(id INTEGER PRIMARY KEY AUTOINCREMENT, i INTEGER)''')
con.commit()
for item in data:
    if type(item) == str:
        word_len = len(item)
        cur.execute('''INSERT INTO txt_tab(t) VALUES(?)''', (item,))
        cur.execute('''INSERT INTO num_tab(i) VALUES(?)''', (word_len,))
        con.commit()
    elif type(item) == int:
        if item % 2 == 0:
            cur.execute('''INSERT INTO num_tab(i) VALUES(?)''', (item,))
            con.commit()
        elif item % 2 != 0:
            cur.execute('''INSERT INTO txt_tab(t) VALUES(?)''', ('Odd',))
            con.commit()
cur.execute('SELECT COUNT(*) FROM num_tab')
items_count = cur.fetchone()[0]
if items_count > 5:
    cur.execute("""DELETE FROM txt_tab WHERE id=1""")
    con.commit()
else:
    cur.execute("""UPDATE txt_tab SET t='hello' WHERE id=1 """)
    con.commit()

