import streamlit as st
import re
from programmeSport import programme_semaine_utilisateur
from getSpecificite import  get_specificite_weights, choose_specificite
import numpy as np
from datetime import datetime, timedelta
import locale

JOURS_TRADUCTION = {
    'Monday': 'Lundi',
    'Tuesday': 'Mardi',
    'Wednesday': 'Mercredi',
    'Thursday': 'Jeudi',
    'Friday': 'Vendredi',
    'Saturday': 'Samedi',
    'Sunday': 'Dimanche'
}


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


def display_seance(contenu):
    lines = contenu.split('\n')
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        if line.startswith("Echauffement"):
            st.markdown(f"*{line}*")
        elif line.isupper() or line.startswith("PARTIE BONUS"):
            st.markdown(f"**{line}**")
        elif re.match(r'https?://\S+', line): 
            st.markdown(f"[Vidéo↗]({line})")
        else:
            st.markdown(line)

def main():
    st.title("Générateur de Programme Sportif Personnalisé DIPODDI")
    st.header("VEUILLEZ SAISIR VOS COORDONNÉES")
    
    col1, col2 = st.columns(2)
    with col1:
        prenom = st.text_input("PRÉNOM ", value="")
    with col2:
        nom = st.text_input("NOM ", value="")
    
    genre = st.radio("SEXE ", ["HOMME", "FEMME"], horizontal=True)
    
    col3, col4, col5 = st.columns(3)
    with col3:
        taille = st.number_input("TAILLE (cm) ", min_value=100, max_value=250, value=175)
    with col4:
        poids = st.number_input("POIDS (kg) ", min_value=30, max_value=200, value=70)
    with col5:
        age = st.number_input("ÂGE ", min_value=10, max_value=100, value=25)
    
    email = st.text_input("EMAIL ", value="")

    st.header("VOS PRÉFÉRENCES SPORTIVES")
    
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
        'MUSCULATION EN SALLE + CARDIO(Generale)',
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
    
    # Filtrer les jours disponibles pour exclure les jours de match
    jours_entrainement_possibles = [jour for jour in ["LUNDI", "MARDI", "MERCREDI", "JEUDI", "VENDREDI", "SAMEDI", "DIMANCHE"] 
                                  if jour not in jours_match]
    
    jours_disponibles = st.multiselect(
        "Quels jours voulez-vous effectuer votre programme DIPODDI ? (2 jours minimun)",
        jours_entrainement_possibles,
        default=[jour for jour in ["LUNDI", "MERCREDI", "VENDREDI"] if jour not in jours_match]
    )
    
    nbr_seances = len(jours_disponibles)
    if len(jours_disponibles) < 2:
            st.warning("Veuillez sélectionner au moins 2 jours (hors jours de match).")
    if st.button("Générer le programme du mois"):
        st.success(f"Programme généré pour {prenom if prenom else 'User'}")
        if len(jours_disponibles) >= 2:
            weights = get_specificite_weights(poste, profil, programme)
            
            today = datetime.now()
            start_date = today - timedelta(days=today.weekday())  # Lundi
            
            for semaine in range(1, 5):
                current_specificite = specificite if semaine == 1 else choose_specificite(weights, specificite)
                st.markdown(f"### Semaine {semaine} - {programme}")
                
                semaine_start = start_date + timedelta(weeks=semaine-1)
                semaine_end = semaine_start + timedelta(days=6)
                
                debut_fr = JOURS_TRADUCTION[semaine_start.strftime("%A")] + semaine_start.strftime(" %d/%m/%Y")
                fin_fr = JOURS_TRADUCTION[semaine_end.strftime("%A")] + semaine_end.strftime(" %d/%m/%Y")
                st.caption(f"Du {debut_fr} au {fin_fr}")
                
                #Génération programme
                resultat = programme_semaine_utilisateur(
                    choix=programme,
                    theme_principal=current_specificite,
                    nbr_seances=nbr_seances,
                    niveau=niveau
                )
                
                #separation du contenu par séance
                seances = [s for s in resultat.split('Jour ') if s.strip()][1:]  #partie vide
                
                # Traitement par jour
                for i, jour in enumerate(["LUNDI", "MARDI", "MERCREDI", "JEUDI", "VENDREDI", "SAMEDI", "DIMANCHE"]):
                    current_date = semaine_start + timedelta(days=i)
                    day_fr = JOURS_TRADUCTION[current_date.strftime("%A")]
                    date_str = f"{day_fr} {current_date.strftime('%d/%m/%Y')}"
                    
                    if jour in jours_match:
                        st.markdown(f"**{date_str} (jour de match)** ")
                        st.markdown(" *Pas de seance (match prévu)*")
                        st.markdown("_____________________")
                    elif jour in jours_disponibles:
                        jour_num = jours_disponibles.index(jour)
                        if jour_num < len(seances):
                            st.markdown(f"**{date_str}**")
                            # Afficher le contenu complet de la séance
                            display_seance(seances[jour_num].split('\n', 1)[1])
if __name__ == "__main__":
    main()
