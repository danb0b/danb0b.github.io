---
title: Web-Based Control in Micropython
tags:
- python
- micropython
- microdot
summary: ""
---


## Step 1: Create a Form that posts to URL


### Good resources

- <https://how2electronics.com/raspberry-pi-pico-w-web-server-tutorial-with-micropython/>
- <https://www.geeksforgeeks.org/understanding-html-form-encoding-url-encoded-and-multipart-forms/#GFG_AD_gfg_mobile_336x280>


## Step 2: Back-end python code that can parse the input form data.
- <https://developer.mozilla.org/en-US/docs/Learn/Forms/Sending_and_retrieving_form_data>

- using post method allows us to enter data from the form rather than the url bar.  keeps the address bar clean
- using the GET method allows us ot enter commands directly from address bar
    - however the method includes the referal url which has the old data in it, so you must do a better job of parsing the request string. 
- or you can use microdot as seen below

### Some resources

- <https://randomnerdtutorials.com/esp32-esp8266-micropython-web-server/>


## Implementation of Step 1 & 2

```python
# import libraries
import os
import time
import ubinascii
import machine
import micropython
import esp
esp.osdebug(None)
import gc
gc.collect()
import upip
from machine import Pin


try:
  import usocket as socket
except:
  import socket

import network

import esp
esp.osdebug(None)

import gc
gc.collect()


import network
# set wifi information
ssid     = '<enter-ssid-here>'
wifi_password  = '<enter-password-here>'

#create station instance
station = network.WLAN(network.STA_IF)

#set active
station.active(True)

# if the station is not connected,
if not station.isconnected():
    # connect the station with ssid and password
    station.connect(ssid, wifi_password)

# wait until the station is connected
while station.isconnected() == False:
  pass


# print connection successful
print('Connection successful')

# print full connection information 
print(station.ifconfig())


# import upip

# if 'lib' in os.listdir('./'):
#     if 'microdot' not in os.listdir('lib/'):
#     # install the micropython logging library
#         upip.install('microdot')
#         os.rename('lib/src','lib/microdot')
#         with open('lib/microdot/__init__.py','w') as f:
#            f.write('')


led = Pin(2, Pin.OUT)


template = '''
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <title>URL Encoded Forms</title>
  </head>
  <body>
    <form
      method="POST"
      enctype="application/x-www-form-urlencoded">
      <input type="text" name="led" value="{led_value}" />
      <input type="text" name="password" value="GFG@123" />
      <input type="submit" value="Submit" />
    </form>
  </body>
</html>
'''

def web_page(led_value = ""):
  if led.value() == 1:
    gpio_state="ON"
  else:
    gpio_state="OFF"
  html = template.format(led_value=led_value)
  return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  request = str(request)
  print('Content = %s' % request)
  if request.find('led=1') > -1:
    print('LED ON')
    led.value(1)
  if request.find('led=0') > -1:
    print('LED OFF')
    led.value(0)
  response = web_page(led_value=str(led.value()))
  conn.send('HTTP/1.1 200 OK\n')
  conn.send('Content-Type: text/html\n')
  conn.send('Connection: close\n\n')
  conn.sendall(response)
  conn.close()

```

## Step 3: alternatively Microdot based api can be used to create quick apps

https://bhave.sh/micropython-microdot/
https://github.com/bhavesh-k/micropython-bamboo/blob/main/main.py

I used this approach to create this simpmle script:

```python
import network
# set wifi information
ssid     = '<enter-ssid-here>'
wifi_password  = '<enter-password-here>'

#create station instance
station = network.WLAN(network.STA_IF)

#set active
station.active(True)

# if the station is not connected,
if not station.isconnected():
    # connect the station with ssid and password
    station.connect(ssid, wifi_password)

# wait until the station is connected
while station.isconnected() == False:
  pass


# print connection successful
print('Connection successful')

# print full connection information 
print(station.ifconfig())


import uasyncio
from microdot_asyncio import Microdot


# setup webserver
app = Microdot()

@app.route('/')
async def hello(request):
	return 'Hello world'


from machine import Pin
led = Pin(2, Pin.OUT)

def set_servo(value):
    led.value(int(value))

    print('setting servo value: ',value)

@app.get('/servo')
async def servo(request):
    set_servo((int(request.args['v'])))
    return 'OK'


def start_server():
    print('Starting microdot app')
    try:
        app.run(port=80)
    except:
        app.shutdown()

start_server()
```

## External resources

### Other microdot info

- <https://www.donskytech.com/how-to-create-a-micropython-web-server-the-easy-way/>
- <https://www.donskytech.com/microdot-micropython-handling-dynamic-content/>
- <https://microdot.readthedocs.io/en/latest/intro.html#running-with-micropython>
- <https://microdot.readthedocs.io/en/latest/api.html#microdot-asyncio-module>

### Fetch API

- <https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Fetching_data>
- <https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API>

## Asyncio info

- <https://github.com/miguelgrinberg/microdot/issues/17>
- <https://github.com/miguelgrinberg/microdot/issues/19>
- <https://stackoverflow.com/questions/62528272/what-does-asyncio-create-task-do>


## External Links

- <https://stackoverflow.com/questions/4007969/application-x-www-form-urlencoded-or-multipart-form-data>
- <https://stackoverflow.com/questions/4007969/application-x-www-form-urlencoded-or-multipart-form-data#4073451>
- <https://duckduckgo.com/?q=microdot+URLencoded+form+data+example>
- <https://stackoverflow.com/questions/11556958/sending-data-from-html-form-to-a-python-script-in-flask#11566296>
- <https://forum.micropython.org/viewtopic.php?t=4013>
- <https://www.petecodes.co.uk/creating-a-basic-raspberry-pi-pico-web-server-using-micropython/>
- <https://microdot.readthedocs.io/en/latest/index.html>