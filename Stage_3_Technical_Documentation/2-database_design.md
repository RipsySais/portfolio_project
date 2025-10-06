# Filename: System-Components-Classes-Database-Design.md

## 1. Back-end : Classes clés

| Classe      | Attributs principaux                     | Méthodes principales                      |
|-------------|-----------------------------------------|-------------------------------------------|
| Utilisateur | userID, username, email, passwordHash, role | login(), logout(), updateProfile()       |
| Contenu     | contentID, title, description, contentData, userID, timestamp | createContent(), updateContent(), deleteContent(), getContentByUser() |
| Analytics   | analyticsID, userID, eventName, timestamp | logEvent(), getEventsByUser()             |

## 2. Base de données relationnelle : Schéma ER

### Tables et attributs

| Table       | Attributs                            | Clés                        | Relations                         |
|-------------|------------------------------------|-----------------------------|----------------------------------|
| Utilisateur | userID (PK), username, email, passwordHash, role | userID (PK)                 | -                                |
| Contenu     | contentID (PK), title, description, contentData, userID (FK), timestamp | contentID (PK), userID (FK) | Utilisateur 1..* — Contenu *     |
| Analytics   | analyticsID (PK), userID (FK), eventName, timestamp | analyticsID (PK), userID (FK) | Utilisateur 1..* — Analytics *   |

### Diagramme ER Mermaid

erDiagram
UTILISATEUR {
  INT userID PK "Identifiant unique"
  VARCHAR username
  VARCHAR email
  VARCHAR passwordHash
  ENUM role
}
CONTENU {
  INT contentID PK "Identifiant unique"
  VARCHAR title
  TEXT description
  TEXT contentData
  INT userID FK "Référence utilisateur"
  DATETIME timestamp
}
ANALYTICS {
  INT analyticsID PK "Identifiant unique"
  INT userID FK "Référence utilisateur"
  INT contentID FK "Réf. contenu"
  VARCHAR eventName
  DATETIME timestamp
}
UTILISATEUR ||--o{ CONTENU : "crée"
UTILISATEUR ||--o{ ANALYTICS : "génère"
CONTENU ||--o{ ANALYTICS : "est analyser par"

## 3. Base de données orientée document (MongoDB) : Collections

| Collection  | Structure document (exemple)                                                                       | Champs obligatoires                   | Champs optionnels         |
|-------------|--------------------------------------------------------------------------------------------------|-------------------------------------|--------------------------|
| utilisateurs | { "_id": ObjectId, "username": String, "email": String, "passwordHash": String, "role": String } | username, email, passwordHash, role | -                        |
| contenus    | { "_id": ObjectId, "title": String, "description": String, "contentData": String, "userId": ObjectId, "timestamp": Date } | title, userId                       | description, contentData  |
| analytics   | { "_id": ObjectId, "userId": ObjectId, "eventName": String, "timestamp": Date }                    | userId, eventName                   | timestamp                |

## 4. Front-end : Composants UI principaux

| Composant       | Description                                | Interactions principales                           |
|-----------------|--------------------------------------------|---------------------------------------------------|
| LoginForm       | Formulaire d’authentification utilisateur | Envoie les données à la classe Utilisateur backend |
| UserProfile     | Affiche et modifie les données utilisateur | Appelle updateProfile sur back-end                   |
| ContentList     | Liste des contenus créés par l’utilisateur | Affiche contenus, interaction avec contenu backend |
| ContentEditor   | Création et modification de contenu        | Appelle createContent et updateContent              |
| AnalyticsViewer | Affiche les données analytiques basiques   | Requête vers Analytics backend                        |
