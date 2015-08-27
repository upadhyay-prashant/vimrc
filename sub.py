import sys
import zmq
port = "7272"
context=zmq.Context()
socket=context.socket(zmq.SUB)
print "collecting updates "
socket.connect("tcp://172.31.20.113:%s"%port)
topicfilter="10001"
socket.setsockopt(zmq.SUBSCRIBE,topicfilter)
total_value=0
for update_nbr in range(5):
    string=socket.recv()
    topic,messagedata = string.split()
    total_value+=int(messagedata)
    print topic, messagedata
