import sys
import zmq
import collections

port = "5556"
if len(sys.argv) > 1:
    port = sys.argv[1]
    int(port)
    
if len(sys.argv) > 2:
    port1 = sys.argv[2]
    int(port1)

# Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)

print("Collecting updates from weather server...")
socket.connect ("tcp://localhost:%s" % port)

if len(sys.argv) > 2:
    socket.connect("tcp://localhost:%s" % port1)
    
# Subscribe to zipcode, default is NYC, 10001
socket.setsockopt_string(zmq.SUBSCRIBE, '')

# Process 5 updates
total_value = 0

avlist = collections.deque(maxlen=10)
while True:
    string = socket.recv().decode("utf-8", "strict")      
    if string.split()[0] == 'EUR_USD':
        avlist.append(float(string.split()[2].split('/')[0]))
        print(sum(i for i in avlist)/10)