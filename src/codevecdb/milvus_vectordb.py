import configparser
import json
import time

from pymilvus import (
    connections,
    FieldSchema, CollectionSchema, DataType,
    Collection,
    utility
)

from src.codevecdb.config.Config import Config

_VECTOR_FIELD_NAME = 'embedding'
# Index parameters
_METRIC_TYPE = 'L2'
_INDEX_TYPE = 'IVF_FLAT'


def create_connection():
    print(f"\nCreate connection...")
    cfp = Config()
    try:
        milvus_uri = cfp.milvus_uri
        user = cfp.milvus_user
        password = cfp.milvus_password
    except configparser.NoOptionError:
        raise Exception("配置文件.env中的milvus_config配置不存在")

    connections.connect("default",
                        uri=milvus_uri,
                        user=user,
                        password=password)

    print(f"\nList connections:")
    print(connections.list_connections())


# Create a collection named 'demo'
def create_collection(name):
    cfg = Config()
    if cfg.vector_embeddings == "openai":
        dim = 1536
    else:
        dim = 384

    default_fields = [
        FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=False),
        FieldSchema(name="semantics", dtype=DataType.VARCHAR, max_length=1000),
        FieldSchema(name="code", dtype=DataType.VARCHAR, max_length=5000),
        FieldSchema(name=_VECTOR_FIELD_NAME, dtype=DataType.FLOAT_VECTOR, description='Embedding vectors', dim=dim)
    ]

    schema = CollectionSchema(fields=default_fields, description="collection description")
    collection = Collection(name=name, data=None, schema=schema)

    print("\ncollection created:", name)
    return collection


def get_collection(name):
    return Collection(name=name)


def has_collection(name):
    return utility.has_collection(name)


# Drop a collection in Milvus
def drop_collection(name):
    collection = Collection(name)
    collection.drop()
    print("\nDrop collection: {}".format(name))


# List all collections in Milvus
def list_collections():
    print("\nlist collections:")
    print(utility.list_collections())


def insert(collection, i, semantics, code, vector):
    id = [i]
    s = [semantics]
    c = [code]
    v = [vector]

    data = [id, s, c, v]
    print(data)
    collection.insert(data)
    print("end insert")
    return data


def batch_insert(collection, i, code_result):
    # for i, (code, result) in enumerate(code_result.items()):
    data = [
        [i + j for j in range(len(code_result))],
        [code_result[key]["semantics"] for key in code_result.keys()],
        [str(key) for key in code_result.keys()],
        [code_result[key]["codeVector"] for key in code_result.keys()]
    ]
    print(data)
    collection.insert(data)
    print("end insert")
    return data


def get_entity_num(collection):
    print("\nThe number of entity:")
    print(collection.num_entities)


def create_index(collection, filed_name):
    index = {
        'index_type': 'AUTOINDEX',
        'metric_type': 'L2',
        'params': {
            'M': 8,
            'efConstruction': 64
        },
    }
    collection.create_index(filed_name, index)
    print("\nCreated index:\n{}".format(collection.index().params))


def drop_index(collection):
    collection.drop_index()
    print("drop index success")


def load_collection(collection):
    collection.load()


def release_collection(collection):
    collection.release()


def search(collection, search_vectors, top_k=5):
    search_param = {
        'metric_type': 'L2',
        'params': {
            'ef': max(64, top_k)
        }
    }

    try:
        results = collection.search([search_vectors], _VECTOR_FIELD_NAME, search_param,
                                    output_fields=['semantics', 'code'],
                                    limit=top_k)
    except Exception as e:
        return [e]

    queryCode = []
    for i, result in enumerate(results):
        for j, res in enumerate(result):
            data = {
                'id': res.id,
                'distance': res.distance,
                'code': res.entity.get("code"),
                'semantics': res.entity.get("semantics")
            }
            queryCode.append(data)
    for item in queryCode:
        print(item)
    return queryCode


def set_properties(collection):
    cfp = Config()
    ttl_second = int(cfp.milvus_collection_ttl)
    if ttl_second > 0:
        collection.set_properties(properties={"collection.ttl.seconds": ttl_second})


def batchInsert(result_dict):
    cfg = Config()
    collection_name = cfg.milvus_collection_name

    if has_collection(collection_name):
        collection = get_collection(name=collection_name)
    else:
        collection = create_collection(collection_name)

    set_properties(collection)
    list_collections()
    batch_insert(collection, int(time.time() * 1000), result_dict)

    collection.flush()
    get_entity_num(collection)
    create_index(collection, "embedding")
    load_collection(collection)
    release_collection(collection)


def searchVectorCode(code_vector_list, top_k):
    cfg = Config()
    collection_name = cfg.milvus_collection_name
    if code_vector_list:
        codeVector = code_vector_list[0]
    else:
        return ["not found"]

    if has_collection(collection_name):
        collection = get_collection(name=collection_name)
    else:
        collection = create_collection(collection_name)
    # load data to memory
    load_collection(collection)
    set_properties(collection)
    list_collections()

    # search
    result = search(collection, codeVector, top_k)
    release_collection(collection)
    return result


def searchRecentData(top_k=100):
    cfg = Config()
    collection_name = cfg.milvus_collection_name

    if not has_collection(collection_name):
        return ["请插入数据创建数据集合"]

    try:
        collection = get_collection(name=collection_name)
        load_collection(collection)
        results = collection.query(expr="id > 0", limit=top_k, output_fields=["semantics", "code"])
    except Exception as e:
        return [e]
    for item in results:
        print(item)
    return results
