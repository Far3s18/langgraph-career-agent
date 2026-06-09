from langchain_ollama import ChatOllama
from resume_ai.core.settings import settings

def get_text_model(temperature: float = 0.3) -> ChatOllama:
    return ChatOllama(
        model=settings.TEXT_MODEL,
        temperature=temperature,
        max_retries=3
    )