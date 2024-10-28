# Projet FastAPI - Ai-FastApi

Ce projet est une API REST développée avec FastAPI, qui inclut une structure modulaire, des dépendances essentielles, et les bonnes pratiques pour une gestion efficace du dépôt.

## Table des Matières
1. [Pré-requis](#pré-requis)
2. [Installation et Configuration](#installation-et-configuration)
3. [Structure du Projet](#structure-du-projet)
4. [Lancer l'application](#lancer-lapplication)
5. [Gestion des Dépendances](#gestion-des-dépendances)
6. [Bonnes Pratiques pour le Push](#bonnes-pratiques-pour-le-push)

---

### 1. Pré-requis

Avant de commencer, assurez-vous d'avoir les éléments suivants installés :
- **Python 3.7+**
- **Git** (pour le contrôle de version)
- **Virtualenv** (ou utilisez `python -m venv` pour les environnements virtuels)

---

### 2. Installation et Configuration

Suivez les étapes ci-dessous pour configurer le projet FastAPI.

1. **Cloner le dépôt** :
   ```bash
   git clone <URL_DU_DEPOT>
   cd Ai-FastApi

Créer un environnement virtuel :
   ```bash
   python -m venv env
   ```

Activer l'environnement virtuel :
   ```bash
   .\env\Scripts\activate
   ```

### 3. **structure-du-projet** : 

Ai-FastApi/
├── app/
│   ├── __init__.py            # Fichier pour initialiser le module
│   ├── main.py                # Point d'entrée de l'application FastAPI
│   ├── api/                   # Dossier pour les routes de l'API
│   │   ├── __init__.py
│   │   ├── v1/                # Versionnement des routes (ex: v1)
│   │   │   ├── __init__.py
│   │   │   ├── user_routes.py # Routes liées aux utilisateurs
│   │   │   └── question_routes.py # Routes liées au chatbot
│   ├── core/                  # Configuration principale et fonctions de base
│   │   ├── __init__.py
│   │   ├── config.py          # Fichier de configuration de l'application
│   │   └── security.py        # Gestion de la sécurité (authentification, tokens, etc.)
│   ├── models/                # Modèles de données pour MongoDB
│   │   ├── __init__.py
│   │   ├── user_model.py      # Modèle utilisateur
│   │   └── question_model.py  # Modèle pour les données du chatbot
│   ├── schemas/               # Schémas Pydantic pour la validation
│   │   ├── __init__.py
│   │   ├── user_schema.py     # Schéma pour les utilisateurs
│   │   └── question_schema.py  # Schéma pour les données chatbot
│   └── services/              # Logique métier, ex : gestion des utilisateurs
│       ├── __init__.py
│       ├── user_service.py    # Service pour les utilisateurs
│       └── question_service.py # Service pour le chatbot
├── env/                       # Environnement virtuel (ne doit pas être poussé sur Git)
├── requirements.txt           # Liste des dépendances
├── README.md                  # Documentation du projet
└── .gitignore                 # Fichier pour ignorer certains fichiers/dossiers dans Git

### 4. **lancer-lapplication** :

  ```bash
  uvicorn app1.main:app1 --reload
  ```

### 5. **gestion-des-dépendances** :

Installer les dépendances :
   ```bash
   pip install -r requirements.txt
   ```


### 5. **bonnes-pratiques-pour-le-push** :


