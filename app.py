from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    # Page d'accueil simple avec instructions
    return '<h1>Bienvenue !</h1><p>Utilisez le chemin /hello/VOTRE_NOM dans l\'URL.</p>'

@app.route('/hello/<string:name>')
def hello(name):
    # La variable 'name' vient directement du chemin de l'URL
    # Utilisation de f-string pour l'intégration directe
    return f'<h1>Hello, {name}!</h1>'
Créer un fichier requirements.txt avec le contenu suivant:
Flask
pytest
Créer un fichier test_app.py avec le contenu suivant
import pytest
from app import app as flask_app # Renomme pour éviter conflit

@pytest.fixture
def app():
    """Crée une instance de l'application Flask pour les tests."""
    yield flask_app

@pytest.fixture
def client(app):
    """Crée un client de test Flask."""
    return app.test_client()

def test_root_path(client):
    """Teste la route racine '/'."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'<h1>Bienvenue !</h1>' in response.data
    assert b'/hello/VOTRE_NOM' in response.data

def test_hello_with_name_parameter(client):
    """Teste la route '/hello/<name>' avec un nom spécifique."""
    test_name = "DockerCI"
    response = client.get(f'/hello/{test_name}') # Utilise la nouvelle URL
    assert response.status_code == 200
    assert f'<h1>Hello, {test_name}!</h1>'.encode() in response.data

def test_hello_with_another_name(client):
    """Teste la route '/hello/<name>' avec un autre nom."""
    test_name = "Utilisateur"
    response = client.get(f'/hello/{test_name}')
    assert response.status_code == 200
    assert f'<h1>Hello, {test_name}!</h1>'.encode() in response.data
