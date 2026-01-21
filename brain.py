import os
from pinecone import Pinecone
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv

load_dotenv()

class JarvisBrain:
    def __init__(self):
        self.index_name = "jarvis-index"
        
        # 1. Update to the model YOU HAVE: phi3:mini
        self.llm = ChatOllama(model="phi3:mini", temperature=0.3)
        
        # 2. Use phi3:mini for embeddings as well
        self.embeddings = OllamaEmbeddings(model="phi3:mini")
        
        # 3. Pinecone Connection
        pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
        
        # Connect to your existing index
        self.vector_store = PineconeVectorStore(
            index_name=self.index_name, 
            embedding=self.embeddings
        )

    def ask_jarvis(self, query):
        # Search for context
        docs = self.vector_store.similarity_search(query, k=3)
        context = "\n".join([d.page_content for d in docs])
        
        prompt = f"Context: {context}\n\nUser Question: {query}\n\nAnswer as Jarvis:"
        response = self.llm.invoke(prompt)
        return response.content