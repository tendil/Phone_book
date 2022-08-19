import sys
import csv
class Human:
    def __init__(self, name=None, last_name=None, address=None, phone_number=None, from_line=None):
        if from_line is None:
            self.name = name
            self.last_name = last_name
            self.address = address
            self.phone_number = phone_number
        # else:
        #     self.name, self.last_name, self.address, self.phone_number = str(from_line)

        def __str__(self):
            return f'Human: {self.name}, {self.last_name},\nAddress: {self.address},\nPhoneNumber: {self.phone_number}'

    def input_characters(self):
        self.name = input("Enter name: ").capitalize()
        self.last_name = input("Enter last name: ").capitalize()
        self.address = input("Enter address: ").capitalize()
        while True:
            try:
                self.phone_number = input("Enter phone number: ")
                if not self.phone_number.isdigit():
                    raise Exception
                print(self.phone_number)
                break
            except Exception as e:
                print('\nInvalid input!!! Only digit\'s!')


class Contacts:

    # def find_human(self, query=None):
    #     with open('date.csv') as file:
    #         for line in file:
    #             human = Human(from_line=line)
    #             if human.last_name == query:
    #                 return human
    #             if human.phone_number == query:
    #                 return human
    def add_human(self):
        h = Human()
        h.input_characters()
        #if c.find_human(query=(h.name, h.last_name)) is None:
        with open('date.csv', 'a+') as file:
            writer = csv.writer(file)
            first_line = file.readline(0)

            if not str(('name', 'last name', 'address', 'phone number')) in first_line:
                writer.writerow(('name', 'last name', 'address', 'phone number'))

            lst = [(h.name, h.last_name, h.address, h.phone_number)]
            for i in lst:
                with open('date.csv', 'a') as file:
                    writer = csv.writer(file)
                    writer.writerow(lst)
            print(f'\nContact {h.name} {h.last_name} successfully added.)\n')



    def deleted_contacts(self, query):
        pass
        # f = open('base.txt', 'r')
        # line = f.readlines()
        # f.close()
        # f = open('base.txt', 'w')

        # for line in f.readline():
        #     human = Human(from_line=line)
        #     objects.append(human)
        # for object in objects:
        #     if (human.last_name, human.name) != query:
        #         f.write(object.__str__())

    def show_all_contacts(self):
        with open('date.csv') as file:
            reader = csv.reader(file)
            for line in reader:
                human = Human(from_line=line)
            #     # result = enumerate(file.readlines())
                print(f"{human}" + '-' * len(line))

def choice():
    sel = None
    try:
        sel = int(input('Search - "1"\n'
                        'New contact - "2"\n'
                        'Show all phone book - "3"\n'
                        'Deleted contact - "4"\n'
                        'Edit contact - "5"\n'
                        'EXIT - "0"\n'
                        '\nEnter --->: '))
    except ValueError:
        print('\n\nInvalid input!!!')
        print('You must enter an integer!!!\n\n')
    return sel


c = Contacts()

while True:
    sel = choice()
    if sel == 1:
        query = (input('To search for a contact, enter his full name or phone number: ').capitalize())
        #print(c.find_human(query))

    elif sel == 0:
        sys.exit()

    elif sel == 2:
        c.add_human()

    elif sel == 3:
        c.show_all_contacts()

    elif sel == 4:
        query = ((input('To delete a contact, enter his last name and name: ').capitalize()))
        c.deleted_contacts(query)

    elif sel == 5:
        pass