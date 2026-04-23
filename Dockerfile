FROM python

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier d'abord le fichier des dépendances
COPY requirements.txt .

# Installer les dépendances (Flask et pytest)
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste du code (app.py et test_app.py)
COPY . .

# Indiquer le port sur lequel l'application écoute (pour info)
EXPOSE 5000

# Commande pour lancer l'application Flask (mode développement)
CMD ["flask", "--app", "app", "run", "--host=0.0.0.0", "--port=5000"]
