
from concurrent.futures import ThreadPoolExecutor

from src.codevecdb import llm
from src.codevecdb.langchianEmbedding import get_semantics_vector
from src.codevecdb.milvus_vectordb import batchInsert


def parseCodeAndInsert(code):
    code_list = [code]
    semantics = batchParseCodeAndInsert(code_list)
    return semantics


def batchParseCodeAndInsert(code_list):
    if not code_list:
        return ["code_list empty"]
    result_dict, semantics = getSemanticsAndVector(code_list, False)
    batchInsert(result_dict)
    return semantics


def getSemanticsAndVector(code_list, asyncRequest):
    if asyncRequest:
        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(llm.getFunctionSemantics, item) for item in code_list]
            semantics = [future.result() for future in futures]
    else:
        semantics = []
        for item in code_list:
            semantics.append(llm.getFunctionSemantics(item))

    codeVector = get_semantics_vector(semantics)
    result_dict = {}
    for code, semantics_item, codeVector_item in zip(code_list, semantics, codeVector):
        result_dict[code] = {"semantics": semantics_item, "codeVector": codeVector_item}
    return result_dict, semantics

