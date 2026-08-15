# password strength checker python program

# import sys built-in module
import sys

# change content of sys.argv[1] with password provided by user
password = sys.argv[1]

# use nested ifs to verify the strength of the password
pw_strength = int(len(password))

# check password strength and prints apropriate message
if pw_strength < 8:
    print('weak password strength.')
elif pw_strength >= 8 and pw_strength < 12:
    print('decent password strength.')
elif pw_strength >= 12 and pw_strength < 16:
    print('good password strength.')
else: 
    print('strong password, good job!')

