class Asset:
    def __init__(self, asset_id, name, location):
        self.asset_id = asset_id
        self.name = name
        self.location = location
        self.date_taken = None
        self.return_date = None

    def update_location(self, new_location):
        self.location = new_location

    def set_return_date(self, return_date):
        self.return_date = return_date

    def is_available(self):
        return self.date_taken is None


class Staff:
    def __init__(self, staff_id, name):
        self.staff_id = staff_id
        self.name = name
        self.assets = []  # List to hold assigned assets

    def assign_asset(self, asset, date_taken, return_date):
        asset.date_taken = date_taken
        asset.return_date = return_date
        self.assets.append(asset)

    def return_asset(self, asset):
        if asset in self.assets:
            asset.date_taken = None
            asset.return_date = None
            self.assets.remove(asset)


class AssetManager:
    def __init__(self):
        self.assets = {}
        self.staff_members = {}
        self.assignments = []  # To track asset assignments

    def add_asset(self, asset):
        self.assets[asset.asset_id] = asset

    def remove_asset(self, asset_id):
        if asset_id in self.assets:
            del self.assets[asset_id]

    def add_staff(self, staff):
        self.staff_members[staff.staff_id] = staff

    def assign_asset_to_staff(self, staff_id, asset_id, date_taken, return_date):
        if staff_id in self.staff_members and asset_id in self.assets:
            staff = self.staff_members[staff_id]
            asset = self.assets[asset_id]
            staff.assign_asset(asset, date_taken, return_date)
            self.assignments.append((staff_id, asset_id, date_taken, return_date))

    def process_return(self, staff_id, asset_id):
        if staff_id in self.staff_members and asset_id in self.assets:
            staff = self.staff_members[staff_id]
            asset = self.assets[asset_id]
            staff.return_asset(asset)
            self.assignments = [(s_id, a_id, d_t, r_t) for (s_id, a_id, d_t, r_t) in self.assignments if a_id != asset_id]

    def check_asset_status(self, asset_id):
        if asset_id in self.assets:
            asset = self.assets[asset_id]
            return {
                "name": asset.name,
                "available": asset.is_available(),
                "location": asset.location,
                "date_taken": asset.date_taken,
                "return_date": asset.return_date,
            }
        return None