import requests
import time
from bs4 import BeautifulSoup
import smtplib
import lxml

URL = "https://www.amazon.co.uk/Apple-Airpods-Wireless-Charging-latest/dp/B07PYM8FB8/ref=sr_1_6?keywords=airpods&qid=1581244893&sr=8-6"
HEADERS = {'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0"}
WANTED_PRICE = 160
EMAIL_ADDRESS = "email@gmail.com"

def trackPrice():
    price = int(getPrice())
    if price > WANTED_PRICE:
        diff = price - WANTED_PRICE
        print(f"It's still {diff} too expensive")
    else:
        print("Cheaper!")
        #sendEmail()

def getPrice():
    page = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(page.content, 'lxml')

    # Product Title
    title = soup.find(id="priceblock_ourprice").get_text().strip()
    
    # Product Price
    price = soup.find(id="priceblock_ourprice").get_text().strip()[1:4]

    print(title)
    print(price)
    return price

def sendEmail():
    subject = "Amazon Price Dropped!"
    mailtext='Subject:'+subject+'\n\n'+URL

    server = smtplib.SMTP(host='smtp.gmail.com', port=587) # Use gmail with port 587
    # Note for gmail, you must turn on "Less secure app access" on gmail accouunt
    server.ehlo() #identifies self to server
    server.starttls() #enable security
    server.login(EMAIL_ADDRESS, 'Password') #login to email
    server.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, mailtext) #Sends email
    print("Mail Sent")

if __name__ == "__main__":
    while True:
        trackPrice()
        time.sleep(10)