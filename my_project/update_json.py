import json
def get_max_index_by_chat_id(pill_list, chat_id):
    max_index = -1
    for index, pill in enumerate(pill_list):
        if pill['chat_id'] == chat_id:
            max_index = max(max_index, index)
    return max_index

def update_json(chat_id, key, value):
    file_path = 'pills_library.json'

    with open(file_path, 'r') as file:
        data = json.load(file)
        if key == 'name':
                data.append({"chat_id": chat_id, "name": value, "day": 0, "time": []})
        elif key == "day" or key == "time":
            max_index = get_max_index_by_chat_id(data, chat_id)
            data[max_index][key] = value
    with open(file_path, 'w') as file:
        json.dump(data, file)

# update_json(697755555, "name", "pill100")
# update_json(697755555, "day", 55)
# update_json(697755555, "time", ["18:00"])


