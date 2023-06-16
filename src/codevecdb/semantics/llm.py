import threading
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from itertools import cycle

from langchain.llms import OpenAI
from langchain import PromptTemplate
import os
import openai
from tenacity import retry, wait_random_exponential, stop_after_attempt

from src.codevecdb.config.Config import Config

if os.getenv("OPENAI_PROXY"):
    OPENAI_PROXY = os.getenv("OPENAI_PROXY")
    openai.proxy = OPENAI_PROXY


def split_list(lst, chunk_size):
    return [lst[i:i+chunk_size] for i in range(0, len(lst), chunk_size)]


def batchGetSemantics(code_list):
    cfg = Config()
    key_list = cfg.openai_key_pool.split(",")
    key_list.append(cfg.openai_api_key)
    unique_key = list(set(key_list))
    print("key size:" + str(len(unique_key)))
    print("key: " + str(unique_key))
    semantics = []
    with ThreadPoolExecutor() as executor:
        all_code_list = split_list(code_list, len(unique_key))
        key_cycle = cycle(unique_key)
        for sub_code_list in all_code_list:
            print("code_list " + str(sub_code_list))
            futures = []
            for item in sub_code_list:
                api_key = next(key_cycle)
                futures.append(executor.submit(getFunctionSemantics, item, api_key))
            semantics.extend([future.result() for future in futures])

    return semantics


@retry(reraise=True, wait=wait_random_exponential(min=1, max=20), stop=stop_after_attempt(6))
def getFunctionSemantics(code, api_key):
    cfg = Config()
    temperature = cfg.temperature
    if temperature > 2 or temperature < 0:
        temperature = 0.3
    module = cfg.module
    if not module:
        module = "text-davinci-003"

    current_thread = threading.current_thread()
    thread_id = current_thread.ident
    current_time = datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    print("start " + formatted_time + " " + str(thread_id) + " " + code)
    llm = OpenAI(openai_api_key=api_key, temperature=temperature, model=module)
    if cfg.semantics_language == "CN":
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
    else:
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
