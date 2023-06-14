import os

from src.codevecdb.parse_code import batchParseCodeAndInsert
from src.codevecdb.split.cpp_split import extract_functions_from_cpp_file
from src.codevecdb.split.get_language import get_language
from src.codevecdb.split.java_split import extract_functions_from_java_file
from src.codevecdb.split.python_split import python_split_function


def split_file_to_function(file):
    print(file)
    file.save('uploads/' + file.filename)  # 保存文件到指定路径
    with open(os.path.join('uploads', file.filename), 'r') as f:
        content = f.read()
    language = get_language(file.filename)
    if language == "Python":
        extracted_functions = python_split_function(content)
    elif language == "Java":
        extracted_functions = extract_functions_from_java_file(content)
    elif language == "Cpp":
        extracted_functions = extract_functions_from_cpp_file(content)
    else:
        return "only support python, java, c++"

    semantics = batchParseCodeAndInsert(extracted_functions)
    print(semantics)
