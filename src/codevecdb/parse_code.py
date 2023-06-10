
from src.codevecdb import langchianEmbedding, milvus_vectordb, llm
import time
from concurrent.futures import ThreadPoolExecutor
from src.codevecdb.extract import extract_functions

_COLLECTION_NAME = 'code'

def parsePythonFileCode(python_code):
    extracted_functions = extract_functions(python_code)
    code_list = []
    for function_name, function_code in extracted_functions:
        code_list.append(function_code)
    batchParseCodeAndInsert(code_list)

def parseCodeAndInsert(code):
    code_list = [code]
    semantics = batchParseCodeAndInsert(code_list)
    return semantics

def batchParseCodeAndInsert(code_list):
    milvus_vectordb.create_connection()
    # drop collection if the collection exists
    if milvus_vectordb.has_collection(_COLLECTION_NAME):
        milvus_vectordb.drop_collection(_COLLECTION_NAME)

    collection = milvus_vectordb.create_collection(_COLLECTION_NAME)
    milvus_vectordb.set_properties(collection)
    milvus_vectordb.list_collections()
    # 创建并启动线程
    result_dict, semantics = getSemanticsAndVector(code_list, False)

    #semantics = llm.getFunctionSemantis(code)
    #codeVector = langchianEmbedding.getTextEmbedding(semantics)
    # insert 10000 vectors with 128 dimension

    vectors = milvus_vectordb.batch_insert(collection, int(time.time()*1000), result_dict)
    print("after insert")
    collection.flush()
    milvus_vectordb.get_entity_num(collection)
    milvus_vectordb.create_index(collection, "embedding")
    milvus_vectordb.load_collection(collection)
    milvus_vectordb.release_collection(collection)
    return semantics

def getSemanticsAndVector(code_list, asyncRequest):
    if asyncRequest:
        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(llm.getFunctionSemantis, item) for item in code_list]
            semantics = [future.result() for future in futures]
        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(langchianEmbedding.getTextEmbedding, item) for item in semantics]
            codeVector = [future.result() for future in futures]
        result_dict = {}
        for code, semantics_item, codeVector_item in zip(code_list, semantics, codeVector):
            result_dict[code] = {"semantics": semantics_item, "codeVector": codeVector_item}
        return result_dict, semantics
    else:
        semantics = []
        for item in code_list:
            semantics.append(llm.getFunctionSemantis(item))

        codeVector = []
        for item in semantics:
            codeVector.append(langchianEmbedding.getTextEmbedding(item))

        result_dict = {}
        for code, semantics_item, codeVector_item in zip(code_list, semantics, codeVector):
            result_dict[code] = {"semantics": semantics_item, "codeVector": codeVector_item}
        return result_dict, semantics

