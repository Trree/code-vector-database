from langchain.embeddings import OpenAIEmbeddings


def getTextEmbedding(text):
    embeddings = OpenAIEmbeddings()
    query_result = embeddings.embed_query(text)
    return query_result
