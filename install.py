#Written by @Tenjin979 and posted to Github.
#!/usr/bin/python3

from os import path,system,getcwd
from sys import stdout

z=['zsh','bash','sh']

#Move files and assign execute permissions.
system('mv %s/hash/hash/ /usr/bin/'%(getcwd()))
system('chmod +x /usr/bin/hash/*')

#add files to PATH permanently.
for i in z: 
    if path.exists('%s/%s'%(getcwd(),i)): 
       f=open('%s/.%rc'%(getcwd(),i)
       f.write('export PATH=$PATH:/usr/bin/hash/')
       f.close()
    else: 
         print('[-] Installation Unsuccessful, please report this to the Developer on Github @Tenjin979 ...')
         exit()
print('\n[+] Installation Successful, run "hsh" to access RandHash ...")
