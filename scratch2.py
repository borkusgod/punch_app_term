def py_writer():
    with open("./tester.py", "w") as py_r:
        txt_output = "var_test = [1, 2, 3]"
        py_r.write(txt_output)


