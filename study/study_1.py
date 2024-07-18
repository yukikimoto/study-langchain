import os
from dotenv import load_dotenv
load_dotenv()  # .envで設定した環境変数を読み込む

from langchain_openai import AzureChatOpenAI