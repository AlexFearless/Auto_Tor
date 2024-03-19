# -*- coding: utf-8 -*-

import time
import os
import subprocess




try:
    check_pip3 = subprocess.check_output('dpkg -s python3-pip', shell=True)
    if str('install ok installed') in str(check_pip3):
        pass
except subprocess.CalledProcessError:
    print('[+] pip3 yüklü değil')
    subprocess.check_output('sudo apt update',shell=True)
    subprocess.check_output('sudo apt install python3-pip -y', shell=True)
    print('[!] pip3 başarıyla yüklendi')



try:

    import requests
except Exception:
    print('[+] python3 yüklü değil')
    os.system('pip3 install requests')
    os.system('pip3 install requests[socks]')
    print('[!] python3 yüklendi ')
try:

    check_tor = subprocess.check_output('which tor', shell=True)
except subprocess.CalledProcessError:

    print('[+] tor yüklü değil !')
    subprocess.check_output('sudo apt update',shell=True)
    subprocess.check_output('sudo apt install tor -y',shell=True)
    print('[!] tor başarıyla yüklendi ')

os.system("clear")
def ma_ip():
    url='https://www.myexternalip.com/raw'
    get_ip= requests.get(url,proxies=dict(http='socks5://127.0.0.1:9050',https='socks5://127.0.0.1:9050'))
    return get_ip.text

def change():
    os.system("service tor reload")
    print ('[+] Ip niz şu şekilde değiştirildi : '+str(ma_ip()))

print('''\033[1;32;40m \n
                _          _______
     /\        | |        |__   __|
    /  \  _   _| |_ ___      | | ___  _ __
   / /\ \| | | | __/ _ \     | |/ _ \| '__|
  / ____ \ |_| | || (_) |    | | (_) | |
 /_/    \_\__,_|\__\___/     |_|\___/|_|
                Fearless
Made By @Alex_Fearless
''')
print("\033[1;40;31m instagram=alex_fearless_\n")

os.system("tor servisi başladı")




time.sleep(3)
print("\033[1;32;40m SOCKES in şu şekilde değiştirildi 127.0.0.1:9050 \n")
os.system("tor başlatıldı")
x = input("[+] saniyede kaç kere ıp değişsin [örnek=60] >> ")
lin = input("[+] kaç kere ıp değişsin [örnek=1000]sınırsız ıp değişimi için [0] >>")
if int(lin) ==int(0):

	while True:
		try:
			time.sleep(int(x))
			change()
		except KeyboardInterrupt:

		 	print('\nauto tor kapandı ')
		 	quit()

else:
	for i in range(int(lin)):
		    time.sleep(int(x))
		    change()
