
class Person:
    
    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone

    def get_name(self, name):
        self.__name = name

    def get_address(self, address):
        self.__address = address

    def get_phone(self, phone):
        self.__phone = phone

    def print_person(self):
        print('Name:', self.__name)
        print('Address:', self.__address)
        print('Phone:', self.__phone)

class Customer(Person):
    
    def __init__(self, name, address, phone, customer_num, on_list):
        Person.__init__(self, name, address, phone)
        self.__customer_num = customer_num
        self.__on_list = on_list


    def print_person(self):
        print('Name:', Person.get_name(self))
        print('Address:', Person.get_address(self))
        print('Phone:', Person.get_phone(self))

        print()
        print()

        Person.print_person(self)
        
        print('Cusotmer number:', self.__customer_num)
        if self.__on_list:
            print('On mailing list: Yes' )
        else:
            print('On mailing list: No' )


