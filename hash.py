# Written by @Tenjin979
#!/usr/bin/python3

from hashlib import __all__
from random import randrange, choice
from sys import stdout, argv
from time import sleep

# type output to screen
def type(seq):
  for char in seq:
    stdout.write(char)
    stdout.flush()
    time.sleep(0.005)
    
    
# Pseudo-random generate hash
def random(hashtype=None, array=None):  
   # Append all usefull hashtypes to local import list    
   a=[l for l in a if l.startswith('s') or if l.startswith('m')];a =[l for l in a if 'k' not in l]; a.append(__all__)
   try:
       if hashtype ==None:
         x=choice(a)
         exec('from hashlib import %s'%(x))
       elif hashtype !=None:
          x=hashtype
          exec('from hashlib import %s'%(x))
       else: pass
    except Error as e:
          type('Unsupported Hash-Type ...')
    v=globals()[x](f'%i'.encode('utf-8')%(randrange(1,10**100))).hexdigest() # generate call
    if array !=None: array.append(v)
    else: print(x)

hash =argv[1]
if hash =='random': random()
elif hash!='random': pass
