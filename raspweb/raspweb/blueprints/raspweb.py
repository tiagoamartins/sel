from flask import Blueprint, render_template
from raspweb.model import query_db

bp = Blueprint('raspweb', __name__)


@bp.route('/')
def index():
    features = query_db('select * from features')
    news = query_db('select * from news')
    return render_template('index.html', news=news, features=features)


@bp.route('/about/')
def about():
    members = query_db('select * from members')
    return render_template('about.html', team=members)
