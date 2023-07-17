from flask import render_template, Blueprint, jsonify, request
from db.mysqlDao import MySqlDBDao
import logging

logger = logging.getLogger(__name__)
company_bp = Blueprint('company', __name__)
dao = MySqlDBDao()

# 컨트롤러
@company_bp.route('/list', methods=['GET'])
def list():     
    return jsonify(dao.get_all())

@company_bp.route('/id/<id>', methods=['GET'])
def find_by_id(id):
    id_ = request.view_args['id']
    logger.debug(f'id={id}')
    logger.debug(f'id_={id_}')
    return jsonify(dao.find_by_id(id))