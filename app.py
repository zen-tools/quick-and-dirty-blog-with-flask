#!/usr/bin/env python

from sqlalchemy import desc
from models import PostItem
from database import db_session
from flask import (
    Flask, request, session, redirect,
    url_for, abort, render_template, flash
)
from flaskext.auth import Auth
from flaskext.auth import AuthUser

app = Flask(__name__)
app.config.from_pyfile('config.py')
auth = Auth(app)


@app.before_request
def init_users():
    admin = AuthUser(username=app.config['USERNAME'])
    admin.set_and_encrypt_password(app.config['PASSWORD'])
    auth.users = {'admin': admin}


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


@app.template_filter('strftime')
def _jinja2_datetimeformat(value, format='%H:%M / %d-%m-%Y'):
    return value.strftime(format)


@app.route('/')
def show_entries():
    entries = []
    for post in PostItem.query.order_by(desc(PostItem.date)):
        entries.append({
            "id": post.id,
            "title": post.title,
            "text": post.text,
            "date": post.date
        })
    return render_template('show_entries.html', entries=entries)


@app.route('/add_entry', methods=['GET', 'POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(403)
    if request.method == 'POST':
        title = request.form['title']
        text = request.form['text']

        if not (title and text):
            flash('No title or text')
            return redirect(url_for('show_entries'))

        post = PostItem(title, text)
        db_session.add(post)
        db_session.commit()
        flash('New entry was successfully posted')
        return redirect(url_for('show_entries'))
    else:
        return render_template('add_entry.html')


@app.route('/del_entry/<int:post_id>', methods=['GET'])
def del_entry(post_id):
    if not session.get('logged_in'):
        abort(401)
    post = PostItem.query.filter_by(id=post_id).first()
    if post is None:
        abort(404)
    db_session.delete(post)
    db_session.commit()
    return redirect(url_for('show_entries'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if session.get('logged_in'):
        return redirect('/')
    error = None
    if request.method == 'POST':
        username = request.form['username']
        if username in auth.users:
            if auth.users[username].authenticate(request.form['password']):
                session['logged_in'] = True
                flash('You were logged in')
                return redirect(url_for('show_entries'))
        error = 'Invalid username or password'
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    if session.get('logged_in'):
        session.pop('logged_in', None)
        flash('You were logged out')
    return redirect(url_for('show_entries'))
