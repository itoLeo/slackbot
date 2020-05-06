# config: utf-8
import os

# herokuで暗号化
API_TOKEN = os.environ['SLACK_API']

# デフォルトで返信する単語
DEFAULT_REPLY = "•🔻•"

PLUGINS = [
  'plugins.mention',
  'plugins.weather',
  'plugins.google',
  ]