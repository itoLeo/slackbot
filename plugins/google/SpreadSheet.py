import random
import gspread
import os
from oauth2client.service_account import ServiceAccountCredentials
from slackbot.bot import respond_to     # @botname: で反応するデコーダ
import plugins.google.example

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

@respond_to('テスト')
def test(message):
  test_test = plugins.google.example.test
  message.send(test_test) # メンション

@respond_to('お寿司召喚')
def read_sheet(message):
  number_list = list(range(1, 1458))
  import_value = wks.acell('A' + str(random.choice(number_list))).value
  message.send(import_value) # メンション

@respond_to('お寿司大放出')
def read_sheet(message):
  number_list = list(range(1, 1458))
  import_value = wks.acell('A' + str(random.choice(number_list))).value
  message.send(import_value) # メンション
  import_value = wks.acell('A' + str(random.choice(number_list))).value
  message.send(import_value) # メンション
  import_value = wks.acell('A' + str(random.choice(number_list))).value
  message.send(import_value) # メンション
  import_value = wks.acell('A' + str(random.choice(number_list))).value
  message.send(import_value) # メンション
  import_value = wks.acell('A' + str(random.choice(number_list))).value
  message.send(import_value) # メンション
  import_value = wks.acell('A' + str(random.choice(number_list))).value
  message.send(import_value) # メンション
  import_value = wks.acell('A' + str(random.choice(number_list))).value
  message.send(import_value) # メンション
  import_value = wks.acell('A' + str(random.choice(number_list))).value
  message.send(import_value) # メンション
  import_value = wks.acell('A' + str(random.choice(number_list))).value
  message.send(import_value) # メンション
  import_value = wks.acell('A' + str(random.choice(number_list))).value
  message.send(import_value) # メンション