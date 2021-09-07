import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

print("[+] Dextools Bot Starting")
driver = webdriver.Firefox()
url = "https://www.dextools.io/app/pancakeswap/pair-explorer/0xef1c8dcd81f2980d5ca1879b2665e8d04e7185be"
driver.get(url)
print("[+] Go for settings. You have 120 seconds!!")
#time.sleep(120)
x = input("[+] Time to refresh Dextools in Sec [type=5] >> ")
time.sleep(5)

def ma_ip():
    url='https://www.myexternalip.com/raw'
    get_ip= requests.get(url,proxies=dict(http='socks5://127.0.0.1:9050',https='socks5://127.0.0.1:9050'))
    return get_ip.text

while True:
    driver.get(url)
    print ('[+] Your IP was for this refresh : '+str(ma_ip()))
    time.sleep(x)