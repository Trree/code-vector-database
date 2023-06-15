from langchain.embeddings import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")


def semantics_vector(code):
    print("this is my code: " + code)
    return embeddings.embed_query(code)


