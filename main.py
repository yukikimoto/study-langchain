import os
from dotenv import load_dotenv
load_dotenv()  # .envで設定した環境変数を読み込む

from langchain_openai import AzureChatOpenAI

# Azure Chat OpenAIのクライアントを作成
llm = AzureChatOpenAI(
    azure_deployment=os.environ['AZURE_DEPLOYMENT_NAME'], # Azureリソースのデプロイメント名
    api_version="2024-06-01", # azure openaiのAPIバージョン
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

# 送信するメッセージを定義
messages = [
    (
        "system", # システムメッセージ
        "You are a helpful assistant that translates English to japanese. Translate the user sentence.",
    ),
    (
        "human", # ユーザーメッセージ 
        "I love programming.",
    ),
]

# メッセージを送信して、AIからの返信を取得し表示
ai_msg = llm.invoke(messages)
print(ai_msg) # メッセージの情報を全て表示
print(ai_msg.content) # メッセージの内容のみ表示

