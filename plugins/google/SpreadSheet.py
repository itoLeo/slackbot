import random
from slackbot.bot import respond_to     # @botname: で反応するデコーダ
import example

wks = example.Authentication()

@respond_to('テストa')
def test(message):
  test_test = example.Authentication.test
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