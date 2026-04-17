🧠 Agentic RAG System with Evaluation Framework

📌 Overview

This project implements an Agentic Retrieval-Augmented Generation (RAG) system that dynamically decides how to answer a query instead
of relying on static retrieval.
Unlike traditional RAG pipelines, this system introduces a query routing mechanism that classifies user intent and applies different 
reasoning strategies, enabling more accurate and controlled responses.


🎯 Objective

The goal of this project is to:

Build a context-aware Q&A system over a fixed dataset of AI regulation documents
Implement an explicit query routing mechanism
Generate grounded, non-hallucinated responses
Design a quantitative evaluation framework
Perform failure analysis to identify system limitations

📂 Dataset

4 documents on AI regulation
Provided externally (https://drive.google.com/drive/folders/18jlAr6bPEKHEL6km7dNKf-C6bjB4yTH9?usp=sharing)
Documents include:
Policy report
News article
Stakeholder memo
Technical brief

⚠️ The dataset contains:

Inconsistent formatting
Partial overlaps
Contradictions

👉 This is intentional to test system robustness.

🏗️ System Architecture
User Query
     ↓
Query Router (Agent)
     ↓
Retriever (FAISS)
     ↓
Generator (LLM - Groq)
     ↓
Final Answer

⚙️ Components

1️⃣ Ingestion Pipeline
Documents are loaded (.txt / .pdf)
Chunked using:
chunk_size = 400
chunk_overlap = 50

💡 Why this strategy?
Ensures context continuity
Prevents information loss at boundaries
Improves retrieval accuracy

2️⃣ Embedding & Vector Store
Embedding Model: all-MiniLM-L6-v2
Vector Store: FAISS

👉 Why?

Fast similarity search
Lightweight and efficient
Works well for semantic retrieval

3️⃣ Agentic Query Router 🧠

The system classifies queries into 3 types:

Type	Description
Factual	Answer exists directly
Synthesis	Requires combining multiple chunks
Out-of-Scope	Not present in documents

✅ Implementation

Rule-based keyword classification (explicit & inspectable)
No black-box decision making

4️⃣ Retrieval System
Uses FAISS retriever
Retrieves top k = 5 chunks

👉 Why k=5?

Improves context coverage
Enables better synthesis

5️⃣ Answer Generation

LLM: Groq (llama-3.3-70b-versatile)
Prompt design ensures:
No hallucination
Context-grounded answers
Partial reasoning allowed

6️⃣ Out-of-Scope Handling 🚫

If query is not relevant:

"Not available in documents"

👉 This avoids hallucination (critical requirement)

📊 Evaluation Framework

✅ Test Set

Total: 15 questions
5 Factual
5 Synthesis
5 Out-of-Scope

📈 Metrics Used

Metric	Purpose
Retrieval Accuracy	Correct chunks retrieved
Routing Accuracy	Correct classification
Answer Quality	Keyword overlap / similarity

📋 Output

Results are stored as:

Table (printed or CSV)
Includes:
Query
Expected Output
Predicted Output
Scores

❌ Failure Analysis

🔴 Failure 1: Missing Explicit Definitions
Query: "What is AI regulation?"
Issue: Documents discuss concept but don’t define it clearly
Result: Weak or incomplete answers

👉 Fix:

Improve chunking or add summarization layer
🔴 Failure 2: Weak Synthesis
Query: "Compare AI policies"
Issue: Retrieval may not fetch diverse sources
Result: Limited comparison

👉 Fix:

Increase k or use re-ranking
🔴 Failure 3: Over-Conservative Model

Model sometimes outputs:

Not available in documents

even when partial info exists

👉 Fix:

Improve prompt design (already done)

🚀 How to Run

1️⃣ Install dependencies
pip install -r requirements.txt

2️⃣ Run ingestion
python src/ingestion.py

3️⃣ Run system
python app.py

4️⃣ Run evaluation
python evaluation.py

🧪 Example Queries

What is AI regulation?
Compare AI policies across documents

Who is Elon Musk?

📦 Project Structure

Agentic RAG/
│── data/
│── src/
│     ├── ingestion.py
│     ├── retriever.py
│     ├── router.py
│     ├── generator.py
│
│── app.py
│── evaluation.py
│── requirements.txt
│── README.md

🎥 Video Demonstration

👉 Add your video link here:

🔗 https://drive.google.com/file/d/1c-_ajCxe-lKDS2wXhP3LDwas0MruvHgy/view?usp=sharing

Video should include:

Running the system (all 3 query types)
Evaluation script execution
One failure case explanation

🏆 Key Highlights

Agentic decision-making pipeline
Explicit and interpreable routing
Grounded answer generation
Evaluation-driven development
Real-world failure analysis


⚠️ Limitations

Depends on dataset quality
No re-ranking
Limited reasoning depth

🚀 Future Improvements

Hybrid search (BM25 + vector)
Better embeddings (OpenAI / Cohere)
Smarter routing (ML-based)
Contradiction detection

👨‍💻 Author

Atul Singh

🎯 FINAL NOTE

This project demonstrates:

Practical understanding of Agentic AI systems
Strong grasp of RAG pipelines
Ability to build evaluation-driven AI systems
