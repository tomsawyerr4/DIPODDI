import streamlit as st
import re
from programmeSport import programme_semaine_utilisateur, save_to_pdf, translate_programme
import numpy as np
import streamlit as st
def get_specificite_weights(poste, profil, programme):
    weights = {
        "GARDIENS": {
            "PANTHERE (PUISSANT)": {
                'MUSCULATION EN SALLE': {
                    'ENDURANCE DE FORCE': 35,
                    'FORCE MAX': 35,
                    'MASSE MUSCULAIRE': 30,
                    'RÉPÉTITIONS DES EFFORTS': 25,
                    'FORCE EXPLOSIVE': 40
                },
                'MUSCULATION EN SALLE + CARDIO(Generale)': {
                    'ENDURANCE DE FORCE': 40,
                    'FORCE MAX': 40,
                    'PERTE DE POIDS': 20,
                    'REMISE EN FORME': 30,
                    'RÉPÉTITIONS DES EFFORTS': 45,
                    'FORCE EXPLOSIVE': 50
                },
                # Ajoutez les autres programmes de la même manière
            },
            "PIEUVRE (HABILE)": {
                # Structure similaire pour PIEUVRE
            },
            # Ajoutez les autres profils
        },
        # Ajoutez les autres postes (DÉFENSEURS, MILIEUX, ATTAQUANTS)
    }
    
    return (weights.get(poste, {}).get(profil, {}).get(programme, {}))

def choose_specificite(weights, current_specificite):
    if not weights:
        return current_specificite
    
    # Retire la spécificité actuelle pour éviter les répétitions
    filtered_weights = {k: v for k, v in weights.items() if k != current_specificite}
    
    if not filtered_weights:
        return current_specificite
    
    # Normalise les poids
    total = sum(filtered_weights.values())
    normalized = {k: v/total for k, v in filtered_weights.items()}
    
    # Choisit une spécificité aléatoire selon les poids
    choices = list(normalized.keys())
    probabilities = list(normalized.values())
    return np.random.choice(choices, p=probabilities)
    
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
    #nbr_seances = st.slider("Nombre de séances par semaine :", min_value=3, max_value=7, value=4)
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
    nbr_seances = len(jours_disponibles)
    if len(jours_disponibles) < 3:
        st.warning("Veuillez sélectionner au moins 3 jours.")
    
    if st.button("Générer le programme du mois"):
        st.success(f"Programme généré pour {prenom}")
        if len(jours_disponibles) >= 3:
            weights = get_specificite_weights(poste, profil, programme)
            
            for semaine in range(1, 5):
                st.markdown(f"### Semaine {semaine}")
                
                # Pour la semaine 1, on garde la spécificité choisie
                # À partir de la semaine 2, on choisit selon les poids
                current_specificite = specificite if semaine == 1 else choose_specificite(weights, specificite)
                
                resultat = programme_semaine_utilisateur(
                    choix=programme,
                    theme_principal=current_specificite,
                    nbr_seances=nbr_seances,
                    niveau=niveau
                )
                
                # Remplacer Jour 1, Jour 2... par les vrais jours choisis
                for i, jour in enumerate(jours_disponibles):
                    resultat = resultat.replace(f"Jour {i+1}", jour.upper())
                
                display_program(resultat)
                
                # Afficher la spécificité utilisée pour cette semaine
                if semaine > 1:
                    st.caption(f"Spécificité choisie: {current_specificite} (adaptée à votre profil {profil})")

if __name__ == "__main__":
    main()
