

from src.codevecdb import langchianEmbedding, milvus_vectordb

_COLLECTION_NAME = 'code'

def searchCode(query, top_k = 5):
    # create a connection
    milvus_vectordb.create_connection()
    codeVector = langchianEmbedding.getTextEmbedding(query)

    if milvus_vectordb.has_collection(_COLLECTION_NAME):
        collection = milvus_vectordb.get_collection(name=_COLLECTION_NAME)
    else:
        collection = milvus_vectordb.create_collection(_COLLECTION_NAME)
    # load data to memory
    milvus_vectordb.load_collection(collection)
    milvus_vectordb.set_properties(collection)
    milvus_vectordb.list_collections()

    # search
    result = milvus_vectordb.search(collection, codeVector, top_k)

    # release memory
    milvus_vectordb.release_collection(collection)
    return result