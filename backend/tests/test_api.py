from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get('/api/health')
    assert response.status_code == 200
    assert response.json()['status'] == 'ok'

def test_knowledge_search():
    response = client.get('/api/knowledge/search', params={'q': 'What is RAG retrieval augmented generation?'})
    assert response.status_code == 200
    assert 'results' in response.json()

def test_chat_requires_user_message():
    response = client.post('/api/chat', json={'messages': [{'role':'assistant','content':'Hello'}]})
    assert response.status_code == 422


def test_provider_health_without_key():
    from app.config import settings
    if not settings.llm_api_key:
        response = client.get('/api/health/provider')
        assert response.status_code == 200
        assert response.json()['connected'] is False
