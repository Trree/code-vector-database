import configparser
import json

from pymilvus import (
    connections,
    FieldSchema, CollectionSchema, DataType,
    Collection,
    utility
)

from src.codevecdb.config.Config import Config

# This example shows how to:
#   1. connect to Milvus server
#   2. create a collection
#   3. insert entities
#   4. create index
#   5. search


# Const names

_ID_FIELD_NAME = 'id_field'
_VECTOR_FIELD_NAME = 'embedding'

# Vector parameters
_DIM = 1536
_INDEX_FILE_SIZE = 32  # max file size of stored index

# Index parameters
_METRIC_TYPE = 'L2'
_INDEX_TYPE = 'IVF_FLAT'
_NLIST = 1024
_NPROBE = 16
_TOPK = 3



# Create a Milvus connection
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
    default_fields = [
        FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=False),
        FieldSchema(name="semantics", dtype=DataType.VARCHAR, max_length=1000),
        FieldSchema(name="code", dtype=DataType.VARCHAR, max_length=5000),
        FieldSchema(name='embedding', dtype=DataType.FLOAT_VECTOR, description='Embedding vectors',  dim=_DIM)
    ]

    schema = CollectionSchema(fields=default_fields, description="collection description")
    collection = Collection(name=name, data=None, schema=schema)

    print("\ncollection created:", name)
    return collection


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



def insert(collection, i, semantics, code,  vector):
    id =[i]
    s = [semantics]
    c = [code]
    v = [vector]

    data = [id, s, c, v]
    print(data)
    collection.insert(data)
    print("end insert")
    return data

def batch_insert(collection, i, code_result):
    #for i, (code, result) in enumerate(code_result.items()):
    data = [
        [i + j for j in range(len(code_result))],
        [code_result[key]["semantics"] for key in code_result.keys()],
        [key for key in code_result.keys()],
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
    print("\nDrop index sucessfully")


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

    results = collection.search([search_vectors], _VECTOR_FIELD_NAME, search_param, output_fields=['semantics', 'code'], limit=top_k)
    queryCode = []
    for i, result in enumerate(results):
        print("\nSearch result for {}th vector: ".format(i))
        for j, res in enumerate(result):
            print("Top {}: {}".format(j, res))
            print(type(res))
            queryCode.append(res)
    return queryCode

def set_properties(collection):
    collection.set_properties(properties={"collection.ttl.seconds": 1800})
