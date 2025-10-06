# 4. Documentation des API externes et internes

## 4.1 Liste des API externes utilisées

| API externe                  | Usage principal                                     | Raison du choix                              |
|-----------------------------|--------------------------------------------------|----------------------------------------------|
| Deepfake Detection API       | Analyse des fichiers (images, vidéos, textes) pour vérifier leur authenticité | Service dédié fiable avec modèles IA avancés, simple intégration REST |
| SendGrid (ou autre SMTP)     | Envoi de notifications et alertes par email      | Fiabilité, documentation complète, intégration facile via API REST    |
| Auth0 (optionnel)            | Gestion externe de l’authentification et sécurité | Solution sécurisée, épargne développement interne complexe              |

---

## 4.2 Description des points d’API internes

| URL Path           | Méthode HTTP | Entrée (format)                                  | Sortie (format)                      | Description                                        |
|--------------------|--------------|------------------------------------------------|------------------------------------|--------------------------------------------------|
| `/api/auth/register` | POST         | JSON : { username, email, password }            | JSON : { token }                   | Inscription utilisateur, renvoie token JWT      |
| `/api/auth/login`   | POST         | JSON : { email, password }                       | JSON : { token }                   | Authentification utilisateur                      |
| `/api/data`         | GET          | Headers : Authorization (JWT)                    | JSON : liste des données           | Récupère les données associées à l’utilisateur   |
| `/api/data`         | POST         | JSON : { key, value }                            | JSON : objet données créé          | Ajout d’une donnée à surveiller                   |
| `/api/data/:id`     | PUT          | JSON : { key, value }                            | JSON : objet données mis à jour    | Mise à jour d’une donnée existante                |
| `/api/data/:id`     | DELETE       | Headers : Authorization (JWT)                    | JSON : { message }                 | Suppression d’une donnée                           |
| `/api/alerts`       | GET          | Headers : Authorization (JWT)                    | JSON : liste des alertes utilisateur| Récupération des alertes                          |
| `/api/alerts`       | POST         | JSON : { dataId, message }                       | JSON : objet alerte créé           | Création d’une alerte                             |
| `/api/subscriptions`| POST         | JSON : { plan }                                 | JSON : objet abonnement            | Souscription ou modification d’abonnement        |

---

## Formats d’entrée et sortie

- **Entrée** : Tout est au format JSON dans le corps des requêtes POST/PUT, avec validation côté serveur.  
- **Sortie** : Réponses au format JSON, toujours avec un code HTTP approprié (ex : 200, 201, 400, 401, 404, 500).
