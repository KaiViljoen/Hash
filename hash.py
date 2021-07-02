# Written and Published by @Tenjin979 on Github.

#!/usr/bin/python3
from hashlib import __all__
from sys import argv,stdout; from sys import exit
from time import sleep
from random import choice, random

help ='Usage:\n\t Example: hsh md5 hashvalue\n\t Example: hsh sha_512 hashvalue\n\t Example: hsh random'

#Narrow down usable hashes
x=[i for i in __all__ if i.startswith('s') or i.startswith('m')]
x=[i for i in x if not 'k' in i]

#Typing Animation
def type(seq):
    for char in seq: 
        stdout.write(char)
        stdout.flush()
        sleep(0.005)
        
#Parameter Conditions
try: 
    global hsh
    hsh=argv[1]
    if hsh=='random':
        exec('from hashlib import %s'%(choice(x)))
    else: 
        global chrseq
        chrseq=argv[2]
except IndexError: 
    print(help);exit()

# Parameter Processing
try:
   if hsh in x:
       exec('from hashlib import %s'%(hsh))
       x=globals()[hsh](chrseq.encode('utf-8')).hexdigest();type(x+'\n')
   elif hsh not in x: 
       if hsh=='random':
         type(globals()[list(globals().keys())[-1]](f'%i'.encode('utf-8')%(random()**-200)).hexdigest()+'\n')
       else:
           print('[%s]'%(hsh));type('\nUnsupported or Invalid Hash-Type ...\n');print(help)
except KeyError: type('Unsupported Hash-Type ...\n')
