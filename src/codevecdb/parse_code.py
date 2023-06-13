
from concurrent.futures import ThreadPoolExecutor

from src.codevecdb import llm
from src.codevecdb.extract import extract_functions
from src.codevecdb.langchianEmbedding import get_semantics_vector
from src.codevecdb.milvus_vectordb import batchInsert


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
    result_dict, semantics = getSemanticsAndVector(code_list, False)
    batchInsert(result_dict)
    return semantics


def getSemanticsAndVector(code_list, asyncRequest):
    if asyncRequest:
        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(llm.getFunctionSemantics, item) for item in code_list]
            semantics = [future.result() for future in futures]
        codeVector = get_semantics_vector(semantics)
        result_dict = {}
        for code, semantics_item, codeVector_item in zip(code_list, semantics, codeVector):
            result_dict[code] = {"semantics": semantics_item, "codeVector": codeVector_item}
        return result_dict, semantics
    else:
        semantics = []
        for item in code_list:
            semantics.append(llm.getFunctionSemantics(item))

        codeVector = get_semantics_vector(semantics)
        result_dict = {}
        for code, semantics_item, codeVector_item in zip(code_list, semantics, codeVector):
            result_dict[code] = {"semantics": semantics_item, "codeVector": codeVector_item}
        return result_dict, semantics

