# AI Universe sample knowledge

## Artificial Intelligence
Artificial Intelligence (AI) is the broad field of building systems that perform tasks associated with human intelligence, such as perception, language understanding, planning, and decision support. Machine learning is one approach within AI that learns patterns from data.

## Machine Learning
Machine learning (ML) uses data to fit models that make predictions or decisions. Supervised learning uses labeled examples; unsupervised learning finds structure in data; reinforcement learning learns from actions and rewards.

## Large Language Models
A large language model (LLM) is trained to model sequences of tokens. Transformer architectures use attention mechanisms to process contextual relationships. LLMs can generate useful text and code, but may produce incorrect or unsupported claims, so important answers should be verified.

## Retrieval-Augmented Generation
Retrieval-Augmented Generation (RAG) retrieves relevant passages from an external knowledge source and supplies them as context to a language model. A typical pipeline includes document parsing, chunking, embedding, vector or hybrid search, optional reranking, answer generation, and source citation. RAG can improve grounding but does not guarantee correctness.

## Embeddings and vector search
An embedding represents text or another input as a numeric vector. Semantic search compares vectors to retrieve items with similar meaning. FAISS is a library for efficient similarity search; a production system should also track document permissions, source metadata, index versions, and deletion behavior.

## Prompt injection and safety
Retrieved documents and web pages are untrusted input. Instructions found inside them should not override system policy. Applications should validate input, restrict tools and file access, keep secrets server-side, and test prompt-injection scenarios.
