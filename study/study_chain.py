# azure openai の設定をインポート
from settings import llm

from langchain.prompts import PromptTemplate


prompt = PromptTemplate(
    input_variables=["job"],
    template="{job}に一番オススメのプログラミング言語は何?"
)

chain = prompt | llm
print(chain.invoke({"job": "データサイエンティスト"}))