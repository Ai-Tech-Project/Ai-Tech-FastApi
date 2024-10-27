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
│   └── main.py                # Point d'entrée de l'application FastAPI
├── env/                       # Environnement virtuel (ne doit pas être poussé sur Git)
├── requirements.txt           # Liste des dépendances
├── README.md                  # Documentation du projet
└── .gitignore                 # Fichier pour ignorer certains fichiers/dossiers dans Git

### 4. **lancer-lapplication** :

  ```bash
  uvicorn app.main:app --reload
  ```

### 5. **gestion-des-dépendances** :

Installer les dépendances :
   ```bash
   pip install -r requirements.txt
   ```


### 5. **bonnes-pratiques-pour-le-push** :


