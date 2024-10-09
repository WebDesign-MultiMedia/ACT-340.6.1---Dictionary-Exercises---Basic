grocery_list = {
    'fruits': ['apple', 'blueberry', 'strawberries'],
    'vegtables': ['broccoli', 'cauliflower'], 'meat': 'chicken'
}

print(grocery_list)
print('')

# .get() method
print('.get() method')
print(grocery_list.get('fruits'), ": get() method")
print('')
print(grocery_list.get('milk'), ": get() method")
print('')

# .items() method
print('.items() method')
print(grocery_list.items(), ": items() method")
print(' ')
print(grocery_list)
print('')
print(list(grocery_list.items())[1][0])
print(list(grocery_list.items())[1][1])
print(list(grocery_list.items())[1][1][0])
print('')

# .keys() method
print(".keys() method")
print(grocery_list.keys(), ": keys() method")
print('')
print(list(grocery_list.keys()), ": keys() method")
print('')

# .values() method
print(".values() method")
print(grocery_list.values())
print('')
print(list(grocery_list.values()))
print('')

# .pop() method
print(".pop() method")
print(grocery_list, ": Original")
print(grocery_list.pop('meat'), ": pop() method")
print(grocery_list, ": pop() method")
print('')

# .popitem() method
print(".popitem() method")
print(grocery_list, ": Original")
print(grocery_list.popitem()    , ": popitem() method")
print(grocery_list, ": After popitem() method")