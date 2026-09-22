# Python Program for Handling Exceptions

# Declare a dict with british bands and their short description
BRIT_BANDS = {
    'The Beatles': 'are a British Pop Band',
    'The Rolling Stones': 'are a British Rock\'n\'Roll Band',
    'Cream' : 'are a British Blues Band',
    'Black Sabbath' : 'are a British Heavy Metal Band'
}

# Declare a function for processing bands, venues and instruments
def concert(band_name, band_genre, *venues, **instruments ):
    description = f'{band_name} are a {band_genre} band.'
    tour_venues = f'They are coming to: {venues}.'
    line_up = f'They consist of: {instruments}.'

    return description, tour_venues, line_up


# Block of Try..except..finally statements
try:
    for k, v in BRIT_BANDS.items():
        print(k, v) # accesses and prints dict contents
except NameError:
    print('variable is not defined.')
except TypeError:
    print('variable is of invalid type. Should be a string dictionary.')
except:
    print('An exception occurred.')
finally:
    print('Program exited successfuly.')

try:
    print(
        concert('The Beatles', 'Pop', 
                'London', 'Vienna', 'Stockholm', 
                vocals='John Lennon', bass='Paul McCartney', guitar='George Harrison',
                drums = 'Ringo Starr'
            )
    )
    
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
