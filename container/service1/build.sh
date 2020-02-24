#!/bin/bash
VERSION=v0.5.3

docker build -t h2so40627/service1:${VERSION} .
docker push h2so40627/service1:${VERSION}