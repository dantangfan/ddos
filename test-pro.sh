#!/bin/bash

for i in {1..5};
do
    python proxy-ddos.py http:// &
    echo $i
done

sleep 30

kill `pgrep python`
