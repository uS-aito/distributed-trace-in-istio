#!/bin/bash

docker run --name service2 --network distributed-trace -d -p 8081:8081 h2so40627/service2:v0.4.1 python /root/service2.py 8081