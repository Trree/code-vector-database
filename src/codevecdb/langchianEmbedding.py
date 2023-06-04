from langchain.embeddings import OpenAIEmbeddings


def getTextEmbedding(text):
    embeddings = OpenAIEmbeddings()
    query_result = embeddings.embed_query(text)
    return query_result


if __name__ == '__main__':
    print('Running as main')
    getTextEmbedding("hello")
else:
    print('Imported as module')