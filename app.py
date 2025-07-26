import streamlit as st
import re
from programmeSport import programme_semaine_utilisateur, save_to_pdf, translate_programme


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

    if st.button(" Générer le programme du mois"):
        st.success(f"Programme généré pour {prenom}")
        for semaine in range(1, 5):
            st.markdown(f"### Semaine {semaine}")
            resultat = programme_semaine_utilisateur(
                choix=programme,
                theme_principal=specificite,
                nbr_seances=nbr_seances,
                niveau=niveau
            )
            st.markdown(formatter_texte_avec_liens(resultat), unsafe_allow_html=True)


if __name__ == "__main__":
    main()
