import sqlite3
from datetime import datetime

import click
from flask import current_app, g

# NOTE (BRI) Something about this, I don't like. This is managed life-cycle, in python.

def get_db():
    if 'db' in g:
        return g.db

    g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        ) 
    g.db.row_factory = sqlite3.Row
    return g.db 

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()


def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

@click.command('init-db')
def init_db_command():
    """click is a package which allows a user to register a command within the flask
    app, such that they can call `flask init-db`. Flask would search for the app,
    consume it, and this would get registered during consumption. Then it would consume
    the command `init-db`, and call succesfully if it was registered."""
    init_db()
    click.echo('Initialized database.')

def populate_db():
    ...

@click.command('populate-db')
def populate_db_command():
    """click is a package which allows a user to register a command within the flask
    app, such that they can call `flask init-db`. Flask would search for the app,
    consume it, and this would get registered during consumption. Then it would consume
    the command `init-db`, and call succesfully if it was registered."""
    populate_db()
    click.echo('Populated db.')

sqlite3.register_converter(
    'timestamp', lambda v: datetime.fromisoformat(v,decode())
)

def register(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)