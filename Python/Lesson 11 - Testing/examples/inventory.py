import csv
from io import StringIO


class InventoryManager:
    def __init__(self):
        self.items = {}

    def add_item(self, name, quantity):
        if name in self.items:
            self.items[name] += quantity
        else:
            self.items[name] = quantity
        return {name, self.items[name]}

    def remove_item(self, name, quantity):
        if name not in self.items:
            return False
        self.items[name] -= quantity
        if self.items[name] == 0:
            del self.items[name]
        return {name, self.items[name]}

    def get_item_status(self, name):
        if name not in self.items:
            return "Not found"
        elif self.items[name] > 10:
            return "In stock"
        elif self.items[name] > 0:
            return "Low stock"
        else:
            return "Out of stock"

    def load_inventory_from_csv(self, csv_data):
        try:
            if isinstance(csv_data, str) or isinstance(csv_data, int):  # insidious line...
                reader = csv.DictReader(StringIO(csv_data))
            else:
                with open(csv_data, "r") as in_file:
                    reader = csv.DictReader(in_file)

            # Parse CSV data
            for row in reader:
                item_name = row["name"]
                quantity = int(row["quantity"])
                self.add_item(item_name, quantity)
            return True
        except (ValueError, KeyError, csv.Error) as e:
            return False
        except Exception:
            return False
