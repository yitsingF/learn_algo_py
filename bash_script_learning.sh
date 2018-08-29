#!/bin/base
# this is a bash script 
# variables
a="a b c d"
# loop 
for i in $a:
do
    echo $i
done

# linux null blockhole

server_pid=`ssh resin@$host "ps -ef | grep $project_name | grep -v grep | awk '{printf\"%s\", \\$2}'"`
# list all running(-e) process in a brief mode(-f)
ps -ef
# print all(-a) process in details(-u) even that does not effect terminal excution(-x)
ps -aux | less