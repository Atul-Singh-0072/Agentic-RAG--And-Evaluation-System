from src.router import classify_query
from src.retriever import get_retriever
from src.generator import generate_answer

# Initialize retriever
retriever = get_retriever()


def system(query):
    # Step 1: classify query
    query_type = classify_query(query)

    # Step 2: handle out-of-scope
    if query_type == "out_of_scope":
        return query_type, "Not available in documents"

    # Step 3: retrieve relevant docs (UPDATED METHOD)
    docs = retriever.invoke(query)

    # Step 4: generate answer
    answer = generate_answer(query, docs, query_type)

    return query_type, answer


if __name__ == "__main__":
    print("🤖 Agentic RAG System Ready! (type 'exit' to quit)\n")

    while True:
        q = input("Ask: ")

        if q.lower() == "exit":
            break

        query_type, answer = system(q)

        print(f"\nType: {query_type}")
        print(f"Answer: {answer}\n")