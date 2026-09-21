# Python Program for Handling Exceptions

# Declare a dict with british bands and their short description
BRIT_BANDS = {
    'The Beatles': 'are a British Pop Band',
    'The Rolling Stones': 'are a British Rock\'n\'Roll Band',
    'Cream' : 'are a British Blues Band',
    'Black Sabbath' : 'are a British Heavy Metal Band'
}

# Declare a function for processing bands, venues and stuff


# Block of Try..except.finally statements
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