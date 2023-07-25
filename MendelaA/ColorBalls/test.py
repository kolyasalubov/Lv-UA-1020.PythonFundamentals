import sqlite3

def db():
    #Підключаємося до бази
    conn = sqlite3.connect('db.db')
    #Отриуємо курсор
    cursor = conn.cursor()

    #Створюємо таблицю

    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS "results" (
                    "id"	INTEGER NOT NULL UNIQUE,
                    "nick_name"	TEXT NOT NULL,
                    "scores"	INTEGER NOT NULL,
                    "mis_clisk"	INTEGER NOT NULL,
                    PRIMARY KEY("id" AUTOINCREMENT));
                    ''')
    
    #Отримуємо дані топ гравці
    #cursor.execute('SELECT nick_name, max(scores) FROM results')
    cursor.execute('SELECT * FROM results')
    result = cursor.fetchall()
    print(result, type(result))

db()

def db_add():
    global points, mis_click
    with sqlite3.connect('db.db') as conn:
        conn = sqlite3.connect('db.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO results ("nick_name", "scores", "mis_clisk") VALUES (?, ?, ?)',
                    ('bob2',2, 3))
        conn.commit()
db_add()