# =============================================================================
# PRICE TRACKER FOR GALAXUS
# =============================================================================

# This application aims to do the following things:
# - Track price of a specific product on www.galaxus.ch
# - Automatic tracking interval should be 24h
# - Alert user via email if the price reaches a defined price level

# Libraries
from loguru import logger
import beautifulsoup
import pandas as pd
# from requests_html import AsyncHTMLSession
# from price_parser import Price

# Variables
product_url = "https://www.galaxus.ch/en/s3/product/giro-agilis-mips-55-59-cm-bike-helmets-12392463"
alert_price = 100


