#!/bin/bash

read -p "enter new password : " a
echo $a >> lock.txt
cp lock.txt /data/data/com.termux/files/home


