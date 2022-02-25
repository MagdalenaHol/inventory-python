
import csv
from tkinter.ttk import Separator

inventory = {"gold coin": 45, "arrow": 12, "torch": 6, "dagger": 2, "rope": 1, "ruby": 1}
added_items = ["arrow", "dagger", "sliver coin"] 
removed_items = ["arrow", "gold coin", "arrow", "dagger", "dagger"]


def display_inventory(inventory):

    for key in inventory:
        print(f"\n{key}: {int(inventory[key])}")
        if None in inventory:
            return None
        
def add_to_inventory(inventory, added_items):
    
    for element in added_items:
        if element in inventory:
            inventory[element] += 1
        else:
            inventory.setdefault(element, 1)
   
def remove_from_inventory(inventory, removed_items):
    
    for element in removed_items:
        if element not in inventory:
            continue
        if element in inventory:
            inventory[element] -= 1
        if inventory[element] <= 0:
            del inventory[element]


def print_table(inventory, order):
    header = ["item name", "count"]
    output = ""
    
    list_of_keys = inventory.keys()
    longest_string = max(list_of_keys, key=len)
    longest_string_len = len(longest_string)

    output = (f'{str(header[0]).rjust(longest_string_len)} | {header[1].rjust(5)}')
    print("-" * (len(output) + len(header)))
    print(output)
    print("-" * (len(output) +len(header)))


    if order == " count,desc": 
        inventory = sorted(inventory.items(), key=lambda count: count[1], reverse=True)
        inventory = dict(inventory)
    elif order == "count,asc":
        inventory = sorted(inventory.items(), key=lambda count: count[1], reverse=False)
        inventory = dict(inventory)
    elif order == None:
        inventory = inventory.items()
    
    for key, value in inventory.items():
        print(f"{str(key).rjust(longest_string_len)} | {value:5}")
    print("-" * (len(header) + len(output)))



def import_inventory(inventory, filename="test_inventory.csv"):

    results = []

    with open("test_inventory.csv", "r") as f:
        file = csv.reader(f)
        for line in file:
            for item in line:
                results.append(item)
            add_to_inventory(inventory, results)
            print_table(inventory, results)   
            

def export_inventory(inventory, filename="test_inventory_export.csv"):
    
    with open("test_inventory_export.csv", "w") as items_export_file:
        
        filednames = ["item_name", "value_of_item"]

        items_to_write = csv.DictWriter(items_export_file, filename="test_inventory_export.csv")

        i = 0
        while i < len(list_key_inventory):
            items_to_write.writerow({"item_name": list_key_inventory[i], "value_of_item": list_value_inventory[i]})
            i += 1



print(display_inventory(inventory))
print(add_to_inventory(inventory, added_items))
print(remove_from_inventory(inventory, removed_items))
print_table(inventory, "count,desc")
print(import_inventory(inventory, filename="test_inventory.csv"))
# export_inventory(inventory, filename="test_inventory_export.csv")