from client import AdaptiveRetrievalRouter

queries = [
    "Good morning!",
    "What are the rate limits for the Enterprise API?",
    "Compare the throughput and latency trade-offs between Kafka and Pulsar"
]

for q in queries:
    decision = AdaptiveRetrievalRouter.route_query(q)
    print(f"Query: '{q}' -> Strategy: {decision['strategy']} ({decision['reason']})")
