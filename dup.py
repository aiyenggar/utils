import os
import re
""" 
Renames the filenames by adding a prefix
Usage:
python dup.py
"""
path =  os.getcwd()
mypath = "/Users/anu/Pictures/" 
filenames = os.listdir(mypath)
for filename in filenames:
    filen, filee = os.path.splitext(filename)
    nfile = "20170516_" + filen.lower().title() + filee.lower()
#    print(filename + ", " + nfile)
    os.rename(mypath+filename, mypath+nfile)

# find . -name '*.*' -type f -exec bash -c 'base=${0%.*} ext=${0##*.} a=$base.${ext,,}; [ "$a" != "$0" ] && mv -- "$0" "$a"' {} \;

