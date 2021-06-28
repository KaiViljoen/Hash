# Written by @Tenjin979
#!/usr/bin/python3

from hashlib import __all__
from random import randrange, choice
from sys import stdout
from time import sleep

# type output to screen
def type(seq):
  for char in seq:
    stdout.write(char)
    stdout.flush()
    time.sleep(0.05)
    
    
# Pseudo-random generate hash
def random():
  ''' Import correct hashes and make them usable and importable, 
      import only specefied hash upon usage and encypt and type
      pseudo-random number recursively '''
  
  # Append all usefull hashtypes to local import list    
  a=[l for l in a if l.startswith('s') or if l.startswith('m')];a =[l for l in a if 'k' not in l]; a.append(__all__)
  exec('from hashlib import %s'%(random(a)))
  globals()[random(a)](randrange(1,10**100).hexdigest()
