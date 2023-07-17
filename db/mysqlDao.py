from .mysql import MySqlDB, CursorType
db = MySqlDB()

class MySqlDBDao:
    cursor=None    
    SELCT = "select * from COMPANY"
    
    def __init__(self):        
        conn = db.get_db()
        # Connection 으로부터 Dictoionary Cursor 생성
        self.cursor = conn.cursor(CursorType.DictCursorType.value)         
    
    def query(self, sql:str, param:tuple=None):
        # 만약 Python 문자열에서 사용하는 기본 String Interpolation을 사용하면
        # 데이타에 특수 문자가 있는 경우 SQL문 문법 오류를 발생시킬 수 있다. 
        # sql = "select * from customer where category=%s and region=%s" % (1, data)
        # 변수 data 안에 단일 인용부호가 있는 경우 SQL Syntax 에러를 유발시키게 된다. 
        # 또한 이러한 String Interpolation 혹은 문자열 결합(Concatenation)을 통해 동적 SQL 문을 만드는 방법은 SQL Injection 공격에 쉽게 노출되는 문제점이 있다.
        r = self.cursor.execute(sql, param)
        if not r: return
        return self.cursor.fetchall()        
        
    def get_all(self):
        sql = self.SELCT
        return self.query(sql)
    
    def find_by_id(self, id:int):
        sql = f"{self.SELCT} where id=%s"
        return self.query(sql, (id))
