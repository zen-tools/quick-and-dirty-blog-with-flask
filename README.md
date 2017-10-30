```
$ git clone https://github.com/LinuxHubRu/quick-and-dirty-blog-with-flask.git \
  quick-and-dirty-blog-with-flask-linuxhubru
$ cd quick-and-dirty-blog-with-flask-linuxhubru
$ virtualenv venv  # virtualenv venv -p path/to/python2
$ source venv/bin/activate
(venv)$ pip install -r requirements.txt

$ # populate the config, which should be excluded from the repo:
$ echo "\
SECRET_KEY = 'p9Bv<3Eid9%i01'
#SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
SQLALCHEMY_DATABASE_URI = 'mysql://dirty_admin:da2017@localhost/dirty_blog'
SQLALCHEMY_ECHO = True
SQLALCHEMY_TRACK_MODIFICATIONS = True

DEBUG = False
USERNAME = 'dirty_admin'
PASSWORD = 'ba2017'
"> config.py

(venv)$ ./run.py
```
