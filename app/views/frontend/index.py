from flask import Blueprint,render_template

mod = Blueprint('index',__name__,url_prefix = '/index')

@mod.route('/')
def index():
    return render_template('frontend/index.html')

@mod.route('/list',defaults = {'page' : 'index'})
@mod.route('/list/<page>')
def list(page):
    return render_template('frontend/list.html')