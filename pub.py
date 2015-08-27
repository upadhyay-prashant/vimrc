import zmq
import time
import sys
import random

port="7272"
context=zmq.Context()
socket=context.socket(zmq.PUB)
socket.bind("tcp://*:%s"%port)
while True:
    topic=random.randrange(9999,10005)
    messageData=random.randrange(1,215)-80
    print "%d %d" %(topic,messageData)
    socket.send("%d %d" %(topic, messageData))
    time.sleep(1)
