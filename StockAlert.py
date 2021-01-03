import json
import sys
import time
import urllib.request
import urllib.parse

import requests
import ssl
from datetime import datetime

ssl._create_default_https_context = ssl._create_unverified_context

# body = '{"itemIds":[2711946,2711945,2711944]}'
# requests.post()
condition = True

jsonBody = json.load(open("body.json"))


def getTime():
    # datetime object containing current date and time
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    return dt_string


def sendSMS(apikey, numbers, sender, message):
    data = urllib.parse.urlencode({'apikey': apikey, 'numbers': numbers,
                                   'message': message, 'sender': sender})
    data = data.encode('utf-8')
    request = urllib.request.Request("https://api.textlocal.in/send/?")
    f = urllib.request.urlopen(request, data)
    fr = f.read()
    return (fr)


def sendsms():
    resp = sendSMS('IsPafd7m9pc-Fuft6ZgSMoNkZGttzH30RG14IEeWGI', '916382143117',
                   '', 'Triban RC120 is back in Stock!')

    # if resp.status_code == 200:
    #     sys.exit("Stock Reported!")
    # if resp.status_code != 200:
    print(resp)

def waitAndCheck():
    while True:


        try:
            resp = requests.post(url='https://www.decathlon.in/api/product/stocks', json=jsonBody)
        except Exception as e:
            print(e.__str__())

        if resp.status_code != 200:
            print(resp.json())

        if resp.json()['status'] is False:
            print(getTime() + ' : No Stock!')
            print('Waiting..(300)')
            time.sleep(300)

        if resp.json()['status'] is True:
            print(getTime() + ' : STOCK AVAILABLE! SENDING SMS!')
            try:
                sendsms()
            except:
                sendsms()


waitAndCheck()
