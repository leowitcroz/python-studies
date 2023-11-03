import pandas as pd   

df = pd.read_csv('hotel_booking\hotels.csv')
class Hotel:
    def __init__(self,id):
        pass
    
    def book(self):
        pass
    
    def avaliable(self):
        pass
    


class ReservationTicket:
    def __init__(self,customers_name,hotel):
        pass
    
    def generate(self):
        pass
    

print(df)

id = input('Enter de id of the hotel')

hotel = Hotel(id)
if hotel.avaliable():
    hotel.book()
    name = input('Enter your name: ')
    reservation_ticket = ReservationTicket(name,hotel)
    reservation_ticket.generate()