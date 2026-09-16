# CSV file reader python program

# imports
import pandas as pd

# new dataframe
df = pd.read_csv('csv/LCD_sample_csv.csv')

# prints csv file contents to the console
print(df.to_string()) 