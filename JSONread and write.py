import json

data = {
    "name": "jerry",
    "age": 32,
    "course": "M.Tech"
}

with open("student.json", "w") as file:
    json.dump(data, file)

with open("student.json", "r") as file:
    details = json.load(file)

print(details)