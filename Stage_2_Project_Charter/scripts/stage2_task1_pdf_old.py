import os
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

# --- Dossier et nom du PDF ---
output_dir = "../Stage_2_Project_Charter/docs"
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "Stage2_Task1_Stakeholders_Roles.pdf")

# --- Configuration du document ---
doc = SimpleDocTemplate(output_path, pagesize=A4)
styles = getSampleStyleSheet()
story = []

# --- Titre ---
story.append(Paragraph("Stage 2 – Task 1: Identify Stakeholders and Team Roles", styles['Title']))
story.append(Spacer(1, 20))

# --- Introduction ---
story.append(Paragraph(
    "Cette section identifie toutes les parties prenantes du projet de portfolio et définit leurs rôles et responsabilités. "
    "Comprendre et documenter ces éléments garantit une communication efficace et une responsabilité claire.", styles['Normal']
))
story.append(Spacer(1, 20))

# --- Parties prenantes internes et externes ---
story.append(Paragraph("<b>Parties prenantes</b>", styles['Heading2']))
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
story.append(table)
story.append(Spacer(1, 20))

# --- Rôles de l'équipe ---
story.append(Paragraph("<b>Rôles de l'équipe</b>", styles['Heading2']))
roles_text = """
<ul>
<li><b>Chef de projet (Project Manager)</b> : Planifie, suit les progrès et s'assure que les délais sont respectés.</li>
<li><b>Développeur / Designer</b> : Crée l'interface utilisateur, le code backend et s'assure que le site est responsive.</li>
<li><b>Rédacteur / QA</b> : Rédige les textes, relit le contenu, teste les fonctionnalités et la qualité.</li>
</ul>
"""
story.append(Paragraph(roles_text, styles['Normal']))
story.append(Spacer(1, 20))

# --- Responsabilités détaillées ---
story.append(Paragraph("<b>Responsabilités clés</b>", styles['Heading2']))
responsibilities = """
<ol>
<li><b>Communication</b> : Maintenir un échange régulier avec les instructeurs et collecter du feedback.</li>
<li><b>Gestion des risques</b> : Identifier les blocages techniques et les retards potentiels.</li>
<li><b>Qualité</b> : S'assurer que le portfolio est esthétique, fonctionnel et respecte les standards du web.</li>
<li><b>Livraison</b> : Générer un site déployé et documenté dans les délais impartis.</li>
</ol>
"""
story.append(Paragraph(responsibilities, styles['Normal']))

# --- Génération du PDF ---
doc.build(story)
print(f"✅ PDF généré : {output_path}")

