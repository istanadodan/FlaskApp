from enum import Enum, auto
import pymysql
    
class CursorType(Enum):
    #Row 결과를 Dictionary 형태로 리턴한다.
    DictCursorType = pymysql.cursors.DictCursor
    #Row 결과를 Tupple 형태로 리턴한다. (기본값)
    TuppleCursorType = None    
        
class MySqlDB:
    host:str='localhost'    
    port:int = 3306
    db:str='visitlog'
    user:str='mysql_user'
    pw:str='mysql_password'
    charset:str='utf8'
    conn:any=None    
    
    def __init__(self) -> None:
        self.app=None
        self.driver=None
        
    def init_app(self, app):
        self.app = app
        self.connect()
    
    def connect(self):
        self.conn = pymysql.connect(host=self.host, port=self.port, db=self.db, user=self.user, passwd=self.pw, charset=self.charset)
        return self.conn        
    
    def get_db(self):
        if not self.conn:
            return self.connect()
        return self.conn    