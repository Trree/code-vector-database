
from src.codevecdb import langchianEmbedding
from src.codevecdb.milvus_vectordb import searchVectorCode


def searchCode(query, top_k=5):
    semantics_list = [query]
    codeVectorList = langchianEmbedding.get_semantics_vector(semantics_list)
    return searchVectorCode(codeVectorList, top_k)
