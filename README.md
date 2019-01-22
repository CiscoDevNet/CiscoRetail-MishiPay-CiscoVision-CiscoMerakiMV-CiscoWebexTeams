# CiscoRetail-MishiPay-CiscoVision-CiscoMerakiMV-CiscoWebexTeams
 Cisco Retail integration for Theft Detection solution including Mishipay, Cisco Vision, Cisco Meraki MV and Cisco Webex Teams

This is part of a project that the Cisco DevNet team was involved in with several Cisco BUs and Cisco partners in preparation for NRF 2019. The main purpose of this application is to integrate several different technologies to provide a theft detection solution for the retail industry.

## Requirements
To use this application you need:
* Python 3.7+
* Nedap RFID scanner (optional, see below)
* Cisco Meraki MV camera
* Cisco Vision

Ideally you have access to a Nedap RFID scanner that generates messages whenever an item in the retail store has not been paid. But if you do not have access to Nedap hardware, do not despair. You can simulate the RFID scanner behavior by using an MQTT topic (i.e. nrf2019/unpaid) to which you would continuously publish messages similar to the one below:

`{"time": 1547348535.8938448, "id": "303402328019380004100001", "item": "Kleenex Ultra Soft Facial Tissue - 75ct"}`

The Python application looks for specific names in the "item" values and interacts with a Cisco Vision server to trigger a specific action within Cisco Vision. In this case, a trigger that displays an image of the product that is specified in the "item" value is displayed on a Cisco Vision controlled screen that is placed in the check out area of the store notifying the person that holds the item that it needs to be payed before exiting the store.

At the same time, the `webbrowser` Python library is used to open up a Cisco Meraki MV dashboard tab in the default browser at the "timestamp" specified in the MQTT message. The camera that is ideally placed in the check out area of the store should be used so that a video recording of the person trying to walk out with the unpaid item is recorded.

The application also sends a Cisco Webex Teams message with the Cisco Meraki MV dashboard link from above to a
space that contains security personnel interested

## Install and Setup
Clone the code on your local machine:

`git clone https://github.com/aidevnet/CiscoRetail-MishiPay-CiscoVision-MerakiMV.git`

`cd CiscoRetail-MishiPay-CiscoVision-MerakiMV`

Setup Python Virtual Environment (requires Python 3.7+)

`python3.7 -m venv venv`

`source venv/bin/activate`

`pip install -r requirements.txt`

## Using the application
Once cloned the repo, you can run the application with:
`python mqtt01.py`

## Technologies used

The following technologies were used as part of this demo:
* Cisco Meraki MV camera
* Cisco Vision
* Cisco Webex Teams
* Nedap RFID scanner/MQTT topic
* Mishipay technology

As a Cisco partner, Mishipay can help Cisco customers integrate their own solutions with the Mishipay online paying platform.
