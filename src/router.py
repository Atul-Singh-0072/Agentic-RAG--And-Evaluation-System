def classify_query(query):
    query = query.lower()

    # Out of scope
    if any(word in query for word in ["ceo", "salary", "movie", "weather"]):
        return "out_of_scope"

    # Synthesis (comparison / multiple info)
    if any(word in query for word in ["compare", "difference", "across", "multiple"]):
        return "synthesis"

    # Default
    return "factual"