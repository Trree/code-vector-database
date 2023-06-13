import ast


def python_split_function(code_string):
    tree = ast.parse(code_string)
    functions = []
    # 遍历语法树
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            function_code = ast.get_source_segment(code_string, node)
            functions.append(function_code)
    return functions
