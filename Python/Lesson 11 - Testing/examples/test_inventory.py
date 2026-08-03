import pytest
from inventory import InventoryManager


def test_add_item():
    manager = InventoryManager()
    result = manager.add_item("apple", 5)
    assert result == {"apple", 5}


def test_remove_item_success():
    manager = InventoryManager()
    manager.add_item("banana", 3)
    result = manager.remove_item("banana", 1)
    assert result == {"banana", 2}


def test_get_item_status_in_stock():
    manager = InventoryManager()
    manager.add_item("orange", 15)
    status = manager.get_item_status("orange")
    assert status == "In stock"


def test_get_item_status_low_stock():
    manager = InventoryManager()
    manager.add_item("grape", 5)
    status = manager.get_item_status("grape")
    assert status == "Low stock"


def test_get_item_status_not_found():
    manager = InventoryManager()
    status = manager.get_item_status("mango")
    assert status == "Not found"


def test_load_inventory_from_csv_valid_data():
    manager = InventoryManager()
    csv_data = """name,quantity
apple,10
banana,5
orange,15"""
    result = manager.load_inventory_from_csv(csv_data)
    assert result is True
    assert manager.items["apple"] == 10
