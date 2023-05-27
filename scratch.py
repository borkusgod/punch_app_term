from datetime import datetime


def make_dps(how_many):
    test_cont = []
    date_cont = []
    day = how_many
    for each_day in range(5):
        made_time = datetime(2023, 5, day, 10, 30, 00)
        test_cont.append(made_time)
        day += 1
    for each in test_cont:
        print(each)
    print(type(test_cont[0]))

day_start = int(input("what day to start: \n"))        
make_dps(day_start)
