import csv
import os

shot = input("Shot number:")

# Go to the @shot folder
try:
    os.chdir("/home/sjo/Documents/daisuki/COMPASS/RE_27.1.2020/%s" % shot)
except:
    print("No folder, no data")

with open('%s.csv' %shot) as f:
    reader = csv.reader(f, delimiter=',', skipinitialspace=False)
    first_row = next(reader)
    num_cols = len(first_row)

