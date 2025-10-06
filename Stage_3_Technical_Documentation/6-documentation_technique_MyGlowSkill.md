# Documentation Technique du Projet MyGlowSkill (MVP)

---

## 1. User Stories et Mockups

### 1.1 Priorités des User Stories (MoSCoW)
- Must Have :  
  - Exemple : En tant qu’utilisateur, je veux uploader une image, vidéo ou texte...
- Should Have :  
  - Exemple : En tant qu’utilisateur, je veux recevoir des recommandations...
- Could Have :  
  - Exemple : En tant qu’utilisateur avancé, je veux recevoir des alertes en temps réel...
- Won’t Have :  
  - Exemple : Partage automatique sur réseaux sociaux.

### 1.2 Mockups
- Lien vers maquettes Figma  
- Description sommaire des écrans (Accueil, Résultats, Historique)

---

## 2. Architecture du Système

- Description des composants principaux (Frontend React, Backend Node.js/Express, Base MongoDB, APIs externes)
- Diagramme d'architecture (image ou lien)

---

## 3. Composants, Classes, et Design de la Base de Données

### 3.1 Backend : Classes clés
- User : attributs, méthodes  
- Data : attributs, méthodes  
- Alert : attributs, méthodes  
- Subscription : attributs, méthodes

### 3.2 Base de données
- Description des collections MongoDB avec exemples de documents  
- Ou schéma ER si base relationnelle

---

## 4. Diagrammes de Séquence

- Séquence Connexion utilisateur (diagramme Mermaid)  
- Séquence Soumission fichier (image/diagramme)  
- Séquence Consultation historique (diagramme Mermaid)

---

## 5. Spécifications API

### 5.1 APIs externes
- Liste des APIs externes utilisées avec rôle et justification

### 5.2 API interne
| URL Path           | Méthode HTTP | Entrée (format)                   | Sortie (format)            | Description                    |
|--------------------|--------------|---------------------------------|----------------------------|------------------------------|
| `/api/auth/register`| POST         | JSON                            | JSON                       | Inscription utilisateur       |
| `/api/auth/login`   | POST         | JSON                            | JSON                       | Authentification utilisateur  |
| ...                | ...          | ...                             | ...                        | ...                          |

---

## 6. Plans SCM & QA

### 6.1 SCM
- Outil : Git  
- Branches : main, develop, feature, release, hotfix  
- Processus : commits réguliers, PR & revues, intégration continue

### 6.2 QA
- Types de tests : unitaires, intégration, E2E  
- Outils : Jest, Cypress, Postman  
- Pipeline déploiement staging et prod

---

## 7. Justifications Techniques

- Choix technologiques (React, Node.js, MongoDB)  
- Architecture modulaire et évolutive  
- Intégration API externes et automatisation tests

---
