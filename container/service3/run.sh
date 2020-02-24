#!/bin/bash

docker run --name service3 --network distributed-trace -d -p 8082:8082 h2so40627/service3:v0.1 python /root/service3.py 8082