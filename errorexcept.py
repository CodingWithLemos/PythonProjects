# Python Program for Handling Exceptions

# Define a function for processing bands, venues and artists
def concert(band_name, band_genre, *venues, **artists ):
    ''' Prints band and artist details provided by the user
        band_name (required): The name of the band 
        band_genre (required): The genre of the band 
        venues (arbitrary argument): What cities they will tour in
        artists (arbitrary argument): artist name and instrument '''

    print(f'{band_name} are a {band_genre} band.')
    print('They are coming to:')
    for venue in venues:
        print(venue)
    print('They consist of:')
    for key, value in artists.items():
        print(f'{key} ({value})')

try:
    band_name = 'The Beatles'
    band_genre = 'Pop'
    venues = ['London', 'Stockholm']
    artists = {
        'John Lennon' : 'Vocals',
        'Paul McCartney' : 'Bass',
        'George Harrison' : 'Guitar',
        'Ringo Starr' : 'Drums'
    }
# Unpack arguments upon function call (In this case venues and artists are expanded)
    concert(band_name, band_genre, *venues, **artists)
    
except NameError:
    print('variable is not defined.')
except TypeError:
    print('variable is of invalid type. Should be a function call.')
except ValueError:
    print('Argument is not of correct type. Check order of arguments.')
except:
    print('An exception occurred.')
finally:
    print('Program exited successfuly.')
