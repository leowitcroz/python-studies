import pandas as pd   

df = pd.read_csv('hotel_booking\hotels.csv', dtype={'id': str})
df_cards = pd.read_csv('hotel_booking\cards.csv', dtype=str).to_dict(orient='records')
class Hotel:
    def __init__(self,hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, 'name'].squeeze()
    
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
    def __init__(self,customers_name,hotel_object):
        self.customers_name = customers_name
        self.hotel = hotel_object
        pass
    
    def generate(self):
        content = f"""
            Thank you for your reservation!!
            Here are your booking data:
            Name: {self.customers_name}
            Hotel name: {self.hotel.name}
        """
        return content
    
class Creditcard:
    def __init__(self, number):
        self.number = number
        
    def validate(self,expiration,holder,cvc):
        card_data = {'number':self.number, 'expiration':expiration, 'holder': holder, 'cvc':cvc}
        if card_data in df_cards:
            return True
        else:
            return False
    

print(df)

hotel_id = input('Enter de id of the hotel: ')

hotel = Hotel(hotel_id)
if hotel.avaliable():
    credit_card = Creditcard(number="1234567890123456")
    if credit_card.validate(expiration="12/26", holder="JOHN SMITH", cvc="123"):
        hotel.book()
        name = input('Enter your name: ')
        reservation_ticket = ReservationTicket(name,hotel) 
        print(reservation_ticket.generate())
else: 
    print('This hotel is not free')