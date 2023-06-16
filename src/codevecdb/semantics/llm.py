
from langchain.llms import OpenAI
from langchain import PromptTemplate
import os
import openai

from src.codevecdb.config.Config import Config

if os.getenv("OPENAI_PROXY"):
    OPENAI_PROXY = os.getenv("OPENAI_PROXY")
    openai.proxy = OPENAI_PROXY


def getFunctionSemantics(code):
    cfg = Config()
    temperature = cfg.temperature
    if temperature > 2 or temperature < 0:
        temperature = 0.3
    module = cfg.module
    if not module:
        module = "text-davinci-003"

    llm = OpenAI(temperature=temperature, model=module)
    template = """
    You are a computer expert who can understand the semantics of program code functions well. 
    You can comprehend the purpose and functionality of the code through the code itself and the comments within it.
    Description of the function's semantics and functionality in around 50 words:
    {codeFunction}
    
    Your output needs to be in JSON format and include three fields.
    language：code language
    scope: function or class
    name: function name or class name
    semantics: code semantics
    """

    prompt = PromptTemplate(
        input_variables=["codeFunction"],
        template=template,
    )

    return llm(prompt.format(codeFunction=code))
