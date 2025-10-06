import os
from pinecone import Pinecone, ServerlessSpec

class PineconeService:
    def __init__(self, api_key: str, index_name: str, dimension: int = 768):
        self.pc = Pinecone(api_key=api_key)
        self.index_name = index_name

        # Create index if not exists
        if self.index_name not in [i["name"] for i in self.pc.list_indexes()]:
            self.pc.create_index(
                name=self.index_name,
                dimension=dimension,
                metric="cosine",
                spec=ServerlessSpec(cloud="aws", region="us-east-1")
            )
        self.index = self.pc.Index(self.index_name)

    def upsert_vector(self, vector_id: str, embedding: list[float], metadata: dict = None):
        """Insert or update a vector with metadata"""
        self.index.upsert([(vector_id, embedding, metadata)])

    def query_vector(self, embedding: list[float], top_k: int = 5):
        """Query similar vectors"""
        return self.index.query(vector=embedding, top_k=top_k, include_metadata=True)

    def delete_vector(self, vector_id: str):
        """Delete a vector"""
        self.index.delete(ids=[vector_id])
