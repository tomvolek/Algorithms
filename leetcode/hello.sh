#!/bin/bash
echo "$0"
echo "$1" 
echo "$*"
read -p "Mai ask your name:" name
echo "Hello $name"
if [ $# -gt 1 ] ;  then
   echo "Usage: $0 <name>"
   exit 1 
fi 
exit 0

