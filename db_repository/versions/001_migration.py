from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
posts = Table('posts', pre_meta,
    Column('id', INTEGER(), primary_key=True, nullable=False),
    Column('title', VARCHAR(length=128)),
    Column('text', VARCHAR(length=1024)),
    Column('date', DATETIME),
)

users = Table('users', pre_meta,
    Column('id', INTEGER(), primary_key=True, nullable=False),
    Column('name', VARCHAR(length=50)),
    Column('email', VARCHAR(length=120)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['posts'].drop()
    pre_meta.tables['users'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['posts'].create()
    pre_meta.tables['users'].create()
