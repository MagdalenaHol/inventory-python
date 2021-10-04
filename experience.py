import csv

def working_with_file():
    with open('test.txt') as f:
        lines = f.read()
        print(lines)
        

# working_with_file()


def workin_with_file(): 
    with open('test.txt', encoding='utf8') as f:
        for line in f:
            print(line.strip())



# workin_with_file()




def import_inventory():
    """Import new inventory items from a CSV file.""" 

    results = []

    with open("test_inventory.csv", "r") as f:
        file = csv.reader(f)
        for line in file:
            for item in line:
                results.append(item)

    print(results)




import_inventory()
