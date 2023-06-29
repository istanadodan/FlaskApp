from flask import render_template, Blueprint, jsonify
from models import User

users_bp = Blueprint('users', __name__)

# 컨트롤러
# function to render index page
@users_bp.route('/users', methods=['GET'])
def users():
    users = User.query.all()
    return jsonify([user.serialize() for user in users])

@users_bp.route('/list')
def list():    
    import pandas as pd
    # DB 조회 예시
    users = User.query.all()

    # 데이터 프레임 생성 예시
    data = {'Username': [user.username for user in users]}
    df = pd.DataFrame(data)

    # 데이터 프레임을 HTML 테이블로 변환
    table = df.to_html()
    
    # HTML 템플릿 렌더링
    return render_template('index2.html', table=table, users=users)

@users_bp.route('/<int:user_id>/')
def user(user_id:int):    
    user = User.query.get_or_404(user_id)
    return render_template('user.html', user=user)

@users_bp.route('/create/', methods=('GET','POST'))
def create():
    return render_template('create.html')