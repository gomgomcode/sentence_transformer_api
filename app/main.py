from fastapi import FastAPI
from pydantic import BaseModel

from sentence_transformers import SentenceTransformer

import numpy as np

class EmbedRequest(BaseModel):
    query: str

app = FastAPI()

@app.get("/")
async def root():
    return {"root"}

@app.post("/embeddings")
async def embeddings(request: EmbedRequest):
    embedder = SentenceTransformer("jhgan/ko-sroberta-multitask")

    query = request.query
    query_embedding = embedder.encode(query, convert_to_tensor=True)
    query_embedding = query_embedding.cpu().numpy().tolist()

    return {"embedding": query_embedding}
