#!/bin/bash

docker run --name service1 --network distributed-trace -d -p 8080:8080 h2so40627/service1:v0.5.3 python /root/service1.py 8080