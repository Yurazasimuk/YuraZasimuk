import sqlite3


def create_database():
    conn = sqlite3.connect("articles.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Articles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        content TEXT NOT NULL,
        author TEXT UNIQUE NOT NULL
    )
    """)

    conn.commit()
    conn.close()
    print("✅ База даних і таблиця Articles створені!")


# Функція для додавання нової статті
def add_article():
    title = input("📝 Введіть назву статті: ")
    content = input("📄 Введіть зміст статті: ")
    author = input("✍️ Введіть автора статті: ")

    conn = sqlite3.connect("articles.db")
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO Articles (title, content, author) VALUES (?, ?, ?)",
                       (title, content, author))
        conn.commit()
        print("✅ Статтю додано успішно!")
    except sqlite3.IntegrityError:
        print("❌ Помилка: автор вже існує!")

    conn.close()


# Функція для видалення статті за ID
def delete_article():
    article_id = input("🗑 Введіть ID статті для видалення: ")

    conn = sqlite3.connect("articles.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM Articles WHERE id = ?", (article_id,))
    conn.commit()

    if cursor.rowcount:
        print(f"✅ Статтю з ID {article_id} видалено.")
    else:
        print(f"❌ Статтю з ID {article_id} не знайдено.")

    conn.close()


# Функція для перегляду статті за ID
def view_article():
    article_id = input("🔍 Введіть ID статті для перегляду: ")

    conn = sqlite3.connect("articles.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Articles WHERE id = ?", (article_id,))
    article = cursor.fetchone()

    if article:
        print("\n📖 Стаття:")
        print(f"ID: {article[0]}")
        print(f"Назва: {article[1]}")
        print(f"Зміст: {article[2]}")
        print(f"Автор: {article[3]}\n")
    else:
        print("❌ Статтю не знайдено!")

    conn.close()


# Головне меню
def main():
    create_database()

    while True:
        print("\n📚 Меню:")
        print("1️⃣ Додати статтю")
        print("2️⃣ Видалити статтю")
        print("3️⃣ Переглянути статтю")
        print("4️⃣ Вихід")

        choice = input("🔹 Виберіть опцію: ")

        if choice == "1":
            add_article()
        elif choice == "2":
            delete_article()
        elif choice == "3":
            view_article()
        elif choice == "4":
            print("👋 Вихід...")
            break
        else:
            print("❌ Невірний вибір, спробуйте ще раз!")


# Запуск програми
if __name__ == "__main__":
    main()
