import re


def extract_functions_from_java_file(content):
    # Regular expression pattern to match function declarations
    pattern = r'(/\*(?:.|[\n\r])*?\*/)\s*((?:public|protected|private|static|\s)*)\s*[\w\<\>\[\]]+\s+([' \
              r'a-zA-Z_]\w*)\s*\([^)]*\)\s*{'

    functions = re.findall(pattern, content, re.MULTILINE)

    extracted_functions = []
    for function in functions:
        comment = function[0].strip()
        visibility = function[1].strip()
        function_name = function[2]
        extracted_functions.append((comment, visibility, function_name))

    return extracted_functions
