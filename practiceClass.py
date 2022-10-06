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
    def __init__(id,name,seats,date,status):
        self.id = id
        self.name = name
        self.seats = seats
        self.date = date
        self.status = TRUE

#Create an accessor method each for the name, seats and status attributes only.
    def accessor1(self):
        return self.name
        return self.seats
        return self.status

#Create a method called 'seats_left' that will reduce the number of seats by 1 every time it is called.
    def seats_left(self):
        self.seats -= 1

#Create a mutator method called 'set_status' that will change the status attribute to False.
    def set_status(self):
        self.status = FALSE


# Booking class that has attributes for customer name and seat number. Create accessor methods for both attributes.'''
class Booking:
    def __init__(customer_name,seat_number):
        self.customer_name = customer_name
        self.seat_number = seat_number
    
#Create accessor methods for both attributes.''' 
    def accessor2(self):
        return self.customer_name
        return self.seat_number
        