# 基于ChatGPT的本地代码向量数据库

## 介绍

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

- python 
  - python = 3.10

- antlr4-python3-runtime
  - 用于生成语法解析器和词法分析器，获取函数代码内容

- milvus 
  - 免费试用: https://cloud.zilliz.com/login?redirect=/projects/MA==/databases
  - 连接更新config.ini文件中的配置
- openai
  - cp .env.template .env 
  - 更新.env中的openai_api_key

- Sentence-BERT
  - 词嵌入
