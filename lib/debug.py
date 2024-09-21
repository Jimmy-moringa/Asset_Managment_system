from asset_management.database import init_db, Session
from asset_management.models import Asset, Staff
from uuid import uuid4
from datetime import datetime

def add_asset(name, location):
    session = Session()
    asset = Asset(id=str(uuid4()), name=name, location=location)
    session.add(asset)
    session.commit()
    print(f"Added asset: {name}")

def add_staff(name):
    session = Session()
    staff = Staff(id=str(uuid4()), name=name)
    session.add(staff)
    session.commit()
    print(f"Added staff: {name}")

def check_asset_status(asset_id):
    session = Session()
    asset = session.query(Asset).filter_by(id=asset_id).first()
    if asset:
        print(f"Asset ID: {asset.id}, Name: {asset.name}, Location: {asset.location}")
    else:
        print("Asset not found.")

def main():
    init_db()  # Initialize the database
    while True:
        print("\nDebugging Interface")
        print("1. Add Asset")
        print("2. Add Staff")
        print("3. Check Asset Status")
        print("4. Exit")
        
        choice = input("Select an option: ")

        if choice == '1':
            name = input("Enter asset name: ")
            location = input("Enter asset location: ")
            add_asset(name, location)

        elif choice == '2':
            name = input("Enter staff name: ")
            add_staff(name)

        elif choice == '3':
            asset_id = input("Enter asset ID: ")
            check_asset_status(asset_id)

        elif choice == '4':
            print("Exiting debug interface.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()