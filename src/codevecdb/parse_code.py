
from src.codevecdb import langchianEmbedding, milvus_vectordb, llm
import time

_COLLECTION_NAME = 'code'

def parseCodeAndInsert(code):
    # create a connection
    milvus_vectordb.create_connection()

    # drop collection if the collection exists
    if milvus_vectordb.has_collection(_COLLECTION_NAME):
        milvus_vectordb.drop_collection(_COLLECTION_NAME)

    # create collection
    collection = milvus_vectordb.create_collection(_COLLECTION_NAME)

    # alter ttl properties of collection level
    milvus_vectordb.set_properties(collection)

    # show collections
    milvus_vectordb.list_collections()

    semantics = llm.getFunctionSemantis(code)
    codeVector = langchianEmbedding.getTextEmbedding(semantics)
    # insert 10000 vectors with 128 dimension

    vectors = milvus_vectordb.insert(collection, int(time.time()), semantics, code, codeVector)
    print("after insert")
    collection.flush()
    # get the number of entities
    milvus_vectordb.get_entity_num(collection)

    # create index
    milvus_vectordb.create_index(collection, "embedding")

    # load data to memory
    milvus_vectordb.load_collection(collection)

    # release memory
    milvus_vectordb.release_collection(collection)

    return semantics
