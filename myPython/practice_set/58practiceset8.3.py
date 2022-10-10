
#8.6
def city_country(city,country):
    output = f"{city.title()}, {country.title()}"
    return output

name = city_country('jabalpur','india')
name1 = city_country('california','united states')
name2 = city_country('tokyo','japan')
print(name)
print(name1)
print(name2)

#------------------------------------------------------------------------------------------
#8.7
# 1)
def make_album(artist,alname):
    album  = {'artist':artist.title(),'album_name':alname.title()}
    return album

a = make_album('honey singh','jaadu ki jhappi')
print(a)
b = make_album('zara','jaadu')
print(b)

# 2)
def make_album(artist,alname,number_of_songs = None):
    if number_of_songs:
        album = {'artist':artist,'album name':alname,'number of songs':number_of_songs}
        return album
    else:
        album = {'artist':artist,'album name':alname}
        return album

a = make_album('honey','how are you',5)
b = make_album('sonny','abcdfu')
print(a)
print(b)

#------------------------------------------------------------------------------------------
#8.8

def make_album(artistname,alname):
    album = {'artist':artistname.title(),'album_name':alname.title()}
    return album

print("\nEnter the name of artist and album below:")
print("You can press 'q' to quit the program.")
while True:
    artist = input("Enter the name of artist: ")
    if artist == 'q':
        break
    album = input("Enter the name of album: ") 
    if album == 'q':
        break 
    c = make_album(artist,album)
    print(c)

#------------------------------------------------------------------------------------------