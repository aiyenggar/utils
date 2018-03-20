import os
import re
""" 
(1) Remove leading 00 in files
Usage:
python rename.py
"""
path =  os.getcwd()
mypath = "/Volumes/My Passport for Mac/OneDrive/test"
filenames = os.listdir(mypath)
for filename in filenames:
    filen, filee = os.path.splitext(filename)
    t1=re.sub(r'[\^_():;]',r' - ', filen)
    t2=re.sub(r'[^A-Za-z0-9\- ]+', r'', t1)
    t2b=re.sub(r'[\-]+', r' ', t2)
    t2c=re.sub(r'^\d\d ', r' ', t2b)
    t3=re.sub( '\s+', ' ', t2c).strip()
    t4=re.sub(r'^[^A-Za-z0-9]*', '', t3)
    nfile = t4.lower().title() + filee.lower()
    print(filename + ", " + nfile)
#    os.rename(mypath+filename, mypath+nfile)

# find . -name '*.*' -type f -exec bash -c 'base=${0%.*} ext=${0##*.} a=$base.${ext,,}; [ "$a" != "$0" ] && mv -- "$0" "$a"' {} \;

