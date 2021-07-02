from os import path,system
from sys import stdout

system('mv -r %s/hash /usr/bin/'%(path.abspath('')))
system('chmod +x /usr/bin/hash/*')
a =input('[-] Which Shell do you use [zsh, bash, etc]?: ')
f=open('/bin/%s'%(a));f.write('export PATH=$PATH:/usr/bin/hash');f.close()
print('\n[+] Installation Successful, run "hsh" to access RandHash ...")
