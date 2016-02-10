#!/bin/bash

f=$1
fname="${f##*/}"
r="${f##*.}"
d=$(date +%m-%d-%y)
new="${fname%.*}_$d.$r"
echo $new

