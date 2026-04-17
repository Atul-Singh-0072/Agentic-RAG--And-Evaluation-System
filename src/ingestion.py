from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader, TextLoader
import os


def load_docs():
    docs = []

    # Go to main project folder
    base_dir = os.path.dirname(os.path.dirname(__file__))
    data_path = os.path.join(base_dir, "data")

    print("Looking in:", data_path)

    # Loop through files
    for file in os.listdir(data_path):
        file_path = os.path.join(data_path, file)

        # ✅ Load PDF files
        if file.endswith(".pdf"):
            print("Loading PDF:", file)
            loader = PyPDFLoader(file_path)
            docs.extend(loader.load())

        # ✅ Load TXT files
        elif file.endswith(".txt"):
            print("Loading TXT:", file)
            loader = TextLoader(file_path, encoding="utf-8")
            docs.extend(loader.load())

    return docs


def create_chunks(docs):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=400,
        chunk_overlap=50
    )
    return splitter.split_documents(docs)


def create_vectorstore(chunks):
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    db = FAISS.from_documents(chunks, embeddings)
    db.save_local("vectorstore")


# 🚀 Run everything
if __name__ == "__main__":
    docs = load_docs()
    print(f"Loaded {len(docs)} documents")

    if len(docs) == 0:
        print("❌ No documents found. Check your data folder!")
        exit()

    chunks = create_chunks(docs)
    print(f"Created {len(chunks)} chunks")

    create_vectorstore(chunks)
    print("✅ Vectorstore created successfully!")