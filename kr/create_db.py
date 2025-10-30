import sqlite3
import os

# Создаём папку db, если нет
os.makedirs("db", exist_ok=True)

# Путь к базе
db_path = "db/q.db"

# Удаляем старую базу, если есть (безопасно)
if os.path.exists(db_path):
    try:
        os.remove(db_path)
        print(f"Старая база удалена: {db_path}")
    except Exception as e:
        print(f"Не удалось удалить старую базу: {e}")
        print("Закройте все программы, использующие q.db, и попробуйте снова.")
        exit()

# Создаём новую базу
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

print("Создаю таблицы...")

# Таблица S — секции
cursor.execute('''
CREATE TABLE S (
    sId INTEGER PRIMARY KEY,
    titleTranslation TEXT NOT NULL
)
''')

# Таблица V — стихи
cursor.execute('''
CREATE TABLE V (
    _id INTEGER PRIMARY KEY AUTOINCREMENT,
    sId INTEGER,
    vrId INTEGER,
    vr TEXT,
    FOREIGN KEY (sId) REFERENCES S(sId)
)
''')

print("Вставляю тестовые данные...")

# Данные для секций
cursor.executemany('''
INSERT INTO S (sId, titleTranslation) VALUES (?, ?)
''', [
    (1, 'Введение'),
    (2, 'Основные понятия'),
    (3, 'Заключение')
])

# Данные для стихов
cursor.executemany('''
INSERT INTO V (sId, vrId, vr) VALUES (?, ?, ?)
''', [
    (1, 1, 'Это первое предложение введения.'),
    (1, 2, 'А это второе предложение.'),
    (2, 1, 'Первое определение.'),
    (2, 2, 'Второе определение.'),
    (3, 1, 'Итог работы.')
])

# Сохраняем
conn.commit()
conn.close()

print(f"\nГОТОВО! База данных создана: {db_path}")
print("Теперь запускай свой основной скрипт — он будет работать!")