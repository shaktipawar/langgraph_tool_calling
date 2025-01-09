from typing import Optional, Any
import os, yaml
from langchain_openai import ChatOpenAI


config_path = os.path.join(os.path.dirname(__file__), '..', '', 'config.yaml')
with open(config_path, 'r') as file:
    config = yaml.safe_load(file)
    for key, value in config.items():
        os.environ[key] = value

class ModelFactory:
    @staticmethod
    def get_chat_model(
        provider: str,
        model: str,
        temperature: float = 0.0,
        **kwargs
    ) -> Any:
        """
        Creates a chat model object based on the provider and configuration.

        Args:
            provider (str): The provider of the model (e.g., "openai", "ollama", etc.).
            model (str): The name of the model.
            temperature (float): Temperature for response generation.
            **kwargs: Additional keyword arguments for model configuration.

        Returns:
            Any: An instance of the chat model object.
        """
        if provider == "openai":
            return ChatOpenAI(
                model=model,
                temperature=temperature,
                model_kwargs=kwargs.get("model_kwargs", {})
            )
        elif provider == "ollama":
            return ChatOllama(
                model=model,
                temperature=temperature,
                model_kwargs=kwargs.get("model_kwargs", {})
            )
        else:
            raise ValueError(f"Unsupported provider: {provider}")