fav_vgame = {
    'Andrea': 'Stradew Valley',
    'Bill' : 'Super Smach Bros',
    'Tom' : 'God of War',
    'Jose' : 'Hogwarts Legacy',
    'Mina' : 'Pokemon Gold'
}
print('')
# One Iterator for loop
print('One Iterator for loop')
print(fav_vgame)
print('')
for key in fav_vgame:
    print(key, ": Original \n")

for key in fav_vgame.keys():
    print(key.lower(), ": Lowercase")
print('')
print('')

# build-in function .sort() method
print("")
for key in sorted(fav_vgame):
    print(key, ": Sorted")

print('')

#.values() method
print(".values() method")
for values in fav_vgame.values():
    print(values)

print('')
# .items() method
for key, value in fav_vgame.items():
    print(f"\nkey: {key}")
    print(f"value: {value}")