# 🧾 Stage 3 – Task 0 : Define User Stories and Mockups

## 📌 Purpose

Identifier et prioriser les fonctionnalités essentielles du **MVP** du projet de vérification des contenus falsifiés, et visualiser son interface.

---

## 1️⃣ Prioritized User Stories (MoSCoW)

### ✅ Must Have (Indispensable)

1. **En tant qu’utilisateur**, je veux **uploader une image, une vidéo ou un texte** afin de **vérifier son authenticité rapidement**.  
   **Critères d’acceptation :**  
   - Formats acceptés : JPG, PNG, MP4, TXT.  
   - Temps de traitement ≤ 30 secondes.  
   - Message d’erreur clair en cas de format ou échec.  

2. **En tant qu’utilisateur**, je veux **recevoir un score clair de fiabilité** afin de **savoir si le contenu est potentiellement falsifié**.  
   **Critères d’acceptation :**  
   - Affichage du score en jauge ou % clairement visible.  
   - Accompagnement par une explication synthétique.  
   - Réactivité : score mis à jour à la fin de l’analyse.

3. **En tant qu’utilisateur**, je veux **consulter l’historique de mes analyses précédentes** afin de **revoir mes résultats passés**.  
   **Critères d’acceptation :**  
   - Liste datée avec type de contenu et score.  
   - Tri / filtre disponible.  
   - Accès sécurisé uniquement par utilisateur connecté.

### 🟠 Should Have (Souhaitable)

4. **En tant qu’utilisateur**, je veux **obtenir des recommandations fiables après chaque analyse** afin de **m’améliorer dans la détection de contenus falsifiés**.  
   **Critères d’acceptation :**  
   - Recommandations claires affichées sous le score.  
   - Liens vers ressources ou bonnes pratiques.  

5. **En tant qu’utilisateur**, je veux **pouvoir supprimer une analyse de mon historique** afin de **garder mon compte organisé et confidentiel**.  
   **Critères d’acceptation :**  
   - Option “supprimer” pour chaque entrée historique.  
   - Confirmation préalable demandée.  
   - Suppression effective et interface mise à jour.

### 🟡 Could Have (Optionnel)

6. **En tant qu’utilisateur avancé**, je veux **recevoir des alertes en temps réel lorsqu’un contenu déjà vérifié est signalé comme faux**, afin de **mettre à jour mes informations rapidement**.  
   **Critères d’acceptation :**  
   - Notifications push ou par email configurables.  
   - Historique des alertes consultable.

### ❌ Won’t Have (Exclus)

7. **En tant qu’utilisateur**, je ne pourrai **pas partager automatiquement mes résultats sur les réseaux sociaux** lors de ce MVP.

---

## 2️⃣ Mockups des Écrans Principaux

> Ces maquettes sont réalisées dans Figma et disponibles dans le dossier `/mockups`.

https://www.figma.com/make/yb80inSDEsAazjayCkP7CW/Responsive-Deepfake-Detection-Site?node-id=0-4&t=KQxwO0GWxb36vs1E-1

### 🖼️ Écran d’accueil

- Champ pour uploader une image, vidéo ou texte.  
- Bouton “Analyser”.  
- Lien vers l’historique.

### 📊 Écran de résultats

- Jauge affichant le score de fiabilité.  
- Texte avec recommandations.  
- Boutons pour “Retour à l’accueil” et “Voir l’historique”.

### 📜 Écran d’historique

- Liste des analyses passées avec date, type de contenu, score.  
- Option pour supprimer une analyse.

---

## 3️⃣ Liens Utiles

- [Guide to Writing User Stories](https://www.atlassian.com/agile/project-management/user-stories)  
- [Wireframe vs. Mock-up: what’s the difference?](https://www.justinmind.com/blog/wireframes-vs-mockups)  
- [Figma tutorial for Beginners](https://www.youtube.com/watch?v=FTFaQWZBqQ8)
