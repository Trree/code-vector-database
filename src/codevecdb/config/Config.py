
import os
from colorama import Fore

from src.codevecdb.singleton import Singleton


class Config(metaclass=Singleton):
    """
    Configuration class to store the state of bools for different scripts access.
    """

    def __init__(self) -> None:
        """Initialize the Config class"""
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.milvus_uri = os.getenv("milvus_uri")
        self.milvus_user = os.getenv("milvus_user")
        self.milvus_password = os.getenv("milvus_password")
        self.milvus_collection_ttl = os.getenv("milvus_collection_ttl")
        self.vector_embeddings = os.getenv("vector_embeddings")
        self.milvus_collection_name = os.getenv("milvus_collection_name")
        self.milvus_collection_dim = os.getenv("milvus_collection_dim")

    def set_openai_api_key(self, value: str) -> None:
        self.openai_api_key = value

    def set_milvus_uri(self, value: str) -> None:
        self.milvus_uri = value

    def set_milvus_user(self, value: str) -> None:
        self.milvus_user = value

    def set_milvus_password(self, value: str) -> None:
        self.milvus_password = value

    def set_milvus_collection_ttl(self, value: str) -> None:
        self.milvus_collection_ttl = value

    def set_vector_embeddings(self, value: str) -> None:
        self.vector_embeddings = value

    def set_milvus_collection_name(self, value: str) -> None:
        self.milvus_collection_name = value

    def set_milvus_collection_dim(self, value: str) -> None:
        self.milvus_collection_dim = value

def check_openai_api_key() -> None:
    """Check if the OpenAI API key is set in config.py or as an environment variable."""
    cfg = Config()
    if not cfg.openai_api_key:
        print(
            Fore.RED
            + "Please set your OpenAI API key in .env or as an environment variable."
            + Fore.RESET
        )
        print("You can get your key from https://platform.openai.com/account/api-keys")
        exit(1)