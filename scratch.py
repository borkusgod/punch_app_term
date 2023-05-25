#def imp_cond():
    #from app_sys1 import usr_prof
    #print(prof)


#get_u = input("Make selection: ")

#if get_u == "Y":
    #imp_cond()
#else:
    #print("import failed")
import os


def file_checker():
    import test_folder
    if os.path.exists('./test_folder/file2.txt'):
        print('file exists')
    else:
        print('file does not exist')


file_checker()
