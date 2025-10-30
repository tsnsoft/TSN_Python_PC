import sqlite3
import os

# Создаём папку txt, если её нет
os.makedirs("txt", exist_ok=True)

# Подключаемся к базе
with sqlite3.connect("db/q.db") as conn:
    conn.row_factory = sqlite3.Row  # ← Позволяет обращаться по именам колонок
    cur = conn.cursor()

    # Получаем все секции
    cur.execute("SELECT sId, titleTranslation FROM S ORDER BY sId")
    for sec in cur:
        sId = sec["sId"]
        title = sec["titleTranslation"]

        filename = f"txt/Глава {sId:03d} {title}.txt"
        header = f'Глава {sId} "{title}"\n\n'

        print(f"Создаю: {filename}")

        with open(filename, "w", encoding="utf-8") as f:
            f.write(header)

            # Получаем стихи для этой секции
            cur2 = conn.cursor()
            cur2.execute("SELECT vrId, vr FROM V WHERE sId = ? ORDER BY _id", (sId,))
            for v in cur2:
                line = f"{v[0]}. {v[1]}\n"
                f.write(line)
                print(line.strip())

print("\nГотово! Все файлы в папке txt")