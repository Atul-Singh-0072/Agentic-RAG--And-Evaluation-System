from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def generate_answer(query, docs, query_type):

    if query_type == "out_of_scope":
        return "The information is not available in the provided documents."

    context = "\n".join([doc.page_content for doc in docs])

    if not context.strip():
        return "Not available in documents"

    prompt = f"""
You are a helpful AI assistant.

INSTRUCTIONS:
- Use ONLY the provided context
- Answer clearly and directly
- Even if partial info is available, try to answer
- Only say "Not available in documents" if absolutely no relevant info exists

Context:
{context}

Question:
{query}

Answer in a clear and structured way:
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2   # 🔥 small increase = better answers
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"Error: {str(e)}"