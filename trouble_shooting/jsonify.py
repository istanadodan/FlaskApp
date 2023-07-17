import json
from flask import jsonify, Flask
app = Flask(__name__)

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def toJSON(self):
        # 객체를 JSON 문자열로 변환합니다. 
        # "default" 매개변수를 사용하여 객체의 "dict"를 직렬화에 사용하도록 지정합니다.
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

users = [User("John", 25), User("Alice", 30)]
with app.app_context():
    #jsonify를 사용하기 전에 app.app_context()를 사용하여 애플리케이션 컨텍스트를 설정합니다.
    #@app.route('/')은 context()내에서 실행된다.
    json_data = jsonify([user.toJSON() for user in users])
    print(json_data.get_data(as_text=True))