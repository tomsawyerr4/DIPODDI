import streamlit as st
import re
from programmeSport import programme_semaine_utilisateur, save_to_pdf, translate_programme
import re
import streamlit as st
def display_program(content):
    # Séparer le contenu en lignes
    lines = content.split('\n')
    
    # Traiter chaque ligne
    for line in lines:
        # Détecter les liens
        match = re.search(r'(https?://\S+)', line)
        
        if match:
            # Ligne avec lien - afficher "Vidéo" centré et cliquable
            url = match.group(0)
            st.markdown(
                f'<div style="text-align: center; margin: 10px 0;">'
                f'<a href="{url}" style="color: blue; text-decoration: none;">Vidéo</a>'
                f'</div>',
                unsafe_allow_html=True
            )
        elif "Echauffement" in line:
            # Échauffement - texte centré avec soulignement
            st.markdown(
                f'<div style="text-align: center; margin: 10px 0; border-bottom: 1px solid black; '
                f'padding-bottom: 5px;">{line}</div>',
                unsafe_allow_html=True
            )
        elif line.strip() and (line.isupper() or line.startswith("Jour") or line.startswith("PARTIE BONUS")):
            # Titres en gras et centrés
            st.markdown(
                f'<div style="text-align: center; margin: 10px 0; font-weight: bold;">{line}</div>',
                unsafe_allow_html=True
            )
        else:
            # Texte normal centré
            st.markdown(
                f'<div style="text-align: center; margin: 5px 0;">{line}</div>',
                unsafe_allow_html=True
            )
            
def make_clickable_preserve_newlines(text):
    # Divise le texte en lignes tout en conservant les sauts de ligne
    lines = text.split('\n')
    
    # Traite chaque ligne séparément
    processed_lines = []
    for line in lines:
        # Trouve tous les URLs dans la ligne
        urls = re.findall(r'(https?://\S+)', line)
        # Remplace chaque URL par un lien markdown
        for url in urls:
            line = line.replace(url, f"\n[Voir la vidéo]({url})\n")
        processed_lines.append(line)
    
    # Recombine les lignes avec les sauts de ligne originaux
    return '\n'.join(processed_lines)
    
def make_links_clickable(text):
    # Trouve tous les URLs dans le texte
    urls = re.findall(r'(https?://\S+)', text)
    
    # Remplace chaque URL par un lien markdown
    for url in urls:
        text = text.replace(url, f"[Voir la vidéo]({url})")
    
    return text
def make_contextual_links(text):
    # Pattern pour détecter les URLs précédées d'une description
    pattern = re.compile(r'(Pour voir l\'exercice en Vidéo): (https?://\S+)')
    
    def replace_match(match):
        return f"{match.group(1)}: [cliquez ici ]({match.group(2)})"
    
    return pattern.sub(replace_match, text)

def mettre_a_jour_specificite(programme):
    if programme == 'MUSCULATION EN SALLE':
        return ["ENDURANCE DE FORCE", "FORCE MAX", "MASSE MUSCULAIRE", 
                "PERTE DE POIDS", "REMISE EN FORME", "RÉPÉTITIONS DES EFFORTS", 
                "FORCE EXPLOSIVE"]
    elif programme == 'MUSCULATION EN SALLE (Specifique)':
        return ["BRAS", "DOS", "ÉPAULE", "PECTORAUX", "JAMBES"]
    elif programme == 'MUSCULATION EN SALLE + CARDIO(Generale)':
        return ["ENDURANCE DE FORCE", "FORCE MAX", 
                "PERTE DE POIDS", "REMISE EN FORME", "RÉPÉTITIONS DES EFFORTS", 
                "FORCE EXPLOSIVE"]
    elif programme == 'MUSCULATION EN SALLE + CARDIO(Specifique)':
        return ["BRAS", "DOS", "ÉPAULE", "PECTORAUX", "JAMBES"]
    elif programme == 'CARDIO EN SALLE':
        return ["PUISSANCE", "ENDURANCE", "RÉSISTANCE", "SPRINT"]
    elif programme == 'PROGRAMME MAISON':
        return ["Perte DE POIDS", "RENFORCEMENT", "BRULER DES CALORIES"]
    elif programme == 'PROGRAMME DEHORS':
        return ["PERTE DE POIDS", "PUISSANCE", "REMISE EN FORME", "BOX TO BOX"]
    return []


def rendre_liens_cliquables(texte):
    return re.sub(r'(https?://\S+)', r'[\1](\1)', texte)


def formatter_texte_avec_liens(texte):
    # Convertir les liens en format Markdown cliquable
    texte = re.sub(r'(https?://[^\s]+)', r'[\1](\1)', texte)
    # Remplacer les retours à la ligne simples par deux espaces + retour à la ligne (Markdown)
    texte = texte.replace('\n', '  \n')
    return texte
def main():
    st.title("Générateur de Programme Sportif Personnalisé DIPODDI")

    prenom = st.text_input("Prénom :", value="user")

    discipline = st.selectbox("Quel est votre discipline ?", ["FOOTBALL", "FUTSAL"])
    poste = st.selectbox("Quel est votre poste ?", ["GARDIENS", "DÉFENSEURS", "MILIEUX", "ATTAQUANTS"])

    profils = {
        "GARDIENS": ["PANTHERE (PUISSANT)", "PIEUVRE (HABILE)", "ARAIGNEE (MALIN)", "CHAT (EXPLOSIF)"],
        "DÉFENSEURS": ["CASSEUR (DURE)", "CONTROLEUR (MAITRISE)", "POLYVALENT (ADAPTATION)", "RELANCEUR (PROPRE)"],
        "MILIEUX": ["ARCHITECTE (CONSTRUCTION)", "GAZELLE (CARDIO)", "PITBULL (AGRESSIF)", "ROCK (UNE MACHINE)"],
        "ATTAQUANTS": ["MAGICIEN (TALENTUEUX)", "RENARD (FINISSEUR)", "SNIPER (PRECISION)", "TANK (PUISSANT)"]
    }

    profil = st.selectbox("Quel est votre profil ?", profils[poste])
    blessure = st.radio("Avez-vous une blessure ou douleur actuelle ?", ["NON", "OUI"])
    
    localisation = ""
    if blessure == "OUI":
        localisation = st.selectbox("Où se situe la blessure ?", [
            "CHEVILLES", "GENOUX", "HANCHES", "PIEDS", "ADDUCTEURS", "FESSIERS",
            "ISCHIOS JAMBIERS", "MOLLETS", "MOYEN FESSIERS", "PSOAS FLECHISSEURS", "QUADRICEPS"
        ])

    niveau = st.selectbox("Votre niveau :", ['Debutant', 'Intermidiaire', 'Avance'])
    programme = st.selectbox("Choisissez un programme :", [
        'MUSCULATION EN SALLE',
        'MUSCULATION EN SALLE (Specifique)',
        'MUSCULATION EN SALLE + CARDIO(Generale)',
        'MUSCULATION EN SALLE + CARDIO(Specifique)',
        'CARDIO EN SALLE',
        'PROGRAMME MAISON',
        'PROGRAMME DEHORS'
    ])

    specificites = mettre_a_jour_specificite(programme)
    specificite = st.selectbox("Spécificité :", specificites)
    nbr_seances = st.slider("Nombre de séances par semaine :", min_value=3, max_value=7, value=4)
    est_dans_club = st.radio("Êtes-vous dans un club ?", ["OUI", "NON"])
    
    jours_match = []
    if est_dans_club == "OUI":
        jours_match = st.multiselect(
            "Quels jours avez-vous match ?",
            ["LUNDI", "MARDI", "MERCREDI", "JEUDI", "VENDREDI", "SAMEDI", "DIMANCHE"],
            default=[]
        )
    
    jours_disponibles = st.multiselect(
        "Quels jours voulez-vous effectuer votre programme DIPODDI ? (3 jours min)",
        ["LUNDI", "MARDI", "MERCREDI", "JEUDI", "VENDREDI", "SAMEDI", "DIMANCHE"],
        default=["LUNDI", "MERCREDI", "VENDREDI"]
    )
    
    if len(jours_disponibles) < 3:
        st.warning("Veuillez sélectionner au moins 3 jours.")
    

    
    if st.button("Générer le programme du mois"):
        st.success(f"Programme généré pour {prenom}")
        for semaine in range(1, 5):
            st.markdown(f"### Semaine {semaine}")
            resultat = programme_semaine_utilisateur(
                choix=programme,
                theme_principal=specificite,
                nbr_seances=nbr_seances,
                niveau=niveau
            )
            display_program(resultat)


if __name__ == "__main__":
    main()
