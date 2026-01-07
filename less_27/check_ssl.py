import json
import requests
import datetime
import sys
import os

from yandexcloud import SDK
from yandex.cloud.certificatemanager.v1.certificate_service_pb2 import ListCertificatesRequest
from yandex.cloud.certificatemanager.v1.certificate_service_pb2_grpc import CertificateServiceStub
from dotenv import load_dotenv

load_dotenv()

TG_BOT_TOKEN = os.getenv('TG_BOT_TOKEN')
TG_CHAT_ID = os.getenv('TG_CHAT_ID', '123456')
SA_KEY_FILE = os.getenv('SA_KEY_FILE')


def load_static_key(file_path):
    with open(file_path) as key:
        return json.load(key)

def send_msg(msg):
    if not TG_BOT_TOKEN:
        print(f"Telegram not configured")
        return
    url = f"https://api.telegram.org/bot{TG_BOT_TOKEN}/sendMessage"
    text = {
        "chat_id": TG_CHAT_ID,
        "text": msg,
    }

    try:
        response = requests.post(url, data=text)
        response.raise_for_status()
    except Exception as err:
        print(f"Telegram send message error: {err}")

def certificate_monitor(folder_id):
    sa_key = load_static_key(SA_KEY_FILE)
    sdk = SDK(service_account_key=sa_key)
    client = sdk.client(CertificateServiceStub)
    response = client.List(ListCertificatesRequest(folder_id=folder_id))

    check_result = []
    now_time = datetime.datetime.now()

    for cert in response.certificates:
        expire_date = cert.not_after.ToDatetime()
        days_left = (expire_date - now_time).days

        res = {
            "name": cert.name,
            "expire_date": expire_date,
            "days_left": days_left,
            "alarm": days_left <= 400
        }

        if res["alarm"]:
            msg = f"""
            ⚠️ Warning! Certificate will be expired\nCertificate {res['name']} expired in {res['expire_date']}. Days left {res['days_left']}
            """
            send_msg(msg)

        check_result.append(res)
    return check_result

folder_id = "b1gdge57rslfb323otnm"
stats = certificate_monitor(folder_id)