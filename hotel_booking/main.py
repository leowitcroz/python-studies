import pandas as pd   

df = pd.read_csv('hotel_booking\hotels.csv', dtype={'id': str})
class Hotel:
    def __init__(self,hotel_id):
        self.hotel_id = hotel_id
    
    def book(self):
        df.loc[df["id"] == self.hotel_id, 'available'] = 'no'
        df.to_csv('hotel_booking\hotels.csv', index=False)
    
    def avaliable(self):
        availability = df.loc[df["id"] == self.hotel_id, 'available'].squeeze()
        if availability == 'yes':
            return True
        else: 
            return False
            
    


class ReservationTicket:
    def __init__(self,customers_name,hotel_id):
        pass
    
    def generate(self):
        pass
    

print(df)

hotel_id = input('Enter de id of the hotel: ')

hotel = Hotel(hotel_id)
if hotel.avaliable():
    hotel.book()
    name = input('Enter your name: ')
    reservation_ticket = ReservationTicket(name,hotel)
    reservation_ticket.generate()