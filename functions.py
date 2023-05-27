import os  # ./term_pys/punch_app_term/functions.py
from datetime import datetime
from text_file import *


# functions for system admin


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


def chk_fir():
    import app_sys
    if os.path.exists('./app_sys/usr_prof.py'):
        print("It appears you have run this program before\n")
        ask_if = input("Would you like to log in?\n")
        if ask_if == "y" or ask_if == "Y" or ask_if == "1":
            login()
        else:
            print('return to main system menu')
    elif not os.path.exists('./app_sys/usr_prof.py'):
        print(fresh_greeting)
        create_usr_prof()
        # load_usr_prof()
        # mk_init()


def login():
    from app_sys.usr_prof import prof
    get_username = input("Please type your username: ")
    if get_username == prof[4]:
        get_password = input('Now please enter your password: ')
        if get_password == prof[5]:
            print("You are logged in! Now to main screen")
            main_screen()


# functions having to do with time and date


def create_usr_prof():
    user_info_cont = []
    # name first and last
    gt_fname = input(fn_txt)
    user_info_cont.append(gt_fname)
    gt_lname = input(ln_txt)
    user_info_cont.append(gt_lname)

    # email
    gt_email = input(ea_txt)
    user_info_cont.append(gt_email)

    # phone number
    gt_phone = input(pn_txt)
    user_info_cont.append(gt_phone)

    # desired username, check against rules, previous, etc
    gt_uname = input(un_txt)
    user_info_cont.append(gt_uname)

    gt_password = input(ps_txt)
    user_info_cont.append(gt_password)

    for each in user_info_cont:
        print(each)

    with open("./app_sys/usr_prof.py", "w") as user_prof_create:
        get_list = str(user_info_cont)
        make_var = f'prof = {get_list}'
        user_prof_create.write(make_var + '\n\n')


def main_screen():
    # start blocking out components for main screen and break into pieces
    # below is windos
    #os.system('cls')
    os.system('clear')
    print(wel_mn)
    main_st = True
    while main_st is True:
        gt_choice = input('Please enter the number that corresponds to the choices above: \n')
        if gt_choice == "1":
            #print('You selected option 1')
            add_tp()
            #main_st = False
        elif gt_choice == "2":
            print('You selected option 2')
            edit_tp()
            #main_st = False
        elif gt_choice == "3":
            print('You selected option 3')
            delete_tp()
            #main_st = False
        elif gt_choice == "4":
            print('You selected option 4')
            exit_app()
            #main_st = False
    
    # time punch screen
    # time edit screen
    # time review screen
    # exit screen


def time_puncher():
    get_now = datetime.now()
    made_time = datetime(2023, 5, 26, 20, 52, 00)
    print(get_now)
    print(made_time)

def add_tp():
    print("Print from add_tp() function")
    time_puncher()


def edit_tp():
    print("Print from edit_tp() function")


def delete_tp():
    print("Print from delete_tp() function")


def exit_app():
    print("Print from exit_app() function")    
