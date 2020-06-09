from store import Store
from category import Category

running_category = Category("Running", "All your running needs", [])
baseball_category = Category("Baseball", "Rockies Fans only", [])
basketball_category = Category("Basketball", "Indoor and outdoor products", [])
football_category = Category("Football", "Are you ready for it?", [])


sports_store = Store("Gander Mountain", [running_category, baseball_category, basketball_category, football_category])

# produce_store = Store("Trader Joes", ["Dairy", "Meat", "Bread", "Produce"])
# print(sports_store)
# print(produce_store)
# print(produce_store.name)
# print(repr(sports_store))

### REPL
choice = -1
print(sports_store)
print("Type q to quit")

while True:
    ## Read
    # get input from command line
    choice = input("Please choose a category (#):")
    try:
        ## Evaluate
        if (choice == 'q'):
            break
        choice = int(choice) - 1
        if choice >= 0 and choice < len(sports_store.categories):
            chosen_category = sports_store.categories[choice]
            ## Print
            print(chosen_category)
        else:
            print("The number is out of range")
    except ValueError:
        print("Please enter a valid number")

