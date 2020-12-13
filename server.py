#!/usr/bin/env python

import asyncio		#asynchronous
import datetime		#get time stamp
import random		#make random number
import websockets		#main stuff
import dateutil.parser
count = 0;
async def myServ(ws, path):

    while True:
        time1 = datetime.datetime.now()
        
        
        
        now = 'e1801151 ' + time1.isoformat()
        
        await ws.send(now)
        await asyncio.sleep(1 + random.random() * 3)
        time2 = datetime.datetime.now()
        
        time3 = time2 - time1
        await ws.send('time difference between messages: ' + str(time3))
        global count
        count=count+1                         
        await ws.send('number of messages since server start ' + str(count))
     

start_server = websockets.serve(myServ, 'HOST_IP', PORT)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
