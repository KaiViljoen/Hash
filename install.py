#Written by @Tenjin979 and posted to Github.
#!/usr/bin/python3

from os import path,system,getcwd,chdir,listdir
from sys import stdout
from getpass import getuser as user

#Move files and assign rwx permissions.
system('sudo rm -rfv /usr/bin/hash && sudo mv -f /home/$USER/Hash/hash/* /usr/bin/ && sudo chown -R $USER /usr/bin/hsh /usr/bin/hash.py && sudo chmod g+rwx,u+rwx /usr/bin/hsh /usr/bin/hash.py')

#add files to PATH permanently.
chdir('/home/%s'%(user()))
x=list(listdir())
x=[a for a in x if a.endswith('rc')]
if path.exists(x[0]):
   system('echo export PATH=/usr/bin/hash.py >> ~/.{sh}rc && echo PATH=/usr/bin/hsh >> ~/.{sh0}rc'.format(sh=x[0],sh0=x[0]))
   system('rm -rf /home/$USER/Hash/hash/')
   print('[+] Installation Complete ...\n [+] Run "hsh" command to access...')
   exit(0)
else:
     print('[-] Installation Unsuccessful ...')
     exit()
print('\n[+] Installation Successful, "hsh" command active ...' )
