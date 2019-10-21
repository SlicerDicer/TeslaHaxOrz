#!/bin/bash

if grep --quiet Greg /etc/motd; then
  echo "motd updated, noice"
else
  rm /etc/motd
  touch /etc/motd
  echo "motd not updated, fixing now"
  echo "Linux cid 4.4.35-release-03mar2017-g352318b-dirty armv7l GNU/Linux" >> /etc/motd
  echo "Hey Elon, The dolphin is not working. " >> /etc/motd
  echo "Tesla Model S, Its magically Rootsauce." >> /etc/motd
  echo "Call Greg, dont mess with this car." >> /etc/motd
fi
