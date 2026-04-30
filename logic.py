import json
import random
import os

def generate_ticket_id():
    """Генерация уникального ID (библиотека random)"""
    return f"REQ-{random.randint(1000, 9999)}"

def save_to_json(data, filename="tickets.json"):
    """Сохранение данных в JSON"""
    tickets = load_from_json(filename)
    tickets.append(data)
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(tickets, f, ensure_ascii=False, indent=4)

def load_from_json(filename="tickets.json"):
    """Загрузка данных из JSON"""
    if not os.path.exists(filename):
        return []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []