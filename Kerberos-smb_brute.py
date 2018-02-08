#!/usr/bin/python
import os
# Code By Miguel Mendez Z.
# info: https://www.attackdebris.com/?p=364 | https://www.attackdebris.com/?p=311

logo = '''
  _             _                         ___                  _     
 | | _____ _ __| |__   ___ _ __ ___  ___ ( _ )   ___ _ __ ___ | |__  
 | |/ / _ \ '__| '_ \ / _ \ '__/ _ \/ __|/ _ \/\/ __| '_ ` _ \| '_ \ 
 |   <  __/ |  | |_) |  __/ | | (_) \__ \ (_>  <\__ \ | | | | | |_) |
 |_|\_\___|_|  |_.__/ \___|_|  \___/|___/\___/\/|___/_| |_| |_|_.__/  
 @s1kr10s
'''

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()
print logo

BLUE = '\033[94m'
RED = '\033[1;31m'
BOLD = '\033[1m'
GREEN = '\033[32m'
ENDC = '\033[0m'

print RED+BOLD+" Recomendacion: \n Obtener Dominio con "+ENDC+BOLD+GREEN+"[Responder.py] "+ENDC

nomx=[]
apex=[]
nombres = file("nombres.txt", "r")
apellid = file("apellidos.txt", "r")
abc = 'abcdefghijklmnopqrstuvwxyz'

for nom in nombres:
	nom = nom.rstrip()
	nomx.append(nom)
for ape in apellid:
	ape = ape.rstrip()
	apex.append(ape)

op = input('\n Elija una opcion para crear el Diccionario:\n\n 1) [(inicial)nombre][apellido]\n 2) [(inicial)nombre].[apellido]\n 3) [nombre].[apellido]\n\n '+BLUE+'Opcion?: '+ENDC)
if op == 1:
	#[ini-nombre][apellido]
	nomfile='iniape.txt'
	for d in abc:
		for a in apex:
			word=d+a.lower()
			f=open(nomfile,'a')
			f.write(word+'\n')
	f.close()
elif op == 2:
	#[ini-nombre][apellido]
	nomfile='ini.ape.txt'
	for d in abc:
		for a in apex:
			word=d+'.'+a.lower()
			f=open(nomfile,'a')
			f.write(word+'\n')
	f.close()
elif op == 3:
	#[nombre].[apellido]
	nomfile='nom.ape.txt'	
	for n in nomx:
		for a in apex:
			word=n+'.'+a.lower()
			f=open(nomfile,'a')
			f.write(word+'\n')

	f.close()

msfkrb = raw_input('\n '+BLUE+'Desea ejecutar auxiliar kerberos_enumusers (Y/n): '+ENDC)
if msfkrb == 'y':
	domain = raw_input(' Ingrese Domain: ')
	rhost  = raw_input(' Ingrese Rhost : ')
	os.system('msfconsole -x "use auxiliary/gather/kerberos_enumusers;set USER_FILE '+nomfile+';set DOMAIN '+domain+';set RHOST '+rhost+';run;creds;exit"')

	msfsmb = raw_input('\n '+BLUE+'Desea ejecutar auxiliar smb_login (Y/n): '+ENDC)
	if msfsmb == 'y':
		cls()
		userfile  = raw_input('\n '+BLUE+'+User_File : '+ENDC)
		os.system('msfconsole -x "use auxiliary/scanner/smb/smb_login;set RHOSTS '+rhost+';set SMBDomain '+domain+';set USER_FILE '+userfile+';run"')
