
# ライブラリの読み込み
import json
import requests

# 天気情報を取得するための関数。botboduleで読み込む
def get_weather(city_number):
    url = "http://weather.livedoor.com/forecast/webservice/json/v1?city=%s" % city_number
    # URLアクセスして情報を取得する
    response = requests.get(url)
    #urlが読み込まれなかったときにここで処理を止めてエラー内容を吐き出す。
    response.raise_for_status()
    # 取得したjsonデータを読み込む
    weather_data = json.loads(response.text)
    return(weather_data)