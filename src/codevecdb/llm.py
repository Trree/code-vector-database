
from langchain.llms import OpenAI
from langchain import PromptTemplate


def getFunctionSemantis(code):
    llm = OpenAI(temperature=0.3)
    template = """
    你是一个计算机专家，能很好的理解程序代码函数的语义，你可以通过代码和代码上的注释很好的理解代码的作用和功能。
    请用50个字以内描述下面函数的功能
    {codeFunction}
    
    你的输出需要是json格式的,包含3个字段
    language：code language
    scope: function or class
    name: function name or class name
    semantics: 代码的语义
    """

    prompt = PromptTemplate(
        input_variables=["codeFunction"],
        template=template,
    )

    return llm(prompt.format(codeFunction=code))
