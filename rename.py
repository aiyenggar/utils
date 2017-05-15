import os
import re
""" 
Renames the filenames within the same directory to be Unix friendly
(1) Changes spaces to hyphens
(2) Makes lowercase (not a Unix requirement, just looks better ;)
Usage:
python rename.py
"""
path =  os.getcwd()
mypath = "/Users/anu/sangeetham/" 
filenames = os.listdir(mypath)
for filename in filenames:
    filen, filee = os.path.splitext(filename)
    t1=re.sub(r'[\^_():;]',r' - ', filen)
    t2=re.sub(r'[^A-Za-z0-9\- ]+', r'', t1)
    t3=re.sub( '\s+', ' ', t2).strip()
    t4=re.sub(r'^[^A-Za-z]*', '', t3)
    nfile = t4.lower().title() + filee.lower()
#    print(filename + ", " + nfile)
    os.rename(mypath+filename, mypath+nfile)

# find . -name '*.*' -type f -exec bash -c 'base=${0%.*} ext=${0##*.} a=$base.${ext,,}; [ "$a" != "$0" ] && mv -- "$0" "$a"' {} \;

