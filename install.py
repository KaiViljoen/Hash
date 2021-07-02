from os import path,system
from sys import stdout

system('mv -r %s/hash /usr/bin/'%(path.abspath('')))
a =input('[-] Which Shell do you use [zsh, bash, etc]?: ')
f=open('/bin/%s'%(a),a);f.write('export PATH=$PATH:/usr/bin/hash')
print('\n[+] Installation Successful, run "hsh" to access RandHash ...")
