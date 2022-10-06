'''Create two class definitions

1) a Play class that has attributes for
id, name, number of seats, date and status. Set the value of
the status attribute to True as default. Create an accessor
method each for the name, seats and status attributes only. 
Create a method called 'seats_left' that will reduce the 
number of seats by 1 every time it is called.
Create a mutator method called 'set_status' that will
change the status attribute to False.

2) a Booking class that has attributes for customer name and
seat number. Create accessor methods for both attributes.'''
    
#a Play class that has attributes for id, name, number of seats, date and status

class Play:
    def __init__(self,id,name,seats,date):
        self.__id = id
        self.__name = name
        self.__seats = seats
        self.__date = date
        self.__status = True

#Create an accessor method each for the name, seats and status attributes only.
    #def get_ID (self):
        #return self.__id

    def get_name (self):
        return self.__name

    def get_seats (self):
        return self.__seats

    #def get_date (self):
        #return self.__date

    def get_status (self):
        return self.__status

#Create a method called 'seats_left' that will reduce the number of seats by 1 every time it is called.
    def seats_left(self):
        self.__seats -= 1

#Create a mutator method called 'set_status' that will change the status attribute to False.
    def set_status(self):
       self.__status = False

# Booking class that has attributes for customer name and seat number. Create accessor methods for both attributes.''
class Booking:
    def __init__(self,customer_name,seat_number):
         self.__customer_name = customer_name
         self.__seat_number = seat_number
    
#Create accessor methods for both attributes.''' 
    def get_name(self):
        return self.__customer_name
    def get_seat_number(self):
        return self.__seat_number
        


