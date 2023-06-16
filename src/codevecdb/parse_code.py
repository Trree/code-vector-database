from src.codevecdb.embeddings.langchainEmbedding import get_semantics_vector
from src.codevecdb.db.milvus_vectordb import batchInsert
from src.codevecdb.semantics.llm import batchGetSemantics


def parseCodeAndInsert(code):
    code_list = [code]
    semantics = batchParseCodeAndInsert(code_list)
    return semantics


def batchParseCodeAndInsert(code_list):
    if not code_list:
        return ["code_list empty"]
    result_dict, semantics = getSemanticsAndVector(code_list)
    batchInsert(result_dict)
    return semantics


def getSemanticsAndVector(code_list):
    semantics = batchGetSemantics(code_list)
    codeVector = get_semantics_vector(semantics)
    result_dict = {}
    for code, semantics_item, codeVector_item in zip(code_list, semantics, codeVector):
        result_dict[code] = {"semantics": semantics_item, "codeVector": codeVector_item}
    return result_dict, semantics

