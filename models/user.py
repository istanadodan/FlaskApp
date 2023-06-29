from .common import db, func

# 모델 정의
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    bio = db.Column(db.Text)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    
    def __init__(self, username):
        self.username = username
        
    def __repr__(self):
        return f'<User {self.username}>'
