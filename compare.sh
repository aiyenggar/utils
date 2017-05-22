#!/bin/bash

file1=`md5 $1 | awk '{print $4}'`
file2=`md5 $2 | awk '{print $4}'`

if [ "$file1" == "$file2" ]
then
    echo "Files are identical"
else
    echo "Files are different"
fi
