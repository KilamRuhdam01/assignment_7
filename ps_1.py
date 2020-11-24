class Lab:
    def __init__(self, name, email, role):
        self.__name=name
        self.__email=email
        self.__role=role

    def get_name(self):
        return self.__name
    def get_email(self):
        return self.__email
    def get_role(self):
        return self.__role
    def set_name(self,name):
        self.__name = name
    def set_role(self, role):
        return self.__role
    def details(self):
        print("\n{}({}) at {}\n".format(self.__name,self.__role,self.__email))

#software_lab = Lab('Madhur', 'eet@iitd.ac', 'S')

#software_lab.details()

class Software_lab(Lab):
    def set_marks(self,marks):
        if marks >=0:
            self.marks=marks
        else:
            print('Wrong marks entered, they cant be negative')
    def p_details(self):
        if super().get_role() == 'I':
            print('\n{}({}) can be reached at {}\n'.format(super().get_name(),super().get_role(),super().get_email()))
        elif super().get_role() == 'S':
            print('\n{} got {} marks\n'.format(super().get_name(), str(self.marks)))
        else:
            print('\nThe role is incorrect please correct it using set_role() method. \n')

subrat = Software_lab('Subrat','subrat@iit','I')
subrat.p_details()
madhur = Software_lab('Madhur', 'eet2757@iit', 'S')
madhur.set_marks(99)
madhur.p_details()

sonal = Software_lab('Sonal', 'eet2757@iit', 'T')
sonal.p_details()

