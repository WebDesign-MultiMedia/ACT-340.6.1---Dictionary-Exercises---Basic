playlist = {
    "Jay-Z": "99 Problems",
    "Kendrick Lamar": "Humble",
    "Lil Wayne": "A Milli",
    "Drake": "In My Feelings",
    "Cardi B": "Bodak Yellow",
    "Kanye West": "Gold Digger"
}

# Use a for loop to create a print statement that prints all the artists in the playlist
print("Artists in the playlist:")
for key in playlist:
    print(key)
print('')
# Use a for loop to create a print statment that prints all the songs in the playlist
print("\nSongs in the playlist:")
for pairs in playlist:
    print(playlist[pairs])

print('')
# Use a for loop to create a print statement that says: "(Song Name) by (Artist) is in the current playlist."
for key, value in playlist.items():
        print(f"{key} by {value}")
print('')

# Remove the last Key:Value pair from the Dictionary
print("Original Playlist: \n" , playlist)
print('')
print(playlist.pop('Kanye West'))
print(playlist, ": After pop() method")
print('')

# Add the song "Anti-Hero" by Taylor Swift to your playlist.
print(playlist, ": Original")
playlist["Taylor Swift"] = "Anti-Hero"
print(playlist, ": Added")
print('')

# Overwrite one of your songs to have REMIX in front of the song title
print(playlist, ": Original")
playlist["Jay-Z"] = "REMIX 99 Problems"
print(playlist, ": Updated")

print('')
# Define & call a function that will print all the artists and songs from the object you pass into it.
def print_playlist():
    for key, value in playlist.items():
        print(f"{key} by {value}")
print_playlist()

     