# Diagrammes de séquence pour site de vérification deepfake

## Cas 1 : Connexion utilisateur

Participants : Utilisateur, Front-end, Back-end, Base de données

Séquence :
- L’utilisateur saisit ses identifiants et valide.
- Le front-end envoie une requête d’authentification au back-end.
- Le back-end vérifie les identifiants dans la base de données.
- La base de données retourne le résultat (succès ou échec).
- Le back-end renvoie la réponse au front-end.
- Le front-end affiche la page d’accueil ou un message d’erreur.

### Diagramme de séquence Mermaid - Connexion utilisateur

sequenceDiagram
participant Utilisateur
participant Front-end
participant Back-end
participant BaseDeDonnées

text
Utilisateur->>Front-end: Saisit identifiants
Front-end->>Back-end: Requête d'authentification
Back-end->>BaseDeDonnées: Vérifie identifiants
BaseDeDonnées-->>Back-end: Résultat auth
Back-end-->>Front-end: Réponse succès/échec
Front-end-->>Utilisateur: Affiche résultat
text

---

## Cas 2 : Soumission d’un fichier deepfake pour vérification

Participants : Utilisateur, Front-end, Back-end, Service IA, Base de données

Séquence :
- L’utilisateur charge un fichier via le front-end.
- Le front-end envoie le fichier au back-end.
- Le back-end transmet le fichier au service d’analyse IA.
- Le service IA analyse le fichier et retourne un verdict.
- Le back-end stocke le résultat dans la base de données.
- Le back-end informe le front-end du résultat.
- Le front-end affiche le verdict à l’utilisateur.

### Diagramme de séquence Mermaid - Soumission fichier deepfake pour vérification

![Diagramme séquence soumission fichier deepfake](https://ppl-ai-code-interpreter-files.s3.amazonaws.com/web/direct-files/5f40220dd667f178207a4d38711815d4/79676a7a-99a1-4c73-a421-c4441aea5204/2ffba478.png)

---

## Cas 3 : Consultation des résultats précédents

Participants : Utilisateur, Front-end, Back-end, Base de données

Séquence :
- L’utilisateur demande l’historique de ses vérifications.
- Le front-end envoie une requête au back-end.
- Le back-end récupère les données dans la base de données.
- La base de données envoie les données au back-end.
- Le back-end retourne les données au front-end.
- Le front-end affiche l’historique des résultats.

### Diagramme de séquence Mermaid - Consultation historique

sequenceDiagram
participant Utilisateur
participant Front-end
participant Back-end
participant BaseDeDonnées

text
Utilisateur->>Front-end: Demande historique vérifications
Front-end->>Back-end: Requête historique
Back-end->>BaseDeDonnées: Récupère données
BaseDeDonnées-->>Back-end: Données
Back-end-->>Front-end: Envoie données historique
Front-end-->>Utilisateur: Affiche résultats
text
undefined
