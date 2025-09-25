# Stage 3 – Task 1 : Design System Architecture

## Architecture du système

Ce diagramme présente les composants principaux du système MVP de vérification de contenus falsifiés :

- **Front-end** : Application web utilisant React.js pour l’interface utilisateur. Permet d’uploader du contenu, consulter les résultats et l’historique.
- **Back-end / API** : Serveur Node.js avec Express, traitant les requêtes, validant les contenus et orchestrant les appels aux services d’analyse.
- **Base de données** : PostgreSQL (ou choix similaire) pour stocker les profils utilisateurs, les analyses et historiques.
- **Services externes d’analyse** : APIs/moteurs d’intelligence artificielle dédiés à la détection de falsifications.

## Flux de données

1. L’utilisateur dépose un fichier (image, vidéo, texte) via le front-end.
2. Le backend reçoit et valide le contenu, envoie la requête d’analyse aux services externes.
3. Les résultats de l’analyse sont retournés et stockés dans la base de données.
4. Les résultats sont renvoyés au front-end pour affichage à l’utilisateur.
5. L’historique des analyses est consultable via le front-end, avec données récupérées depuis la base.

![Diagramme d'architecture système simplifié](https://ppl-ai-code-interpreter-files.s3.amazonaws.com/web/direct-files/004672192487e22c40afe2ca38aaa6db/a1e45b7b-a238-4d1b-9a2b-c44a2c1c0799/184aad95.png)

---

## Outils technologiques envisagés

- Frontend : React.js  
- Backend : Node.js, Express  
- Base de données : PostgreSQL  
- Services externes : API d’analyse IA (ex. deepfake detection APIs)
