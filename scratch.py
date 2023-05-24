def imp_cond():
    from app_sys1 import usr_prof
    print(prof)


get_u = input("Make selection: ")

if get_u == "Y":
    imp_cond()
else:
    print("import failed")
