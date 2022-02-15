#### TRY IT YOURSELF - Chapter 8 - User Albums 
def make_album(artist_name, album_title):
    """Build dictionary with info about an album."""
    album = {'artist': artist_name.title(), 'title': album_title.title()}
    return album

while True:
    print("\nPlease tell me the name of an artist and an album you like:")
    print("(You can enter 'q' at anytime to quit)")
    artist = input("Artist name: ")
    if artist == 'q':
        break
    album = input("Album name: ")
    if album == 'q':
        break
    album_dict = make_album(artist, album)
    print(album_dict)