# function file for punch app in termux dir

# function to check if app has ever 
# been run before 
from datetime import datetime
import os
from text_file import *


# functions for system admin
def chk_fir():
    sys_fld = './app_sys'
    if os.path.exists(f'{sys_fld}'):
        print("ini file found")
    elif not os.path.exists(f'{sys_fld}'):
        print("Program has not been run before")
        mk_init()


def mk_init():
    with open('./app_sys/init_set.txt', 'w') as writer:
        gt_tmstmp = now_raw()
        writer.write(f'File initially created at {gt_tmstmp}')


# functions having to do with time and date
# format so that you can pass args for results
def now_raw():
    now_full = datetime.now()
    now_dt_tm = now_full.strftime(year_time)
    return now_full, now_dt_tm
