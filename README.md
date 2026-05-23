# 🛰️ ISS Track & Notify

A simple Python automation project that tracks the International Space Station (ISS) and sends an email notification when it is overhead during nighttime at your location.

## 🚀 Features

* Live ISS tracking using APIs
* Detects when ISS is near your coordinates
* Checks if it is nighttime
* Sends automated email alerts
* Uses `.env` for secure credentials

## 🛠️ Tech Stack

* Python
* Requests
* smtplib
* python-dotenv
* Open Notify API
* Sunrise-Sunset API

## ⚙️ Setup

```bash
git clone https://github.com/aditya-m-mishra/ISS-track-and-notify.git
cd ISS-track-and-notify
pip install -r requirements.txt
```

Create a `.env` file:

```env
MY_LAT=your_latitude
MY_LONG=your_longitude
EMAIL=your_email@gmail.com
PASSWORD=your_app_password
```

Run the project:

```bash
python main.py
```

