from flask.cli import with_appcontext
import click

from src.extensions import db


@click.command("init-db")
@with_appcontext
def init_db():
    click.echo("Creating Database...")
    db.drop_all()
    db.create_all()
    click.echo("Database Created.")
