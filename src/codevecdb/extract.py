import ast


def extract_functions(code_string):
    tree = ast.parse(code_string)
    functions = []
    # 遍历语法树
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            function_name = node.name
            function_code = ast.get_source_segment(code_string, node)
            functions.append((function_name, function_code))
    return functions
