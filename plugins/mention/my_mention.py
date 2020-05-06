# coding: utf-8
# ランダム関数が使えるようになる
import random

from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ
from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ

# @respond_to('string')     bot宛のメッセージ
#                           stringは正規表現が可能 「r'string'」
# @listen_to('string')      チャンネル内のbot宛以外の投稿
#                           @botname: では反応しないことに注意
#                           他の人へのメンションでは反応する
#                           正規表現可能
# @default_reply()          DEFAULT_REPLY と同じ働き
#                           正規表現を指定すると、他のデコーダにヒットせず、
#                           正規表現にマッチするときに反応
#                           ・・・なのだが、正規表現を指定するとエラーになる？

# message.reply('string')   @発言者名: string でメッセージを送信
# message.send('string')    string を送信
# message.react('icon_emoji')  発言者のメッセージにリアクション(スタンプ)する
#                               文字列中に':'はいらない
@respond_to('誕生日おめでとう')
def mention_func1(message):
    message.send('ありがとう!') # メンション

@listen_to('いつでもどこでも変化球')
def listen_func1(message):
    message.send('ひなのなの！')      # ただの投稿
    # message.reply('')　メンションで返す

@listen_to('大喜利')
def mention_func2(message):
  res_list = ['心友だから', '元気田支店長', 'ヘイ！', '○カバヤシ', '上沼恵美子']
  message.send(random.choice(res_list))