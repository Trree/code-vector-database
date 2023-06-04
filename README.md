# 代码向量数据库


### 使用场景
- 建立个人或者公司级别的向量代码库 
- 支持通过 prompt 匹配得到自己的代码 
- 支持通过需求文档生成框架和代码

### 需求
- [ ] 支持上传代码文件
- [ ] 函数级别切分代码
- [x] 通过 ChatGPT 获得切分函数的语意
- [x] 通过语意建立代码向量库
- [x] 支持各种开源向量数据库
- [x] 支持页面搜索
- [ ] 支持通过 ChatGPT 优化代码
- [ ] 支持 ChatGPT 翻译自定义代码为其他语言
- [ ] 支持监督调整

### 依赖

- milvus 
  - 免费试用: https://cloud.zilliz.com/login?redirect=/projects/MA==/databases
  - 连接更新config.ini文件中的配置
- openai
  - cp .env.template .env 
  - 更新.env中的openai_api_key