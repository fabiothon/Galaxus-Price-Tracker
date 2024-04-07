# =============================================================================
# PRICE TRACKER FOR GALAXUS
# =============================================================================

# This application aims to do the following things:
# - Track price of specific products on www.galaxus.ch
# - Automatic tracking interval should be 24h
# - Alert user via email if the price reaches a defined price level

# Libraries
from loguru import logger
from bs4 import BeautifulSoup
import requests
import smtplib
import keyring
# import pandas as pd


# Variables
product = "Helm"
product_url = "https://www.galaxus.ch/en/s3/product/giro-agilis-mips-55-59-cm-bike-helmets-12392463"
alert_price = float(10.0)
price = None #Initalisation of price
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:88.0) Gecko/20100101 Firefox/88.0"}

email = keyring.get_password("Notification_Mail_Name", "Notification_Mail_Name")
password = keyring.get_password("Notification_Mail", "Notification_Mail")

# Function
def scrape():
    try:
        page = requests.get(product_url, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        price = float(soup.find(attrs={'sc-125c42c7-5 hMyxKO'}).get_text())
        return price
        if(price < alert_price):
            send_mail()
        logger.success("Successfully scraped website")
        
    except requests.exceptions.RequestException as e:
        logger.error(f"Request failed: {e}")
    except AttributeError as e:
        logger.error(f"Attribute error: {e}")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login(email, password)
    
    subject = f"ALERT! Price for {product} is low!"
    body = f"Checkout the Product via this Link: {product_url}"
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        email,
        email,
        msg
        )
    
    server.quit
    logger.success("Mail sent.")
    
    
scrape() 
    

        

    

# logger.info("An info message.")
# logger.success("A success message.")
# logger.warning("A warning message.")
# logger.error("An error message.")