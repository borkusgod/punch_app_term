# function file for punch app in termux dir
import os
from datetime import datetime
from text_file import *


# functions for system admin
def chk_fir():
    if os.path.exists(f'{system_drive}'):
        print("It appears you have run this program before")
    elif not os.path.exists(f'{system_drive}'):
        print(fresh_greeting)
        mk_init()


def mk_init():
    os.mkdir(system_drive)
    with open('./app_sys/init_set.txt', 'w') as writer:
        gt_tmstmp = dt_tm("year/date")
        writer.write(f'File initially created at {gt_tmstmp}')


# functions having to do with time and date
def dt_tm(option):
    # format so that you can pass args for results
    now_full = datetime.now()
    if option == "raw":
        return now_full
    elif option == "year/date":
        now_dt_tm = now_full.strftime(year_time)
        return now_dt_tm
    else:
        return "Invalid argument passed"


def append_usr_info():
    pass
