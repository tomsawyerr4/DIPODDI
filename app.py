import streamlit as st
import re
from programmeSport import programme_semaine_utilisateur, save_to_pdf, translate_programme
import re
import streamlit as st

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
            line = line.replace(url, f"\n[Voir la vidéo]({url})")
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
            
            # Traite le texte en conservant les sauts de ligne
            resultat_avec_liens = make_clickable_preserve_newlines(resultat)
            
            # Affiche le résultat avec markdown (qui interprète les sauts de ligne)
            st.markdown(resultat_avec_liens)
if __name__ == "__main__":
    main()
