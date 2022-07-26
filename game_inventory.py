
import csv


inventory = {"gold coin": 45, "arrow": 12, "torch": 6, "dagger": 2, "rope": 1, "ruby": 1}
added_items = ["arrow", "dagger", "sliver coin"] 
removed_items = ["arrow", "gold coin", "arrow", "dagger", "dagger"]


def display_inventory(inventory):

    for key in inventory:
        print(f"{key}: {int(inventory[key])}")
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

    output = (f'{str(header[0]).rjust(longest_string_len)} | {header[1].rjust(3)}')
    print("-" * (len(output) + len(header)))
    print(output)
    print("-" * (len(output) +len(header)))


    if order == "count,desc": 
        inventory = dict(sorted(inventory.items(), key=lambda count: count[1], reverse=True))
    elif order == "count,asc":
        inventory = dict(sorted(inventory.items(), key=lambda count: count[1]))
        
    # elif order == None:
    #     inventory = inventory.items()
    
    for key, value in inventory.items():
        print(f"{str(key).rjust(longest_string_len)} | {value:3}")
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

    try:
        with open(filename, "w") as f:
            every_item = ','.join(inventory)
            ineed = ""

            for element in every_item:
                if element not in ineed:
                    ineed.join(element)
                    f.write(ineed)

    except PermissionError:
        print(f"You don't have permission creating file '{filename}'!")

        for element in every_item:
                if element not in ineed:
                    ineed.join(element)
                    f.write(ineed)

        
        # list_of_keys = inventory.keys()
        # with open(filename, "w") as f:      
        #     f.write(str(list_of_keys).replace("[","").replace("dict_keys","").replace("(","").replace("]","").replace(")","").replace("'","").replace(", ",","))
       
    
   

print(display_inventory(inventory))
print(add_to_inventory(inventory, added_items))
print(remove_from_inventory(inventory, removed_items))
print(print_table(inventory, "count,desc"))
print(print_table(inventory, "count,asc"))
print(import_inventory(inventory, filename="test_inventory.csv"))
export_inventory(inventory, filename="test_inventory_export.csv")