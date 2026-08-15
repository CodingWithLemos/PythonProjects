# Age in months calculator Python program

# Import sys to accept module arguments from terminal
import sys

# Initialize age variable and let n read sysargv array size
age = 1
n = len(sys.argv)

# With sysargv convert age input into months
for i in range(age, n):
    age_months = int(sys.argv[i]) * 12
    print('Your age in months:', age_months) # Print message to the terminal