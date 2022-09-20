from flask import Flask
import requests
from bs4 import BeautifulSoup
import time
import smtplib

HEADERS = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Safari/605.1.15"}

def inputInfos(input_url,input_price,input_mail):
    return trackPrice(input_url,input_price,input_mail)

def trackPrice(url,price,mail):
    actual_price = getPrice(url)
    diff = actual_price - int(price)
    if actual_price <= int(price):
        sendMail(url,mail)
        return "Prix actuellement inférieur de {:0.2f}€, un mail vous a été adressé. Commandez vite !".format(abs(diff))
    else: return "Prix actuellement {:0.2f}€ trop élevé, nous vous notifierons lorsqu'il sera plus bas.".format(diff)

def getTitle(url):
    page = requests.get(url, headers = HEADERS)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id='productTitle').get_text().strip()
    return title

def getPrice(url):
    page = requests.get(url, headers = HEADERS)
    soup = BeautifulSoup(page.content, 'html.parser')
    for el in soup.find_all('div',{'class':'a-section a-spacing-small'}):
        price = soup.select_one('.a-offscreen').get_text().strip()
    price = int(price.translate(translation))
    price = price//100 + (price%100)/100
    return price

translation = dict.fromkeys(map(ord, '.,$€£'), None)

def sendMail(url,mail):
    subject = "Prix Bas pour {}".format(' '.join(getTitle(url).split()[:4]))
    mailtext = "Subject: "+subject+"\n\n"+url

    server = smtplib.SMTP(host="smtp-mail.outlook.com", port=587)
    server.ehlo()
    server.starttls()
    server.login('tracker_1231@hotmail.com', 'tracker1231')
    server.sendmail('tracker_1231@hotmail.com', mail, mailtext.encode("utf-8"))