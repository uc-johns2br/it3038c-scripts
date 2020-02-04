#!/bin/bash
#This script will email us our user, IP, hostname and today's date.
emailaddress=brettjohnson791@gmail.com
today=$(date +"%d-%m-%Y")
ip=$(ip a | grep 'dynamic ens192'|awk '{print $2}')
content="User $USER"
hostname="Hostname: $HOSTNAME"
mail -s "IT3038C Linux IP" $emailaddress <<< $(echo -e $content " from " $ip " on " $today " running machine type of " $MACHTYPE  " with hostname " $HOSTNAME ".")
