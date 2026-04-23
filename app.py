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
