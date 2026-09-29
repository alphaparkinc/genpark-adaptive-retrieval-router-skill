# genpark-adaptive-retrieval-router-skill

Agent Skill implementing **Adaptive Retrieval Routing** across direct reasoning, single-hop RAG, and multi-hop synthesis in 100% Python standard library.

## Architectural Flow
```mermaid
flowchart TD
    Q["User Prompt"] --> Router["Adaptive Retrieval Router"]
    Router -->|Conversational| D1["Direct LLM Generator"]
    Router -->|Factual / Policy| D2["Standard Single-Hop RAG"]
    Router -->|Comparative / Relational| D3["Multi-Hop Graph RAG Pipeline"]
    Router -->|Code / Mathematical| D4["Direct Symbolic Engine"]
```
