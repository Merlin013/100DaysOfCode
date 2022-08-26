import requests
from datetime import datetime
import smtplib
import pytz
import time

MY_LAT = 12.976325
MY_LNG = 77.595864
indian_time = pytz.timezone('Asia/Kolkata')
MY_EMAIL = "youremail@gmail.com"
MY_PASSWORD = "123456abcde()"


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LNG - 5 <= iss_longitude <= MY_LNG + 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,

    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = data["results"]["sunrise"]
    sunrise_time = datetime.strptime(sunrise, '%Y-%m-%dT%H:%M:%S%z')
    indian_sunrise_time = sunrise_time.astimezone(indian_time)
    sunrise_hour = indian_sunrise_time.hour
    print(indian_sunrise_time)
    print(sunrise_hour)

    sunset = data["results"]["sunset"]
    sunset_time = datetime.strptime(sunset, '%Y-%m-%dT%H:%M:%S%z')
    indian_sunset_time = sunset_time.astimezone(indian_time)
    sunset_hour = indian_sunset_time.hour
    print(indian_sunset_time)
    print(sunset_hour)

    time_now = datetime.now()
    current_time_hour = time_now.hour

    if current_time_hour >= sunset_hour or current_time_hour <= sunrise_hour:
        return True

while True:
    time.sleep(30)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject: Look UP\n\n The iss is above you in the sky."
        )
