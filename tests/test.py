from llama_cpp import Llama
from langchain.embeddings import HuggingFaceEmbeddings
from chromadb.config import Settings
from chromadb import Client

# Llama 모델 경로
MODEL_PATH = "./path/to/your/llama/model.bin"

# Llama 로드 테스트
llm = Llama(model_path=MODEL_PATH)
response = llm("Hello, how are you?")
print("Llama 응답:", response)

# ChromaDB 설정
settings = Settings(persist_directory="./chroma_db", chroma_db_impl="duckdb+parquet")
client = Client(settings)
print("ChromaDB 설정 완료!")
