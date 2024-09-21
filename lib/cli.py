import click
from uuid import uuid4
from database import init_db, Session
from models import Asset, Staff
from datetime import datetime

@click.group()
def cli():
    """Asset Management CLI"""
    pass

@cli.command()
@click.argument('name')
@click.argument('location')
def add_asset(name, location):
    """Add a new asset."""
    session = Session()
    asset = Asset(id=str(uuid4()), name=name, location=location)
    session.add(asset)
    session.commit()
    click.echo(f"Added asset: {name}")

@cli.command()
@click.argument('name')
def add_staff(name):
    """Add a new staff member."""
    session = Session()
    staff = Staff(id=str(uuid4()), name=name)
    session.add(staff)
    session.commit()
    click.echo(f"Added staff: {name}")

@cli.command()
@click.argument('asset_id')
def check_status(asset_id):
    """Check the status of an asset."""
    session = Session()
    asset = session.query(Asset).filter_by(id=asset_id).first()
    if asset:
        click.echo(f"Asset ID: {asset.id}, Name: {asset.name}, Location: {asset.location}")
    else:
        click.echo("Asset not found.")

if __name__ == "__main__":
    cli()