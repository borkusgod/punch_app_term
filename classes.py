# class file for punch app in term dir

class Person:
    def __init__(self,
                f_name,
                l_name,
                age,
                p_number,
                em_add,
    ):
        self.firstName = f_name
        self.lastName = l_name
        self.age = age
        self.phoneNumber = p_number
        self.emailAddress = em_add
        
    def messageTest(self):
        print('Test output')
        