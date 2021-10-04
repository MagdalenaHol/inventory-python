
import csv


inventory = {"gold coin": 45, "arrow": 12, "torch": 6, "dagger": 2, "rope": 1, "ruby": 1}


def display_inventory(inventory):

    for key in inventory:
        print(f"""\n{key}: {inventory[key]}""")
        if None in inventory:
            return None
        

def add_to_inventory(inventory, added_items):
    
    for element in added_items:
        if element in inventory:
            inventory[element] += 1
        else:
            inventory.setdefault(element, 1)


added_items = ["arrow", "brain", "koziol", "gold coin", "arrow"] 
   
# add_to_inventory(inventory, added_items)
# display_inventory(inventory)
    

def remove_from_inventory(inventory, removed_items):
    
    for element in removed_items:
        if element not in inventory:
            continue
        if element in inventory:
            inventory[element] -= 1
        if inventory[element] <= 0:
            del inventory[element]


removed_items = ["arrow", "gold coin", "arrow", "dagger", "dagger", "dagger"]


# remove_from_inventory(inventory, removed_items)
# display_inventory(inventory)


def print_table(inventory, order):

    header = ["item name", "count"]
    output = ""
    print("\n-------------------------")
    for item in header:
        output = "  "  + str(header[0]  +  " | " + header[1]) +  " " 
    print(output)
    print("-------------------------")

    if order == " count, desc": 
        inventory = sorted(inventory.items(), key=lambda count: count[1], reverse=True)
        inventory = dict(inventory)

    for key, value in inventory.items():
        print(f"{key:>11} | {value:>5}")
    print("-------------------------")


# print_table(inventory, "count, desc")


def import_inventory(inventory, filename):

    results = []

    with open(filename, "r") as f:
        file = csv.reader(f)
        for line in file:
            for item in line:
                results.append(item)

    print(results)
    add_to_inventory(inventory, results)
    

import_inventory(inventory, "import_inventory.csv")
display_inventory(inventory)
print_table(inventory, "count, desc")


list_value_inventory = list(inventory.values())
list_key_inventory = list(inventory)


def export_inventory(inventory, filename):
    
    with open(filename, "w") as items_export_file:
        
        filednames = ["item_name", "value_of_item"]

        items_to_write = csv.DictWriter(items_export_file, filednames=filednames)

        i = 0
        while i < len(list_key_inventory):
            items_to_write.writerow({"item_name": list_key_inventory[i], "value_of_item": list_value_inventory[i]})
            i += 1


export_inventory(inventory, "test_inventory.csv")
display_inventory(inventory)
print_table(inventory, "count, desc")