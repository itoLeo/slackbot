

# 作成した天気情報モジュールを読み込む
# import plugins.botbot as botbot
from plugins.weather import weather
from slackbot.bot import respond_to     # @botname: で反応するデコーダ

@respond_to('今日の天気')
def whether_1(message):
    w = weather.get_weather(130010)
    t = w['forecasts'][0]
    message.reply(t['telop'])
