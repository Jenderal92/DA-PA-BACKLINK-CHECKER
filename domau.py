#!/usr/bin/python
# -*- coding: utf-8 -*
# Ma Friendo : JametKNTLS - h0d3_g4n - Moslem - Jenderal92 -Kiddenta
# Blog : https://www.blog-gan.org          
#MINIMAL DONATE LAH ANJING ! 
	# BTC = 31mtLHqhaXXyCMnT2EU73U8fwYwigiEEU1
	# PERFECT MONEY  = U22270614 )
##############################
#KALAU RECODE JANGAN CUMA HAPUS AUTHOR NGENTOT !
#IF RECODE DON'T JUST DELETE THE AUTHOR FUCKING !
##############################
import requests,re,os,time
from multiprocessing import Pool as ThreadPool
from colorama import Fore,Style, init
init(autoreset=True)

r = Fore.RED + Style.BRIGHT
g = Fore.GREEN + Style.BRIGHT
c = Fore.CYAN + Style.BRIGHT
b = Fore.BLUE + Style.BRIGHT
y = Fore.YELLOW + Style.BRIGHT
o = Fore.RESET + Style.RESET_ALL


#url = 'http://kontol.com'

def DOMAUT(url):
	try:
		headers = {
		'User-Agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 9 Pro Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36',
		}
		DAPA = requests.post('https://m5d.net/da-pa-check.php',data = {'q': url}, headers=headers,timeout=30)
		if 'Domain Name' in DAPA.text:
			RES = re.findall("</span> (.*?)</p>",DAPA.text)
			print(url +' [ '+ 'DA: '+b+ RES[1] +o+'PA: '+c+ RES[2] +o+'BC: '+y+ RES[3]+' ] '+o)
			open('mantep.txt','a').write('\n--------------- JANCOK -------------\n'+url+'\nDA: '+ RES[1] +'PA: '+ RES[2] +'BACKLINK: '+ RES[3] +'\n')
		else:
			print ('Shin_Code')
	except:
		pass
		
print "{} DA/PA/BACKLINK CHECKER  | Shin Code\n".format(y)
url = open(raw_input(o+'List:~# '),'r').read().replace('http://','').replace('https://','').splitlines()
pool = ThreadPool(int(1))
pool.map(DOMAUT, url)
pool.close()
pool.join()
print('')
print('Saved in mantep.txt')