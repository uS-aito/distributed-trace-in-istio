#!/bin/bash
VERSION=v0.4.1

docker build -t h2so40627/service2:${VERSION} .
docker push h2so40627/service2:${VERSION}