import requests
import os
from dotenv import load_dotenv

load_dotenv()

MY_EMAIL = os.getenv("EMAIL")
MY_PASSWORD = os.getenv("PASSWORD")

MY_LAT = float(os.getenv("LAT"))
MY_LONG = float(os.getenv("LONG"))
