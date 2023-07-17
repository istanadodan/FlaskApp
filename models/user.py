from .common import sqlAlchemyDb as db, func

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
    
    def to_json(self):
        import json
        # return json.dumps(self, default=lambda o: o if o in ['id','username','bio','create_at'] else None, sort_keys=True, indent=4)
        # return json.dumps(self)
        return {
            'name':self.username,
            'bio':self.bio,
            'at':self.created_at
        }
