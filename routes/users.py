from flask import render_template, Blueprint, jsonify
from models import User
import logging

logger = logging.getLogger(__name__)
users_bp = Blueprint('users', __name__)

# 컨트롤러
@users_bp.route('/users', methods=['GET'])
def users():
    import service.ppt_create as ppt
    from service.dto.user import User as UserDto
    ppt.create_ppt()
    entity_users = User.query.all()
    users=[]
    for u in entity_users:
        u2 = dict()
        for item in u.__dict__.items():
            if not item[0] in UserDto.__dict__: continue
            u2.update({item[0]:item[1]})

        users.append(u2)
        
    logger.debug(f'users={users}')
        
    return jsonify([u for u in users])    

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