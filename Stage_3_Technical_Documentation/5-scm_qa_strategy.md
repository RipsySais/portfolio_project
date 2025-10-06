# 5. Plan SCM et Stratégies QA

## 5.1 Stratégie SCM (Gestion du code source)

- **Outil de contrôle de version** : Git, utilisé pour toute la gestion des versions et du code.
- **Branches principales** :
  - `main` (ou `master`) : branche stable en production.
  - `develop` : branche d’intégration où toutes les fonctionnalités sont fusionnées avant release.
- **Branches temporaires** :
  - `feature/nom-fonctionnalité` : une branche par fonctionnalité développée, créée à partir de `develop`.
  - `release/num-version` : branche dédiée à la préparation d’une nouvelle version (tests, corrections).
  - `hotfix/num-version` : correction rapide de bugs en production, à partir de `main`.
- **Processus** :
  - Push régulier des commits atomiques et bien commentés.
  - Revues de code systématiques avec des Pull Requests avant fusion sur `develop` ou `main`.
  - Intégration continue avec tests automatiques à chaque PR.
- **Outils complémentaires** : GitHub (ou GitLab) pour la gestion des PR et tracking.

## 5.2 Stratégie QA (Assurance qualité)

- **Types de tests** :
  - Tests unitaires : couvrant les fonctions et classes, exécutés automatiquement.
  - Tests d’intégration : validation des interactions entre modules.
  - Tests de bout en bout (E2E) : simulation des scénarios utilisateur complets.
- **Outils de test** :
  - Backend : Jest, Supertest pour les tests unitaires et intégration des APIs.
  - Frontend : Jest, React Testing Library pour les composants.
  - API : Postman pour tests manuels ou automatisés des endpoints.
  - E2E : Cypress ou Playwright pour automatiser les tests du workflow utilisateur.
- **Pipeline de déploiement** :
  - Environnement staging : déploiement automatique après validation des tests unitaires et d’intégration.
  - Environnement production : déploiement après validation complète des tests E2E et revue finale.
- **Processus QA** :
  - Exécution automatique des tests à chaque push sur branches de fonctionnalité et `develop`.
  - Revue manuelle des cas critiques et tests exploratoires en QA.
  - Surveillance post-déploiement pour détecter rapidement les bugs en production.
