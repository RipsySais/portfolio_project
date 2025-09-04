import os
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# Chemin du dossier docs
output_folder = "../Stage_2_Project_Charter/docs"
os.makedirs(output_folder, exist_ok=True)  # crée le dossier s'il n'existe pas

# Chemin complet du PDF
output_path = os.path.join(output_folder, "Project_Charter_Portfolio_Stage2.pdf")

doc = SimpleDocTemplate(output_path, pagesize=A4)
styles = getSampleStyleSheet()
story = []

# Title
story.append(Paragraph("Project Charter – Portfolio Project (Stage 2)", styles['Title']))
story.append(Spacer(1, 20))

# Section 0: Project Objectives
story.append(Paragraph("0. Project Objectives", styles['Heading2']))
story.append(Paragraph(
    "<b>Purpose</b><br/>"
    "Le projet a pour but de développer un <b>portfolio en ligne interactif et responsive</b>, "
    "servant de vitrine professionnelle pour présenter mes compétences et les projets que j’ai réalisés. "
    "Ce portfolio est essentiel car il facilitera la mise en valeur de mon parcours auprès d’enseignants "
    "et de recruteurs potentiels, tout en consolidant mon apprentissage des technologies web.", styles['Normal']
))
story.append(Spacer(1, 12))
story.append(Paragraph(
    "<b>Objectives</b><br/>"
    "1. Concevoir et mettre en ligne un site portfolio responsive en <b>6 semaines</b>, intégrant au minimum "
    "trois projets documentés avec description, visuels et lien vers le code source.<br/>"
    "2. Développer une interface claire et moderne qui permette aux visiteurs de naviguer facilement entre les "
    "différentes sections (projets, compétences, contact).<br/>"
    "3. Ajouter une section de contact fonctionnelle pour permettre aux visiteurs ou recruteurs de prendre rapidement "
    "contact avec moi.", styles['Normal']
))

doc.build(story)
print(f"PDF Stage 2 généré : {output_path}")
