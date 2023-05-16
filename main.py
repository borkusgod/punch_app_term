# main file for punch app in term dir
# this app will function as an app to keep 
# track of your time punched for work 
# and we'll output to several formats

from functions import *
from text_file import *

print(now_raw()[1])
x = now_raw()[0]
x_formed = x.strftime("%Y, %B %d, -- %H:%M:%S")
print(x_formed)
print('\n')

print(greeting)


