import gspread
import os
from oauth2client.service_account import ServiceAccountCredentials


scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
# 辞書オブジェクト。認証に必要な情報をHerokuの環境変数から呼び出している
credential = {
                "type": "service_account",
                "project_id": os.environ['SHEET_PROJECT_ID'],
                "private_key_id": os.environ['SHEET_PRIVATE_KEY_ID'],
                "private_key": os.environ['SHEET_PRIVATE_KEY'],
                "client_email": os.environ['SHEET_CLIENT_EMAIL'],
                "client_id": os.environ['SHEET_CLIENT_ID'],
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://oauth2.googleapis.com/token",
                "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
                "client_x509_cert_url":  os.environ['SHEET_CLIENT_X509_CERT_URL']
             }
credentials = ServiceAccountCredentials.from_json_keyfile_dict(credential, scope)

gc = gspread.authorize(credentials)

wks = gc.open('ひなのシート').sheet1

test = 'OK!'