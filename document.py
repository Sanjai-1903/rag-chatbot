from textwrap import indent
from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import InMemoryVectorStore, Pinecone
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore,Pinecone


from langchain_community.document_loaders import DirectoryLoader



embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
def create_vector():
    loader = DirectoryLoader("data", glob="*.txt")
    documents = loader.load()


    text_splitter=RecursiveCharacterTextSplitter(chunk_size=200,chunk_overlap=50)
    chunks=text_splitter.split_documents(documents)
    Pinecone.from_documents(chunks,embeddings,index_name="first-rag")
    

def search(query):
    vectorstore=PineconeVectorStore(index_name="first-rag",embedding=embeddings)
    docs=vectorstore.similarity_search(query,k=2)
    return docs[0].page_content

