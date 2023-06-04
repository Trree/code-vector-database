
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

    def set_openai_api_key(self, value: str) -> None:
        """Set the OpenAI API key value."""
        self.openai_api_key = value

    def set_milvus_uri(self, value: str) -> None:
        """Set the milvus_uri value."""
        self.milvus_uri = value

    def set_milvus_user(self, value: str) -> None:
        """Set the milvus_user value."""
        self.milvus_user = value

    def set_milvus_password(self, value: str) -> None:
        """Set the milvus_password value."""
        self.milvus_password = value

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