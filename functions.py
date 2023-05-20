# function file for punch app in termux dir
import os
from datetime import datetime
from text_file import *
from app_sys.usr_vars import *


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


def create_usr_prof():
    # testing container
    tmp_cont = []
    # make funcs for each element of prof
    # name first and last
    gt_fname = input(fn_txt)
    tmp_cont.append(gt_fname)
    gt_lname = input(ln_txt)
    tmp_cont.append(gt_lname)
    
    # email
    gt_email = input(ea_txt)
    tmp_cont.append(gt_email)
    
    # phone number
    gt_phone = input(pn_txt)
    tmp_cont.append(gt_phone)
    
    # desired username, check against rules, previous, etc
    gt_uname = input(un_txt)
    tmp_cont.append(gt_uname)
    for each in tmp_cont:
        print(each)
