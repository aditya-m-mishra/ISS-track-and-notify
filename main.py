import requests
import os
from dotenv import load_dotenv

load_dotenv()

MY_EMAIL = os.getenv("EMAIL")
MY_PASSWORD = os.getenv("PASSWORD")

MY_LAT = float(os.getenv("LAT"))
MY_LONG = float(os.getenv("LONG"))


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")

    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if (
        MY_LAT - 5 <= iss_latitude <= MY_LAT + 5
        and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5
    ):
        return True
