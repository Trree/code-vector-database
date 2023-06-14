from antlr4 import *

from src.codevecdb.split.javaparse.JavaLexer import JavaLexer
from src.codevecdb.split.javaparse.JavaParser import JavaParser
from src.codevecdb.split.javaparse.JavaParserListener import JavaParserListener


# 定义一个监听器，用于提取函数内容和声明
class FunctionExtractor(JavaParserListener):
    def __init__(self):
        self.functions = []

    def enterMethodDeclaration(self, ctx):
        function_text = input_stream.getText(ctx.start.start, ctx.stop.stop)
        # 获取函数上方的注释文本
        comments = []
        for i in range(ctx.start.line - 2, -1, -1):
            token = token_stream.get(i)
            if token.type == JavaLexer.COMMENT:
                comments.append(token.text)
            else:
                break

        self.functions.append(function_text)

    def get_functions(self):
        return self.functions


def extract_functions_from_java_file(code_file_context):
    global input_stream, token_stream
    input_stream = InputStream(code_file_context)
    lexer = JavaLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = JavaParser(token_stream)
    tree = parser.compilationUnit()
    walker = ParseTreeWalker()
    listener = FunctionExtractor()
    walker.walk(listener, tree)
    return listener.get_functions()

# code_context = "class MyClass {\n  /*\n   * This is a\n   * multi-line comment\n   */\n  public void myFunction1() {\n    // This is a single-line comment\n    System.out.println(\"Hello, world!\");\n  }\n\n  /*\n   * Another function\n   */\n  public void myFunction2() {\n    System.out.println(\"Another function\");\n  }\n}"
# functions = get_java_function(code_context)
# for function_text, comments in functions:
#     print(f"Function content: {function_text}")
#     print(f"Comments above function: {comments}")
#     print("----")