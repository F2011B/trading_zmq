# trading_zmq
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/3adf2edc1bd242e394058ebaf924fff0)](https://app.codacy.com/app/F2011B/trading_zmq?utm_source=github.com&utm_medium=referral&utm_content=F2011B/trading_zmq&utm_campaign=Badge_Grade_Dashboard)

[![Build Status](https://travis-ci.org/F2011B/trading_zmq.svg?branch=master)](https://travis-ci.org/F2011B/trading_zmq)

## Python trading framework using zeromq 

A publisher is used to deliver data to the first subscriber.
The first subscriber hands filtered data to the next consumer. 
This way a minimum latency should be established between receiving 
data and the final trading decision. 
