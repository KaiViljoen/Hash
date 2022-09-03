#Author @Github.com/KaiViljoen/
#!/usr/bin/python3

from os import path,system,getcwd,chdir,listdir
from sys import stdout
from time import sleep
from getpass import getuser as user

chdir('/home/%s'%(user()))
global x
x=list(listdir())
x=[a for a in x if a.endswith('rc')]

def display(seq):
    for char in seq:
        stdout.write(char)
        stdout.flush()
        sleep(0.015)
def main():
    chdir('/home/%s'%(user())) if x[0]!=path.abspath(getcwd()) else None
    display('\033[0;34;40m[+] \033[0;37;40mWelcome to the Hash.py installer ...\n')
    display('\nWhat would you like to do ? [install/uninstall]: ')
    a=input()
    if a =='install':

         install()
    elif a =='uninstall':
        system('sudo rm -rf /usr/bin/hsh /usr/bin/hash.py /home/$USER/Hash/')
        display('\033[0;31;40m[-] \033[0;37;40mHash Generator Uninstalled ...\n')
    else:
        print('[-] TF did you do?? ... Exit code 1 ...')
        exit(1)

def install():
    if path.exists('/home/%s/Hash/hash/hsh'%(user())):
         pass
    else:
         system('clear')
         display('\033[0;31;40m[-] \033[0;37;40mFatal installation files missing ...\n\033[0;31;40m[-] Please redownload files from Github @KaiViljoen/Hash/\n')
         exit(1)
        #Move files and assign rwx permissions
    system('sudo cp -f /home/$USER/Hash/hash/hash.py /home/$USER/Hash/hash/hsh /usr/bin/ && sudo chown -R $USER /usr/bin/hsh /usr/bin/hash.py && sudo chmod g+rwx,u+rwx /usr/bin/hsh /usr/bin/hash.py')

    #add files to PATH permanently.
    chdir('/home/%s'%(user()))
    if path.exists(x[0]):
       system('echo "export PATH=/usr/bin/hash.py" >> ~/.{sh}rc && echo "export PATH=/usr/bin/hsh" >> ~/.{sh0}rc'.format(sh=x[0],sh0=x[0]))
       system('sudo rm -rf /home/$USER/Hash/hash')
       display('\033[0;34;40m[+] \033[0;37;40mInstallation Complete ...\n\033[0;34;40m[+] \033[0;37;40mRun "hsh" command to access ...\n')
       exit(0)
    else:
         print('\033[0;31;40m[-] Installation Unsuccessful ...')
         exit()
    print('\n[+] Installation Successful, "hsh" command active ...' )

"""
def repair(): # still working on this one but it's slightly more complex than I initially thought...
    display('[+] Repair underway ...')
    uninstall()
    system('cd /home/$USER/ && git clone https://github.com/KaiViljoen/Hash/ && sudo chown -R $USER Hash && cd Hash')
    system('sudo chmod u+rwx,g+rwx install.py')
"""

main()
