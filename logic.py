import json
import os

def save_books(data, filename="books.json"):
    """Сохранение списка книг в JSON"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def load_books(filename="books.json"):
    """Загрузка списка книг из JSON"""
    if not os.path.exists(filename):
        return []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []