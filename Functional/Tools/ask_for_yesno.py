# =============================================================================
# A script for asking yes/no used in other scripts for manual control of the
# algorithm flow
# =============================================================================
import sys

yes = {'yes','y','ye',''}
no = {'no','n'}

choice = input().lower()
if choice in yes:
   True
elif choice in no:
   False
else:
   sys.stdout.write("Please respond with 'yes' or 'no'")
   
# Put this cell in a loop
print("Figure exists, do you wish to continue anyway?")
ques = input("Type 'y' or 'n': ")
if ques == 'y':
    pass
else:
    continue