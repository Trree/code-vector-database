# 基于ChatGPT的本地代码向量数据库

## 介绍

🌍 [_READ THIS IN ENGLISH_](README.md)

🤖️使用完全开源的[milvus](https://github.com/milvus-io/milvus)实现本地的代码向量库，解决本地，个人，公司级别代码本地向量化，
支持根据代码文件，以函数级别切分代码，建立函数和功能级别的代码向量库。
使用ChatGPT来获取函数语义，通过[Sentence-BERT](https://mccormickml.com/2019/05/14/BERT-word-embeddings-tutorial/)来实现词嵌入

## 使用场景
- 建立个人或者公司级别的向量代码库 
- 支持代码文件上传建立函数功能级别向量代码库
- 支持通过 prompt 搜索得到自己的代码
- 支持通过需求文档生成框架和代码

### 需求
- [x] 支持python,java,c++代码上传代码文件
- [x] 函数级别切分代码
- [x] 通过 ChatGPT 获得切分函数的语意
- [x] 通过语意建立代码向量库
- [x] 支持各种开源向量数据库
- [x] 支持页面搜索
- [ ] 支持通过 ChatGPT 优化代码
- [ ] 支持 ChatGPT 翻译自定义代码为其他语言
- [ ] 支持监督调整

### 依赖


- python = 3.10
- antlr4-python3-runtime
- milvus
- openai
- Sentence-BERT

## 本地部署

### 1. 设置环境
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

### 2.部署 Milvus

  - [milvus免费试用](https://cloud.zilliz.com/login?redirect=/projects/MA==/databases)
  - [docker本地快速部署](https://milvus.io/docs/v2.0.x/install_standalone-docker.md)


### 3. 配置

1. 在根目录找到名为 `.env.template` 的文件。由于点前缀，在某些操作系统中，默认情况下该文件可能是隐藏的。要显示隐藏文件，
  请按照您特定操作系统的说明进行操作:Windows, macOS。
2. 创建 `.env.template` 的副本，并将其命名为 `.env`；如果您已经在命令提示符/终端窗口中：`cp .env.template .env`。
3. 使用文本编辑器打开 `.env` 文件。
4. 找到一行上写着 `OPENAI_API_KEY=` 的内容。
5. 在 `=` 之后，输入您的独特的OpenAI API密钥，不要加任何引号或空格。
6. 请提供您想要使用的 `Milvus` 密钥和连接服务。
7. 保存并关闭 `.env` 文件。

### 启动服务

- 运行 `python app.py`.
- 浏览器中输入 `127.0.0.1:5000` 