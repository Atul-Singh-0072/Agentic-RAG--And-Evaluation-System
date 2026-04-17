from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

def evaluate(system, test_data):
    results = []

    for item in test_data:
        question = item["question"]
        true_type = item["type"]

        pred_type, answer = system(question)

        routing_correct = pred_type == true_type

        keyword_score = sum(
            1 for word in item["expected_keywords"]
            if word.lower() in answer.lower()
        )

        results.append({
            "question": question,
            "true_type": true_type,
            "pred_type": pred_type,
            "routing_correct": routing_correct,
            "score": keyword_score
        })

    df = pd.DataFrame(results)
    df.to_csv("results/results.csv", index=False)

    return df