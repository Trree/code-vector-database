
from src.codevecdb import langchianEmbedding
from src.codevecdb.milvus_vectordb import searchVectorCode, searchRecentData


def searchCode(query, top_k=5):
    semantics_list = [query]
    print(semantics_list)
    codeVectorList = langchianEmbedding.get_semantics_vector(semantics_list)
    return searchVectorCode(codeVectorList, top_k)


def getAllCode(top_k=100):
    return searchRecentData(top_k)
