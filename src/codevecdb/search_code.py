from src.codevecdb.db.milvus_vectordb import searchVectorCode, searchRecentData
from src.codevecdb.embeddings.langchainEmbedding import get_semantics_vector


def searchCode(query, top_k=5):
    semantics_list = [query]
    codeVectorList = get_semantics_vector(semantics_list)
    return searchVectorCode(codeVectorList, top_k)


def getAllCode(top_k=100):
    return searchRecentData(top_k)
