import json
from dataclasses import dataclass, asdict
from flask import jsonify, Flask
app = Flask(__name__)

@dataclass(slots=True)
class Person:
    name: str
    age: int    



# 객체를 JSON 문자열로 직렬화
# print(person.__dict__)
# json_str = json.dumps(person.__dict__)
# print(json_str)  # '{"name": "John Doe", "age": 30}'
with app.app_context():
    person = Person("John Doe", 30)
    json_data = jsonify(asdict(person))
    print(json_data.get_data(as_text=True))
    
# json_str2 = json.dumps(asdict(person))
# print(json_str2)

class User:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email        


with app.app_context():
    user = User("John", 30, "john@example.com")    
    json_data = jsonify(user.__dict__)    
    print(json_data.get_data())
    json_data2 = jsonify([1,2,3])
    print(json_data2)
