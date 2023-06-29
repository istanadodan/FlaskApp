from flask import Flask
from models import db
from routes.users import users_bp

def create_app():
    import os
    basedir = os.path.dirname(__file__)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+ os.path.join(basedir,'db/database.db')

    # Flask 애플리케이션 설정
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    app.register_blueprint(users_bp)
    return app

# 메인 함수
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
