"""Adaptive Retrieval Routing Engine.
100% Python Standard Library.
"""

import re

class AdaptiveRetrievalRouter:
    """Semantic query complexity classifier and routing decision engine."""
    @staticmethod
    def route_query(query):
        q = query.lower()
        word_count = len(re.findall(r'\b\w+\b', q))
        is_multi_hop = any(w in q for w in ["compare", "difference", "versus", "relationship between", "how does"]) or ("and" in q and word_count > 8)
        needs_retrieval = any(w in q for w in ["what", "who", "when", "where", "which", "how", "explain", "policy", "documentation"]) or word_count > 6
        is_code_math = any(w in q for w in ["def ", "class ", "calculate", "derivative", "integral", "solve", "+", "*", "="])

        if is_code_math:
            return {"strategy": "direct_reasoning", "reason": "Computational/code task requiring execution rather than document retrieval"}
        elif is_multi_hop:
            return {"strategy": "multi_hop_rag", "reason": "Query requires multi-hop relational synthesis"}
        elif needs_retrieval:
            return {"strategy": "standard_rag", "reason": "Factual informational query requiring grounded retrieval"}
        else:
            return {"strategy": "direct_llm", "reason": "Simple greeting or conversational turn"}
