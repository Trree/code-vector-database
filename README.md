# Local Code Vector Database based on ChatGPT

## Introduction

🤖️ This project utilizes the fully open-source [milvus](https://github.com/milvus-io/milvus) to build a local code vector database, 
enabling local, personal, and company-level code vectorization. 
It supports the creation of function and feature-level code vector databases by parsing code files at the function level. 
It leverages ChatGPT to obtain the semantic meaning of functions and utilizes [Sentence-BERT](https://mccormickml.com/2019/05/14/BERT-word-embeddings-tutorial/) for word embeddings.


## Use Cases
- Building personal or company-level code vector libraries
- Uploading code files to establish function and feature-level code vector databases
- Searching for your own code using prompts
- Generating frameworks and code based on requirement documents

### List
- [x] Support uploading Python, Java, and C++ code files
- [x] Parse code at the function level
- [x] Obtain semantic meaning of parsed functions using ChatGPT
- [x] Build code vector libraries based on semantic meaning
- [x] Support various open-source vector databases
- [x] Support searching on a web interface
- [ ] Support code optimization using ChatGPT
- [ ] Support translation of custom code to other languages using ChatGPT
- [ ] Support supervised adjustments

### Dependencies

- python 
  - python = 3.10

- antlr4-python3-runtime
  - Used for generating grammar parsers and lexical analyzers to extract function code content

- milvus 
  - [milvus Free trial](https://cloud.zilliz.com/login?redirect=/projects/MA==/databases)
  - update .env milvus config
- openai
  - cp .env.template .env 
  - update .env openai_api_key

- Sentence-BERT
  - word embeddings.