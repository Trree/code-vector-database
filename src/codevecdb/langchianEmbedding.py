from concurrent.futures import ThreadPoolExecutor

from src.codevecdb.bert_vector import semantics_vector
from src.codevecdb.config.Config import Config
from src.codevecdb.openai_embeddings import getTextEmbedding


def get_semantics_vector(semantics_list):
    cfg = Config()
    if cfg.vector_embeddings == "openai":
        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(getTextEmbedding, item) for item in semantics_list]
            codeVector = [future.result() for future in futures]
    else:
        with ThreadPoolExecutor() as executor:
            print(semantics_list)
            futures = [executor.submit(semantics_vector, item) for item in semantics_list]
            print(futures)
            codeVector = []
            for f in futures:
                codeVector.append(f.result())

    return codeVector
