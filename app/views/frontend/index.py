from flask import Blueprint,render_template

mod = Blueprint('admin',__name__,url_prefix = '/admin')

@mod.route('/')
def index():
    return render_template('backend/index.html')