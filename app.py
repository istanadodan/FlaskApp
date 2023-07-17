from flask import Flask
from models import sqlAlchemyDb, mysqlDb
from routes.users import users_bp
from routes.company import company_bp

def config_logger():
    import logging    
    log_format = '%(asctime)s - %(levelname)s - %(name)s - %(message)s'
    logging.basicConfig(format=log_format, level=logging.DEBUG)

def create_app():
    #로거 설정
    config_logger()
    
    import os
    basedir = os.path.dirname(__file__)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+ os.path.join(basedir,'db/database.db')

    # Flask 애플리케이션 설정    
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    sqlAlchemyDb.init_app(app)
    mysqlDb.init_app(app)
    app.register_blueprint(users_bp, url_prefix='/user')
    app.register_blueprint(company_bp, url_prefix='/company')
    return app

# 메인 함수
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)