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
        self.marks=marks
    def p_details(self):
        if super().get_role() == 'I':
            print('\n{} can be reached at {}'.format(super().get_name(),super().get_email()))


Subrat = Software_lab('Subrat','subrat@iit','I')
Subrat.p_details()


