from antlr4 import *

from src.codevecdb.split.cppparse.CPP14Lexer import CPP14Lexer
from src.codevecdb.split.cppparse.CPP14Parser import CPP14Parser
from src.codevecdb.split.cppparse.CPP14ParserListener import CPP14ParserListener


class CPPCustomListener(CPP14ParserListener):
    def __init__(self):
        super().__init__()
        self.function_declarations = []
        self.function_contents = []

    def enterFunctionDefinition(self, ctx: CPP14Parser.FunctionDefinitionContext):
        function_name = ctx.getText()
        self.function_declarations.append(function_name)

    # def enterFunctionBody(self, ctx: CPP14Parser.FunctionBodyContext):
    #     function_content = ctx.getText()
    #     self.function_contents.append(function_content)


def extract_functions_from_cpp_file(code_file_context):
    input_stream = InputStream(code_file_context)
    lexer = CPP14Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CPP14Parser(stream)
    tree = parser.translationUnit()

    listener = CPPCustomListener()
    ParseTreeWalker.DEFAULT.walk(listener, tree)

    return listener.function_declarations

