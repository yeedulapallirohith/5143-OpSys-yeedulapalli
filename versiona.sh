#!/bin/bash
echo $1
d=$(date +"%Y-%m-%d"_"$1")
cp "$1" "$d"

