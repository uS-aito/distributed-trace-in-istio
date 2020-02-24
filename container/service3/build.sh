#!/bin/bash
VERSION=v0.1.1

docker build -t h2so40627/service3:${VERSION} .
docker push h2so40627/service3:${VERSION}