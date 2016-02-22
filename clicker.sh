# !/bin/bash

sleep 2

while [ 1 ]; do
    for i in {1..200} 
    do
        xdotool mousemove $1 $2 click 1
        sleep 0.03
    done
  sleep 2
done

#Get position: $ xdotool getmouselocation

