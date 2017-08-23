import os
from flask import (Blueprint, render_template, request, flash, session,
                   redirect, url_for, current_app)
from werkzeug import secure_filename
from raspweb.model import query_db, get_db

bp = Blueprint('admin', __name__, url_prefix='/admin')


def allowed_file(filename):
    extensions = current_app.config['ALLOWED_EXTENSIONS']
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in extensions


@bp.route('/')
def index():
    if 'username' in session:
        data = {
            'features': query_db('select * from features'),
            'news': query_db('select * from news')
        }
        return render_template('admin/index.html', **data)
    return redirect(url_for('.login'))


@bp.route('/login/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin':
            error = 'Invalid username'
        elif request.form['password'] != 'default':
            error = 'Invalid password'
        else:
            session['username'] = 'admin'
            flash('You were logged in', 'info')
            return redirect(url_for('.index'))
    return render_template('admin/login.html', error=error)


@bp.route('/logout/')
def logout():
    session.pop('username', None)
    flash('You were logged out', 'info')
    return redirect(url_for('.index'))


@bp.route('/add_entry', methods=['POST'])
def add_entry():
    filename = ''
    if 'image' in request.files:
        image = request.files['image']
        # if user does not select file, browser also
        # submit a empty part without filename
        if image.filename != '':
            if image and allowed_file(image.filename):
                filename = os.path.join(current_app.config['UPLOAD_FOLDER'],
                                        secure_filename(image.filename))
                image.save(os.path.join('static', filename))

    feat = (request.form['heading'], request.form['subheading'],
            request.form['message'], filename)

    db = get_db()
    db.cursor().execute('insert into features values (?, ?, ?, ?)', feat)
    db.commit()
    flash('Feature successfully added', 'success')
    return redirect(url_for('.index'))
