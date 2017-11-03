```
$ git clone https://github.com/LinuxHubRu/quick-and-dirty-blog-with-flask.git
$ cd quick-and-dirty-blog-with-flask
$ virtualenv venv  # virtualenv venv -p path/to/python2
$ source venv/bin/activate
(venv)$ pip install -r requirements.txt

(venv)$ # populate the config
(venv)$ echo "\
import os

DEBUG = False
USERNAME = 'dirty_admin'
PASSWORD = 'da2017'

SECRET_KEY = 'p9Bv<3Eid9%i01'
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'mysql://' + USERNAME + ':' + PASSWORD \
    + '@localhost/dirty_blog'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repo')
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_ECHO = True
"> config.py

(venv)$ # populate the db
(venv)$ ./db_create.py
(venv)$ ./run.py
```
