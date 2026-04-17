from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings


def get_retriever():
    # ✅ Initialize embeddings
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    # ✅ Load vectorstore
    db = FAISS.load_local(
        "vectorstore",
        embeddings,
        allow_dangerous_deserialization=True
    )

    # ✅ Improved retriever (more context)
    retriever = db.as_retriever(
        search_kwargs={"k": 5}   # 🔥 increased from 3 → 5
    )

    return retriever