import requests
import os
from dotenv import load_dotenv

load_dotenv()


tele_auth_token = os.getenv(
    "TELEGRAM_BOT_TOKEN"
)  
tel_group_id = os.getenv(
    "TELEGRAM_GROUP_ID"
)  


def msgTelegram(msg):
    
    telegram_api_url = f"https://api.telegram.org/bot{tele_auth_token}/sendMessage?chat_id={tel_group_id}&text={msg}"
    tel_resp = requests.get(telegram_api_url)
    print('Telegram response: ', tel_resp)
    if tel_resp.status_code == 200:
        print(tel_resp.json())
        print("Error: Details has been sent on Telegram")
        
    else:
        print("Could not send Message. Please check group id.")


def get_groupupdates():

    telegram_api_url = f"https://api.telegram.org/bot{tele_auth_token}/getUpdates"
    print(telegram_api_url)
    tel_resp = requests.get(telegram_api_url)
    if tel_resp.status_code == 200:
        print("Updates")
        print(tel_resp.json())
    else:
        print("Could not get updates!")



