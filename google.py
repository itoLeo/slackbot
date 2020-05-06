# import gspread,os
# from oauth2client.service_account import ServiceAccountCredentials

# scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

# credential = {
#                 "type": "service_account",
#                 "project_id": os.environ['SHEET_PROJECT_ID'],
#                 "private_key_id": os.environ['SHEET_PRIVATE_KEY_ID'],
#                 "private_key": os.environ['SHEET_PRIVATE_KEY'],
#                 "client_email": os.environ['SHEET_CLIENT_EMAIL'],
#                 "client_id": os.environ['SHEET_CLIENT_ID'],
#                 "auth_uri": "https://accounts.google.com/o/oauth2/auth",
#                 "token_uri": "https://oauth2.googleapis.com/token",
#                 "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
#                 "client_x509_cert_url":  os.environ['SHEET_CLIENT_X509_CERT_URL']
#              }

# # client_emailはgoogleで取得したもの
# credentials = ServiceAccountCredentials.from_json_keyfile_name(credential, scope)
# gc = gspread.authorize(credentials)

# wks = gc.open(os.environ['sheetname']).sheet1

# wks.update_acell('A1', 'Hello World!')
# print(wks.acell('A1').value)