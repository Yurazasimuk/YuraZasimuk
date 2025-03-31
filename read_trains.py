import sqlite3

conn = sqlite3.connect("../../AppData/Roaming/JetBrains/PyCharmCE2023.3/scratches/trains.db")
cursor = conn.cursor()


cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("📌 Таблиці у базі даних:")
for table in tables:
    print(table[0])

print("\n🔍 Перевіряємо дані у таблиці 'trains':")


cursor.execute("SELECT * FROM trains")
rows = cursor.fetchall()

if rows:
    print("📝 Дані у таблиці:")
    for row in rows:
        print(row)
else:
    print("⚠️ Таблиця порожня!")

conn.close()
