# Local Code Vector Database based on ChatGPT

## Introduction

🌍 [_中文文档_](README_CN.md)

🤖️ This project utilizes the fully open-source [milvus](https://github.com/milvus-io/milvus) to build a local code vector database, 
enabling local, personal, and company-level code vectorization. 
It supports the creation of function and feature-level code vector databases by parsing code files at the function level. 
It leverages ChatGPT to obtain the semantic meaning of functions and utilizes [Sentence-BERT](https://mccormickml.com/2019/05/14/BERT-word-embeddings-tutorial/) for word embeddings.


## Scenarios
- Building personal or company-level code vector libraries
- Uploading code files to establish function and feature-level code vector databases
- Searching for your own code using prompts
- Generating frameworks and code based on requirement documents

### List
- [x] support openai api key pool，Support for multi threading Requests to OpenAI API.
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

- python = 3.10
- antlr4-python3-runtime
- milvus
- openai
- Sentence-BERT



## Local Deployment

### 1. Setting up the environment
```shell
# you can use conda to install the environment
$ conda create -p /your_path/env_name python=3.10
# Activate the environment
$ source activate /your_path/env_name
# Deactivate the environment
$ source deactivate /your_path/env_name
# Remove the environment
$ conda env remove -p  /your_path/env_name
```

* Project dependencies

```shell
# Clone the repository
$ git clone https://github.com/Trree/code-vector-database.git

$ cd code-vector-database
# Install dependencies
$ pip install -r requirements.txt
```

### 2. Install Milvus

  - [milvus Free trial](https://cloud.zilliz.com/login?redirect=/projects/MA==/databases)
  - [Standalone Quick Start Guide](https://milvus.io/docs/v2.0.x/install_standalone-docker.md)


### 3. Configuration

1. Find the file named `.env.template` in the main `code-vector-database` folder. This file may
    be hidden by default in some operating systems due to the dot prefix. To reveal
    hidden files, follow the instructions for your specific operating system:
    Windows, macOS.
2. Create a copy of `.env.template` and call it `.env`;
    if you're already in a command prompt/terminal window: `cp .env.template .env`.
3. Open the `.env` file in a text editor.
4. Find the line that says `OPENAI_API_KEY=`.
5. After the `=`, enter your unique OpenAI API Key *without any quotes or spaces*.
6. Please provide the Milvus keys services you would like to use.
7. Save and close the `.env` file.

### 4. Run Scripts to Experience Web UI 

- Start `python app.py`.
- Connect to `127.0.0.1:5000` on your browser.

