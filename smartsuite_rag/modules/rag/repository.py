import chromadb
from datetime import datetime
from langchain_text_splitters import RecursiveCharacterTextSplitter    
from langchain_openai import OpenAIEmbeddings
from langchain.docstore.document import Document
from smartsuite_rag.modules.shared.uuid import generate_uuids
from modules.shared.configs import Configs

client = chromadb.HttpClient(host=Configs.get("CHROMADB_HOST"), port=Configs.get("CHROMADB_PORT"))

collection = client.get_or_create_collection(
    name="version-1", 
    metadata={
        "description": "v1 collection",
        "created": str(datetime.now())
    }
)

class Repository:
    def __init__(self):
        self.collection = collection
        self.embeddings_model = OpenAIEmbeddings(model="text-embedding-3-small", api_key=Configs.get("OPENAI_API_KEY"))

    def add(self, documents):
        docs = [Document(doc) if isinstance(doc, str) else doc for doc in documents]
            
        raw_chunks = self.generate_chunks(docs)
        chunks = []
        embeddings = []

        for chunk in raw_chunks:
            embedding = self.generate_embeddings(chunk.page_content)
            chunks.append(str(chunk))
            embeddings.append(embedding)

        self.collection.add(
            documents=chunks,
            embeddings=embeddings,
            ids=generate_uuids(len(chunks))
        )

    def get_nearest(self, text, limit=4):
        embeddings = self.generate_embeddings(text)

        return self.collection.query(
            query_embeddings=embeddings,
            n_results=limit
        )
    
    def get_exact(self, ids):
        return self.collection.get(ids=ids)
    
    def count(self):
        return self.collection.count()
    
    def delete(self, ids):
        return self.collection.delete(ids=ids)
    
    def generate_chunks(self, docs):
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=512,
            chunk_overlap=0,
        )
        chunks = text_splitter.split_documents(docs)
        return chunks
    
    def generate_embeddings(self, text):
        return self.embeddings_model.embed_query(text)
