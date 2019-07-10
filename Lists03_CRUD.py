###########################################################
# CRUD
# Create - How to create a new item in the data structure.
# Read - How to access an item in a data structure.
# Update - How to change an item in a data structure.
# Delete - How to remove an item from a list.
###########################################################
adventure_time_characters = ['Princess Bubblegum', 'Marceline', 'Lumpy Space Princess']
print("Adventure Time Characters")
print(adventure_time_characters)

## CREATE ##
adventure_time_characters.append("Flame Princess")
# print("\nappending Flame Princess")
# print(adventure_time_characters)

adventure_time_characters.insert(2,"Tree Trunks")
# print("\ninserting Tree Trunks at index 2")
# print(adventure_time_characters)

adventure_time_characters.extend(["Finn", "Jake", "Lemongrab"])
# print("\nextending the list with Finn, Jake, and Lemongrab")
# print(adventure_time_characters)


## YOU DO ##
# Add some elements to the list using append, insert, and extend



################################################################
## READ ##
# print("printing the element at index 1")
# print(adventure_time_characters[1])

# print("printing the element at the end of the list")
# print(adventure_time_characters[len(adventure_time_characters)-1])


## YOU DO ##
# Print individual elements from the list



###############################################################
## UPDATE ##
adventure_time_characters[2] = "BMO"
# print("\nupdating the element at index 2 to \"BMO\"")
# print(adventure_time_characters)


## YOU DO ##
# Change elements in your list


###############################################################
## DELETE ##
adventure_time_characters.remove('Lemongrab')
# print("\nremoving Lemongrab")
# print(adventure_time_characters)

adventure_time_characters.pop(5)
# print("\npopping out the element at the 5th index")
# print(adventure_time_characters)

## YOU DO ##
# Remove some items from the list