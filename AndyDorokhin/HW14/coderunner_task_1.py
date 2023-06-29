""" 
    In file cars.json writed some cars (as array) models with filed max_speed. 
    In file cars2.json writed only one random car (as object) with random max_speed. 
    Read both files and write sorted by max_speed array of all cars in file result.json.

    As example if you have file cars.json with [ { "model": "Volkswagen Amarok 2.0", "max_speed": 179 }, { "model": "random_model", "max_speed": 163 } ]
    and cars2.json with {"model": "random_model","max_speed": 91}
    as result you must obtain file result.json with [{"model": "random_model", "max_speed": 91}, {"model": "random_model", "max_speed": 163}, {"model": "Volkswagen Amarok 2.0", "max_speed": 179}]
"""
import json

file_cars = open("cars.json", "r")
file_cars2 = open("cars2.json", "r")
result_file = open("result.json", "w")

cars = json.load(file_cars)
cars2 = json.load(file_cars2)
result = sorted(cars + [cars2], key=lambda x: x["max_speed"])
result_file.write(json.dumps(result))

file_cars.close()
file_cars2.close()
result_file.close()
