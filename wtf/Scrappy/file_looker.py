import os

shot = input("Shot number:")

# Go to the @shot folder
try:
    os.chdir("/home/sjo/Documents/daisuki/COMPASS/RE_27.1.2020/%s" % shot)
except:
    print("No folder, no data")

path = os.path.dirname(os.path.realpath(__file__))

for f_name in os.listdir(path):
    if f_name.startswith('file') and f_name.endswith('.dat'):
        print('found a match')