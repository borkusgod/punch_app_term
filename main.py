# main file for punch app in term dir
# this app will function as an app to keep 
# track of your time punched for work 
# and we'll output to several formats

from functions import *
from text_file import *

print(dt_tm("year/date"))
print('\n')
if chk_fir():
    print("It looks like you have run the app before.")

