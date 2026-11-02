# AI Universe — Initial Working Version

AI Universe is a full-stack AI knowledge assistant starter. This first build includes a responsive React chat UI, FastAPI backend, SSE streaming, configurable OpenAI-compatible LLM endpoint, sample Markdown knowledge retrieval, source-labelled local answers, conversation history in browser storage, learning/code/compare modes, light/dark appearance, health endpoint, tests, and Docker support for the backend.

## Architecture

- `frontend/`: React + TypeScript + Vite UI. Conversation history is currently saved in browser localStorage.
- `backend/app/main.py`: FastAPI endpoints, streaming chat, provider adapter and error handling.
- `backend/app/knowledge.py`: dependency-free keyword retrieval over Markdown documents. It is intentionally a small starter retriever, not semantic/vector retrieval.
- `backend/data/`: sample trusted knowledge document.
- `backend/tests/`: basic API tests.

## Requirements

- Python 3.11+ (3.12 recommended)
- Node.js 20+ and npm
- Optional API key for a hosted OpenAI-compatible provider

## Run locally (Windows PowerShell)

### 1. Backend

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
# Edit .env and set LLM_API_KEY; leave empty for local setup mode
uvicorn app.main:app --reload --port 8000
```

API docs: http://localhost:8000/docs
Health: http://localhost:8000/api/health

### 2. Frontend (new terminal)

```powershell
cd frontend
npm install
npm run dev
```

Open http://localhost:5173. If the backend runs elsewhere, create `frontend/.env.local` with `VITE_API_BASE_URL=http://localhost:8000`.

## Configure an LLM provider

Copy `backend/.env.example` to `backend/.env`, then set:

```dotenv
LLM_BASE_URL=https://api.openai.com/v1
LLM_API_KEY=your_real_key_here
LLM_MODEL=gpt-4o-mini
```

Use the base URL, model name, and key issued by your provider. Never commit `.env` files or put provider credentials in frontend variables. Restart the backend after changes. In the app, open Workspace settings and choose **Test API connection** to verify the key, endpoint, and model with a small live request. This adapter expects an OpenAI-compatible `/chat/completions` streaming API.

## Run tests

```powershell
cd backend
pip install -r requirements.txt
pytest -q
```

## Docker backend

```bash
cd backend
docker build -t ai-universe-api .
docker run --rm -p 8000:8000 --env-file .env ai-universe-api
```

## Add sample knowledge

Place trusted `.md` documents in `backend/data/`. The starter keyword retriever reads Markdown paragraphs and returns source filenames/section numbers. Do not put private documents here in a public deployment; this starter has no per-user document permissions yet.

## API

- `GET /api/health` — service health and provider configuration status.
- `GET /api/health/provider` — sends a tiny test prompt to the configured model and reports whether the provider connection works (uses a small amount of API quota).
- `GET /api/knowledge/search?q=...` — searches sample Markdown knowledge.
- `POST /api/chat` — request body: `{"messages":[{"role":"user","content":"What is RAG?"}],"mode":"chat","use_knowledge":true}`. Response uses Server-Sent Events with JSON `text` chunks and a final `[DONE]` event.

## Current scope and limitations

This is a working initial foundation, not yet a fully production-ready public service. Implemented: UI, chat API, streaming, optional LLM provider, sample knowledge retrieval, conversation browser persistence, modes, health checks, API docs, initial tests. Not yet implemented: account authentication, server-side conversation persistence, PostgreSQL migrations, semantic embeddings/FAISS, PDF/TXT upload and admin permissions, real web search, rate limiting, robust prompt-injection testing, usage metering, deployment CI, or full production monitoring. Model comparison and learning modes currently guide prompting; they do not independently verify live model prices or benchmarks. Before public launch, add authentication/authorization, rate limits, upload scanning, CORS configuration, durable storage, privacy/retention controls, and security testing.

## Phased roadmap

1. **Phase 1 — UI and working chat:** included.
2. **Phase 2 — Provider adapter and streaming:** included; requires provider credentials for generated answers.
3. **Phase 3 — Durable conversation persistence:** next; add PostgreSQL models and migrations.
4. **Phase 4 — Production RAG:** add document parsers, embeddings, FAISS/pgvector, reranking, metadata filtering and citations.
5. **Phase 5 — Learning, comparisons and web search:** add trusted-source web search and dated, verified model data.
6. **Phase 6 — Security and deployment:** authentication, authorization, rate limits, monitoring, CI and deployment hardening.
