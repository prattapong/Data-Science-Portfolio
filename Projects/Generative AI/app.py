import streamlit as st
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.llms import HuggingFaceHub
from langchain.embeddings import HuggingFaceEmbeddings
from pinecone.grpc import PineconeGRPC as Pinecone
from langchain_pinecone import PineconeVectorStore
import os

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

llm = HuggingFaceHub(
    repo_id="mistralai/Mistral-7B-Instruct-v0.1", 
    model_kwargs={"temperature": 0.0, "max_new_tokens": 500},
    huggingfacehub_api_token=HUGGINGFACE_API_KEY
)

pc = Pinecone(api_key = PINECONE_API_KEY)

index_name = 'testbot'

docsearch = PineconeVectorStore.from_existing_index(
    index_name = index_name,
    embedding = embeddings
)