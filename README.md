# CENG435 TERM PROJECT PART 1

In this project we are sending data from source to destination with UDP and TCP.As and data we are sending time from source and when that time reaches to destination we are getting current time. After getting difference of two time data we are finding end-to-end delay between source and destination.

## NTP Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install NTP.

```bash
pip install NTPlib
```


## Usage of NTP

```python
import NTPlib

c = ntplib.NTPClient()   # returns NTPClient
response = c.request('time.google.com') # returns response from time.google.com
time = response.tx_time #return current time as an timestamp
```

## Source.py

Source.py gets time with NTP and sends it to the Broker with TCP.

## Broker.py

Broker.py gets packets from Source with TCP and sends them to the Routers with UDP.

## Router1.py and Router2.py

Routers gets packets from Broker with UDP and sends it to the Destination with UDP.

## Destination.py

Destination.py gets packets from Routers with UDP and gets time with NTP and take difference between times and prints end-to-end delay between Source and Destination.