import ast

def extract_functions(code_string):
    tree = ast.parse(code_string)

    functions = []

    # 遍历语法树
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            # 获取函数的名称和代码块
            function_name = node.name
            function_code = ast.get_source_segment(code_string, node)
            functions.append((function_name, function_code))
    return functions

# 示例代码字符串
code = '''
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
'''

# 提取函数代码块
extracted_functions = extract_functions(code)

# 打印提取的函数代码块
for function_name, function_code in extracted_functions:
    print(f"Function name: {function_name}")
    print(f"Function code:\n{function_code}\n")