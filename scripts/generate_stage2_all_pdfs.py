import os
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

# --- Dossier de sortie ---
output_dir = "../Stage_2_Project_Charter/docs"
os.makedirs(output_dir, exist_ok=True)

# ========== TÂCHE 0 : Project Objectives ==========
task0_path = os.path.join(output_dir, "Project_Charter_Portfolio_Stage2.pdf")
doc0 = SimpleDocTemplate(task0_path, pagesize=A4)
styles = getSampleStyleSheet()
story0 = []

# Title
story0.append(Paragraph("Project Charter – Portfolio Project (Stage 2)", styles['Title']))
story0.append(Spacer(1, 20))

# Section 0: Project Objectives (enrichie)
story0.append(Paragraph("0. Project Objectives", styles['Heading2']))
story0.append(Paragraph(
    "<b>Purpose / Contexte</b><br/>"
    "Ce portfolio a pour objectif de centraliser et valoriser mes projets et compétences techniques. "
    "Il servira à démontrer ma capacité à concevoir des interfaces web modernes et à gérer un projet de A à Z.", styles['Normal']
))
story0.append(Spacer(1, 12))
story0.append(Paragraph(
    "<b>Objectives (SMART)</b><br/>"
    "1. Développer un site portfolio responsive <b>en 6 semaines</b>, incluant au minimum 3 projets documentés.<br/>"
    "2. Offrir une interface intuitive et moderne, permettant une navigation fluide et un accès rapide aux informations.<br/>"
    "3. Ajouter une section contact fonctionnelle pour faciliter la prise de contact par les recruteurs.<br/>"
    "4. Garantir la conformité aux standards HTML/CSS et bonnes pratiques d'accessibilité.", styles['Normal']
))
story0.append(Spacer(1, 12))
story0.append(Paragraph(
    "<b>Expected Impact</b><br/>"
    "1. Améliorer la visibilité et la crédibilité professionnelle auprès des enseignants et recruteurs.<br/>"
    "2. Consolider l'apprentissage technique et la gestion de projet.<br/>"
    "3. Créer un portfolio réutilisable et évolutif pour de futurs projets.", styles['Normal']
))
story0.append(Spacer(1, 20))

# Build PDF Tâche 0
doc0.build(story0)
print(f"✅ PDF Tâche 0 généré : {task0_path}")

# ========== TÂCHE 1 : Stakeholders and Team Roles ==========
task1_path = os.path.join(output_dir, "Stage2_Task1_Stakeholders_Roles.pdf")
doc1 = SimpleDocTemplate(task1_path, pagesize=A4)
story1 = []

# Title
story1.append(Paragraph("Stage 2 – Task 1: Identify Stakeholders and Team Roles", styles['Title']))
story1.append(Spacer(1, 20))

# Introduction
story1.append(Paragraph(
    "Cette section identifie toutes les parties prenantes du projet de portfolio et définit leurs rôles et responsabilités. "
    "Comprendre et documenter ces éléments garantit une communication efficace et une responsabilité claire.", styles['Normal']
))
story1.append(Spacer(1, 20))

# Parties prenantes internes et externes
story1.append(Paragraph("<b>Parties prenantes</b>", styles['Heading2']))
data = [
    ["Type", "Nom", "Rôle / Intérêt"],
    ["Interne", "Cisse Ahmed", "Développeur, chef de projet, responsable de toutes les décisions."],
    ["Externe", "Instructeurs", "Fournissent des directives et du feedback pour améliorer le projet."],
    ["Externe", "Recruteurs / Utilisateurs finaux", "Évaluent le portfolio pour des opportunités professionnelles."]
]
table = Table(data, colWidths=[80, 120, 280])
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
    ('BOX', (0, 0), (-1, -1), 0.5, colors.black),
]))
story1.append(table)
story1.append(Spacer(1, 20))

# Rôles de l'équipe
story1.append(Paragraph("<b>Rôles de l'équipe</b>", styles['Heading2']))
roles_text = """
<ul>
<li><b>Chef de projet (Project Manager)</b> : Planifie, suit les progrès, gère le budget et les risques, s'assure que les délais sont respectés.</li>
<li><b>Développeur / Designer</b> : Crée l'interface utilisateur, le code backend, s'assure que le site est responsive et respectueux des standards web.</li>
<li><b>Rédacteur / QA</b> : Rédige les textes, relecture, vérification orthographique, test des fonctionnalités et expérience utilisateur.</li>
</ul>
"""
story1.append(Paragraph(roles_text, styles['Normal']))
story1.append(Spacer(1, 12))

# Responsabilités clés
story1.append(Paragraph("<b>Responsabilités clés</b>", styles['Heading2']))
responsibilities = """
<ol>
<li><b>Communication</b> : Maintenir un échange régulier avec les instructeurs et collecter du feedback.</li>
<li><b>Gestion des risques</b> : Identifier les blocages techniques et retards potentiels, proposer des solutions.</li>
<li><b>Qualité</b> : S'assurer que le portfolio est esthétique, fonctionnel, responsive et accessible.</li>
<li><b>Livraison et déploiement</b> : Mettre en ligne un site documenté et maintenable.</li>
<li><b>Suivi des KPIs</b> : Mesurer l’engagement des utilisateurs et la performance du site.</li>
<li><b>Documentation</b> : Tenir un journal de projet et rédiger un rapport final synthétique pour les parties prenantes.</li>
</ol>
"""
story1.append(Paragraph(responsibilities, styles['Normal']))
story1.append(Spacer(1, 20))

# Hiérarchisation des parties prenantes
story1.append(Paragraph("<b>Priorisation des parties prenantes</b>", styles['Heading2']))
stakeholder_matrix = [
    ["Partie prenante", "Influence", "Intérêt", "Stratégie"],
    ["Cisse Ahmed", "Haute", "Haute", "Gestion active et planification continue"],
    ["Instructeurs", "Moyenne", "Haute", "Communication régulière et feedback"],
    ["Recruteurs / Utilisateurs finaux", "Faible", "Haute", "Informer et montrer valeur du portfolio"]
]
table2 = Table(stakeholder_matrix, colWidths=[150, 80, 80, 150])
table2.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
    ('BOX', (0, 0), (-1, -1), 0.5, colors.black),
]))
story1.append(table2)
story1.append(Spacer(1, 20))

# Build PDF Tâche 1
doc1.build(story1)
print(f"✅ PDF Tâche 1 généré : {task1_path}")

# ==============================
# === TÂCHE 2 : Define Scope
# ==============================
task2_path = os.path.join(output_dir, "Stage2_Task2_Define_Scope.pdf")
doc2 = SimpleDocTemplate(task2_path, pagesize=A4)
story2 = []
story2.append(Paragraph("Stage 2 – Task 2: Define Scope", styles['Title']))
story2.append(Spacer(1, 20))
story2.append(Paragraph(
    "Cette section définit ce que le projet livrera (<b>in-scope</b>) et ce qui ne sera pas inclus (<b>out-of-scope</b>) "
    "afin de concentrer les efforts sur les éléments essentiels.", styles['Normal']
))
story2.append(Spacer(1, 20))

# In-Scope et Out-of-Scope
story2.append(Paragraph("<b>In-Scope (Inclus dans le projet)</b>", styles['Heading2']))
story2.append(Paragraph(
    "<ul>"
    "<li>Création d’un site portfolio responsive utilisant HTML, CSS et JavaScript.</li>"
    "<li>Présentation d’au moins trois projets documentés (description, visuels, liens GitHub).</li>"
    "<li>Section 'Compétences' présentant les langages et outils maîtrisés.</li>"
    "<li>Section Contact fonctionnelle (formulaire ou liens directs).</li>"
    "<li>Déploiement sur une plateforme gratuite (GitHub Pages).</li>"
    "<li>Mise en place d’un design moderne, lisible et accessible.</li>"
    "</ul>", styles['Normal']
))
story2.append(Spacer(1, 12))

story2.append(Paragraph("<b>Out-of-Scope (Exclus du projet)</b>", styles['Heading2']))
story2.append(Paragraph(
    "<ul>"
    "<li>Développement d’un blog complet ou d’un système CMS intégré.</li>"
    "<li>Création d’une base de données ou backend complexe.</li>"
    "<li>Optimisation SEO avancée ou intégration marketing payante.</li>"
    "<li>Automatisation de l’import des projets depuis GitHub/LinkedIn.</li>"
    "<li>Fonctionnalités d’e-commerce ou de paiement en ligne.</li>"
    "</ul>", styles['Normal']
))
doc2.build(story2)
print(f"✅ PDF Tâche 2 généré : {task2_path}")

# ==============================
# === TÂCHE 3 : Identify Risks
# ==============================
task3_path = os.path.join(output_dir, "Stage2_Task3_Identify_Risks.pdf")
doc3 = SimpleDocTemplate(task3_path, pagesize=A4)
story3 = []
story3.append(Paragraph("Stage 2 – Task 3: Identify Risks", styles['Title']))
story3.append(Spacer(1, 20))
story3.append(Paragraph(
    "Cette section identifie les risques potentiels du projet et propose des stratégies de mitigation pour chacun.",
    styles['Normal']
))
story3.append(Spacer(1, 12))

# Tableau des risques
data_risks = [
    ["Risque", "Catégorie", "Stratégie de mitigation"],
    ["Manque de temps pour finaliser certaines fonctionnalités", "Timeline",
     "Établir un planning réaliste, prioriser les tâches essentielles, utiliser un suivi régulier."],
    ["Difficultés techniques avec les outils ou frameworks utilisés", "Technical",
     "Prévoir une phase de recherche et tests préliminaires ; solliciter de l’aide ou des ressources en ligne."],
    ["Perte de données ou corruption de fichiers", "Technical",
     "Utiliser un contrôle de version (GitHub) et des sauvegardes régulières."],
    ["Feedback tardif ou insuffisant des instructeurs", "Communication",
     "Fixer des jalons clairs et envoyer des rappels réguliers pour obtenir du feedback."],
    ["Perte de motivation ou surcharge de travail", "Team Dynamics",
     "Planifier des pauses, maintenir un rythme soutenable et célébrer les progrès réalisés."]
]
table_risks = Table(data_risks, colWidths=[200, 100, 200])
table_risks.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
    ('BOX', (0, 0), (-1, -1), 0.5, colors.black),
]))
story3.append(table_risks)
doc3.build(story3)
print(f"✅ PDF Tâche 3 généré : {task3_path}")

# ==============================
# --- Task 4: Develop a High-Level Plan ---
# ==============================
task4_path = os.path.join(output_dir, "Stage2_Task4_High_Level_Plan.pdf")
doc4 = SimpleDocTemplate(task4_path, pagesize=A4)
story4 = []

story4.append(Paragraph("Stage 2 – Task 4: Develop a High-Level Plan", styles['Title']))
story4.append(Spacer(1, 20))

story4.append(Paragraph(
    "Cette section présente les grandes phases et jalons du projet sous forme de plan simplifié. "
    "Elle aide à visualiser la progression et les livrables clés.", styles['Normal']
))
story4.append(Spacer(1, 20))

# Phases principales
phases_data = [
    ["Stage", "Description", "Jalons / Livrables", "Durée estimée"],
    ["Stage 1: Idea Development", "Génération et validation d'idées.", "Liste d'idées validées", "Semaine 1-2 (Terminé)"],
    ["Stage 2: Project Charter Development", "Rédaction de la charte et des livrables initiaux.", "Project Charter, Scope, Risks", "Semaine 3-4 (En cours)"],
    ["Stage 3: Technical Documentation", "Création des spécifications techniques et architecture.", "Docs techniques complètes", "Semaine 5-6"],
    ["Stage 4: MVP Development", "Développement du produit minimum viable.", "Version MVP fonctionnelle", "Semaine 7-10"],
    ["Stage 5: Project Closure", "Présentation finale, rétrospective et clôture.", "Présentation finale et rapport", "Semaine 11-12"]
]
table4 = Table(phases_data, colWidths=[120, 150, 150, 80])
table4.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
    ('BOX', (0, 0), (-1, -1), 0.5, colors.black),
]))
story4.append(table4)
story4.append(Spacer(1, 20))

# Résumé visuel
story4.append(Paragraph(
    "<b>Résumé visuel :</b> Le projet suit un enchaînement clair, du développement d'idées jusqu'à la clôture, "
    "avec des jalons hebdomadaires pour assurer un suivi efficace.", styles['Normal']
))

doc4.build(story4)
print(f"✅ PDF Tâche 4 généré : {task4_path}")

