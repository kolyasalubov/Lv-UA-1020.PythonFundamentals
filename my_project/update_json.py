import json
from datetime import datetime
def get_max_index_by_chat_id(pill_list, chat_id): # функція знаходить найбільший індекс
    # елемента в списку, який відповідає певному chat_id
    max_index = -1
    for index, pill in enumerate(pill_list):
        if pill['chat_id'] == chat_id:
            max_index = max(max_index, index)
    return max_index

def update_json(chat_id, key, value): #записуємо дані в json
    file_path = 'pills_library.json'#сам файл json
    date = datetime.now().strftime("%Y-%m-%d")# date перетворення дати в стрінгу(дата створення дікта)

    with open(file_path, 'r') as file:#спершу вичитуємо файл
        data = json.load(file)
        if key == 'name':#якщо приходить name додаємо новий словник в список словників
                data.append({"chat_id": chat_id, "name": value, "day": 0, "time": [], "creation_date": date})
        elif key == "day" or key == "time":#якщо приходить "day" чи "time" записуємл в максимальний (останній) словник
            # дні по ключу і час аналогічно використовуючи функцію яка повертає макс індекс по конкретному id
            max_index = get_max_index_by_chat_id(data, chat_id)
            data[max_index][key] = value
    with open(file_path, 'w') as file:
        json.dump(data, file)



# update_json(697755555, "name", "pill100")
# update_json(697755555, "day", 55)
# update_json(697755555, "time", ["18:00"])


