"""
Inventory System Module
Maintains a simple stock database and handles item operations.
"""

import json
from datetime import datetime

stock_data = {}

def add_item(item="default", qty=0, logs=None):
    """
    Adds a new item or increments the quantity if it exists.
    Rejects invalid types and negative quantities.
    Updates the operation log.
    """
    if logs is None:
        logs = []
    if not isinstance(item, str):
        print("Invalid item type; must be string")
        return
    if not isinstance(qty, int):
        print("Invalid quantity type; must be integer")
        return
    if qty < 0:
        print("Quantity cannot be negative")
        return
    if not item:
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")

def remove_item(item, qty):
    """
    Removes a quantity from an item if enough stock exists.
    Ensures stock does not go negative.
    """
    try:
        if stock_data[item] < qty:
            print(f"Not enough '{item}' in stock to remove {qty}. Current stock: {stock_data[item]}")
            return
        stock_data[item] -= qty
        if stock_data[item] == 0:
            del stock_data[item]
    except KeyError:
        print(f"Item '{item}' does not exist in stock")

def get_qty(item):
    """
    Gets the current quantity for a given item.
    """
    return stock_data.get(item, 0)

def load_data(file="inventory.json"):
    """
    Loads inventory data from a JSON file.
    """
    global stock_data
    with open(file, "r", encoding="utf-8") as f:
        stock_data = json.loads(f.read())

def save_data(file="inventory.json"):
    """
    Saves inventory data to a JSON file.
    """
    with open(file, "w", encoding="utf-8") as f:
        f.write(json.dumps(stock_data))

def print_data():
    """
    Prints a report of all items with positive stock.
    """
    print("Items Report")
    for i in stock_data:
        if stock_data[i] > 0:
            print(i, "->", stock_data[i])

def check_low_items(threshold=5):
    """
    Returns a list of items below the threshold.
    """
    result = []
    for i in stock_data:
        if stock_data[i] < threshold and stock_data[i] > 0:
            result.append(i)
    return result

def main():
    """
    Main function for running inventory operations.
    """
    add_item("apple", 10)
    add_item("banana", -2)
    add_item(123, "ten")
    remove_item("apple", 3)
    remove_item("orange", 1)
    print(f"Apple stock: {get_qty('apple')}")
    print(f"Low items: {check_low_items()}")
    save_data()
    load_data()
    print_data()

if __name__ == "__main__":
    main()
