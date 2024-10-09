#Problem 1
print("Problem 1")

# Create a dictionary object with the {} brakey notation 
# States = Keys, Capitals = Values
StatesCapitals = {
    "Los Angeles" : "California",
    "Albany" : "New York",
    "Honolulu" : "Hawaii",
    "Juneau" : "Alaska",
    "Austin" : "Texas"
    }
print(StatesCapitals)
print(type(StatesCapitals))
print('')
# Create a Dictionary object with bulit-in function dict()

StatesCapitals2 = dict([
    ("Los Angeles", "California"),
    ("Albany", "New York"),
    ("Honolulu", "Hawaii"),
    ("Juneau", "Alaska"),
    ("Austin", "Texas")
])
print(StatesCapitals2)
print(type(StatesCapitals2))
print('')

#Accessing keys and values in a Dictionary
print("'Accessing keys and values in a Dictionary'")
print(StatesCapitals["Los Angeles"])
print('')
print("'Adding Entry to a Dictionary'")
StatesCapitals["NYC"] = 'The Bronx'
print(StatesCapitals["NYC"])
print(StatesCapitals)
print('')

print("'Update an Entry in a Dictionary'")
StatesCapitals[420] = "New York"
print(StatesCapitals)
print(StatesCapitals[420])
print('')

print("'Update an Entry in a Dictionary'")
StatesCapitals[420] = "Brooklyn"
print(StatesCapitals, ": Updated")
print('')

print("'Delete an Entry in a Dictionary'")
del StatesCapitals["Los Angeles"]
print(StatesCapitals, ": Deleted")

print('')
#Problem 2
print("Problem 2")

# Retrieve the value for the key 'California'
StatesCapitals["Los Angeles"] = "California"
print(StatesCapitals["Los Angeles"], ": Retrieved")
print('')

#Add the State: Captial pair for FLorida: Tallahassee to the dictionary
StatesCapitals["Florida"] = "Tallahassee"
print(StatesCapitals, ": Added")
print('')

#Update the value for the key 'California' to 'Sacramento'
StatesCapitals["Los Angeles"] = "Sacramento"
print(StatesCapitals["Los Angeles"], ": Updated")
print(StatesCapitals)
print('')

#Delete Alaska from the dictionary
del StatesCapitals["Juneau"]
print(StatesCapitals, ": Deleted")
