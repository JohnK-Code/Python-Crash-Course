#### TRY IT YOURSELF - Chapter 8 - Album
def make_album(artist_name, album_title, num_songs=None):
    """Build dictionary with info about an album."""
    album = {'artist': artist_name.title(), 'title': album_title.title()}
    if num_songs:
        album['tracks'] = num_songs
    return album

albums = make_album('eminem', 'curtain call')
print(albums)

albums = make_album('50 cent', 'the kanan tape')
print(albums)

albums = make_album('wu tang clan', '36 chambers')
print(albums)

albums = make_album('nas', 'illmatic', 10)
print(albums)