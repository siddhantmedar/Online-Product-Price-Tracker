#Importing libraries
import requests
from bs4 import BeautifulSoup
from twilio.rest import Client

#create track function
def track():
    #Replace the below URL with the desired product's link, which you would like to track
    URL="https://www.amazon.in/Vivo-Aqua-Blue-Storage-Offer/dp/B07KX1KY5S/ref=sr_1_2?crid=3CZZ6ZE8NLYJV&keywords=vivo+z1+pro+mobile&qid=1567698076&s=gateway&sprefix=%27vivo+z1%2Caps%2C366&sr=8-2"

    headers={
        "user-agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
    }

    page=requests.get(URL,headers=headers)

    parse=BeautifulSoup(page.content,'html.parser')

    title=parse.find(id='productTitle').get_text()

    fetched_price=parse.find(id='priceblock_ourprice').get_text()

    def edit_price(fetched_price):
        mod_price=fetched_price.split()
        new_price=[i for i in mod_price if i not in ('₹',',',' ')]
        new_price=[i.split('.')[0] for i in new_price]
        string=''.join(new_price)
        value=string.replace(",","")
        return value

    def mail():
        account_sid = 'ADD TWILIO SID HERE'
        auth_token = 'ADD TWILIO AUTH TOKEN HERE'
        client = Client(account_sid, auth_token)
        #Add message in body section
        message = client.messages \
                    .create(
                        body="Price fell down! Go shop now https://www.amazon.in/Vivo-Aqua-Blue-Storage-Offer/dp/B07KX1KY5S/ref=sr_1_2?crid=3CZZ6ZE8NLYJV&keywords=vivo+z1+pro+mobile&qid=1567698076&s=gateway&sprefix=%27vivo+z1%2Caps%2C366&sr=8-2",
                        from_='FROM NUMBER',
                        to='TO NUMBER'
                    )
        print(message.sid)
        print("The message have been sent!")

    final_price=edit_price(fetched_price)

    if final_price<'19990':
        mail()



