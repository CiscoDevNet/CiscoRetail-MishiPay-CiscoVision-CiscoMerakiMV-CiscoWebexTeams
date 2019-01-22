#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import webbrowser
import json
import requests
import datetime as dt
import sys
import os
import getopt
from random import randint

CISCO_VISION_DMP_URL = 'http://10.99.1.10:8080/StadiumVision/ws/rest/trigger/input/'
BOT_TOKEN = ''
TEAMS_ROOM = ''
MERAKI_MV_LINK = 'https://n118.meraki.com/CiscoNRF2019/n/gvPRvc2b/manage/nodes/new_list/57548244007525?timespan=86400&timestamp='

def send_it(token, room_id, message):

        header = {"Authorization": "Bearer %s" % token,
                  "Content-Type": "application/json"}

        data = {"roomId": room_id,
                "text": message}

        return requests.post("https://api.ciscospark.com/v1/messages/", headers=header, data=json.dumps(data), verify=True)

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe("nrf2019/unpaid")

def on_message(client, userdata, msg):
    m_decode=str(msg.payload.decode("utf-8","ignore"))
    m_in=json.loads(m_decode)
    timestamp = str(m_in["time"]).split('.')[0] + str(random_with_N_digits(3))
    print("timestamp = ",timestamp)
    webbrowser.open(MERAKI_MV_LINK + timestamp, new=0)
    print("Yes!")
    product_id = str(m_in["item"])
    if "Benadryl" in product_id:
        result = requests.get(url = CISCO_VISION_DMP_URL + '1')
        print(result.status_code)
    elif "Crest" in product_id:
        result = requests.get(url = CISCO_VISION_DMP_URL + '2')
        print(result.status_code)
    elif "Harry's" in product_id:
        result = requests.get(url = CISCO_VISION_DMP_URL + '3')
        print(result.status_code)
    elif "ThermaCare" in product_id:
        result = requests.get(url = CISCO_VISION_DMP_URL + '4')
        print(result.status_code)
    elif "Clorox" in product_id:
        result = requests.get(url = CISCO_VISION_DMP_URL + '5')
        print(result.status_code)
    else:
        result = requests.get(url = CISCO_VISION_DMP_URL + '7')
        print(result.status_code)
    
    res = send_it(BOT_TOKEN, TEAMS_ROOM, str(dt.datetime.now()) + "\n" + MERAKI_MV_LINK + timestamp)
    if res.status_code == 200:
        print("your message was successfully posted to Webex Teams")
    else:
        print("failed with statusCode: %d" % res.status_code)
        if res.status_code == 404:
                print ("please check the bot is in the room you're attempting to post to...")
        elif res.status_code == 400:
                print ("please check the identifier of the room you're attempting to post to...")
        elif res.status_code == 401:
                print ("please check if the access token is correct...")    
    
client = mqtt.Client()
client.connect("mqtt.cisco.com",1883,60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
