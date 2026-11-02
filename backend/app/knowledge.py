from pathlib import Path
import re

DATA_DIR = Path(__file__).resolve().parent.parent / "data"

def retrieve(query: str, limit: int = 3) -> list[dict]:
    """Small dependency-free keyword retriever for the starter version.
    Replace with embeddings + FAISS/pgvector in Phase 4.
    """
    terms = {w.lower() for w in re.findall(r"[a-zA-Z0-9+#.-]+", query) if len(w) > 2}
    hits = []
    for path in DATA_DIR.glob("*.md"):
        text = path.read_text(encoding="utf-8")
        paragraphs = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
        for i, paragraph in enumerate(paragraphs):
            words = set(w.lower() for w in re.findall(r"[a-zA-Z0-9+#.-]+", paragraph))
            score = len(terms & words) / max(1, len(terms))
            if score > 0:
                hits.append({"source": path.name, "chunk": i + 1, "text": paragraph, "score": score})
    return sorted(hits, key=lambda h: h["score"], reverse=True)[:limit]
