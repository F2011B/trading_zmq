[![Build Status](https://travis-ci.org/F2011B/trading_zmq.svg?branch=master)](https://travis-ci.org/F2011B/trading_zmq)

## Python trading framework using zeromq 

A prublisher is used to deliver data to the first subscriber.
The first subscriber hands filtered data to the next consumer. 
This way a minimum latency should be established between receiving 
data and the final trading decision. 
