from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from db.mysql import MySqlDB

sqlAlchemyDb = SQLAlchemy()
mysqlDb = MySqlDB()
