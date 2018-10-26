# trading_zmq
[![Build Status](https://travis-ci.org/F2011B/trading_zmq.svg?branch=master)](https://travis-ci.org/F2011B/trading_zmq)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/3adf2edc1bd242e394058ebaf924fff0)](https://app.codacy.com/app/F2011B/trading_zmq?utm_source=github.com&utm_medium=referral&utm_content=F2011B/trading_zmq&utm_campaign=Badge_Grade_Dashboard)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

## Python trading framework using zeromq 

A publisher is used to deliver data to the first subscriber.
The first subscriber hands filtered data to the next consumer. 
This way a minimum latency should be established between receiving 
data and the final trading decision. 
