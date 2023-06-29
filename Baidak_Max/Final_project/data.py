import requests


parameters = {"amount": 15,
        "type": "boolean",
        "difficulty": "medium"}



response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]
