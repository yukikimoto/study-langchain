from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma

from settings import embeddings

# ドキュメントを読み込み、ページごとに分割
loader = PyPDFLoader("https://blog.freelance-jp.org/wp-content/uploads/2023/03/FreelanceSurvey2023.pdf")
pages = loader.load_and_split()
print(pages[0])

# ページの埋め込みを取得
chroma_index = Chroma.from_documents(pages, embeddings)
docs = chroma_index.similarity_search("「フリーランスのリモートワークの実態」について教えて。", k=2)
for doc in docs:
    print(str(doc.metadata["page"]) + ":", doc.page_content)