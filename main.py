# =============================================================================
# PRICE TRACKER FOR GALAXUS
# =============================================================================

# This application aims to do the following things:
# - Track price of specific products on www.galaxus.ch
# - Automatic tracking interval with cronjob: 24h
# - Alert user via email if the price reaches a defined price level

# Libraries
from loguru import logger
from bs4 import BeautifulSoup
import requests
import keyring
import base64
from email.mime.text import MIMEText
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from requests import HTTPError
import pandas as pd

# Variables
price = None #Initalisation of price
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:88.0) Gecko/20100101 Firefox/88.0"}
credentials = 'credentials.json'
password = keyring.get_password("Notification_Mail_PW", "Notification_Mail_PW")

# Grab data
try:
    df = pd.read_csv('products.csv')
    logger.success("Successfully loaded data")
except Exception as e:
    logger.error(f"An error occurred: {e}")
    
# Function
def scrape():
    try:
        page = requests.get(product_url, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        price = float(soup.find(attrs={'sc-125c42c7-5 hMyxKO'}).get_text())
        logger.success("Successfully scraped website")
        return price
        
    except requests.exceptions.RequestException as e:
        logger.error(f"Request failed: {e}")
    except AttributeError as e:
        logger.error(f"Attribute error: {e}")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
    return None

def send_mail():
    SCOPES = ["https://www.googleapis.com/auth/gmail.send"]
    flow = InstalledAppFlow.from_client_secrets_file(credentials, SCOPES)
    creds = flow.run_local_server(port=0)
    
    service = build('gmail', 'v1', credentials=creds)
    message = MIMEText(f"Check the product ({product}) out via this link: {product_url}\nGreetings!")
    message['to'] = email
    message['subject'] = f"ALERT! Price for {product} is low!"
    create_message = {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}
    
    try:
        message = service.users().messages().send(userId="me", body=create_message).execute()
        logger.success(f"Sent message to {email}. Message Id: {message['id']}")
    except HTTPError as error:
        logger.error(f"An HTTP error occurred: {error}")
        message = None
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        message = None

# For-loop to check all rows of the data
logger.info("Main loop started.")
for index, row in df.iterrows():
    product = row['product']
    product_url = row['url']
    alert_price = row['alert_price']
    email = row['email']
    
    price = scrape()
    if price is not None and price < alert_price:
        send_mail()
logger.info("Main loop ended.")