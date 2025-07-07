"""
Fonctionnalité: Formulaire de réservation week-end
Critère métier principal : 
Le système doit valider que chaque soumission contient 
soit un email valide, soit un numéro de téléphone valide
"""

# Scénario principal - Chemin heureux
Scenario: Soumission valide avec email professionnel
    Given Je suis sur la page du formulaire
    # Données de test génériques respectant RFC 2606
    When Je remplis le champ "Nom" avec "QA_Engineer"
    And Je remplis le champ "Prénom" avec "Test_Auto"
    And Je sélectionne la première ville disponible
    And Je remplis le champ "Email" avec "automation@example.org"
    And Je clique sur "Envoyer"
    Then Je vois la confirmation "Merci pour vos informations"

# Scénario alternatif
Scenario: Soumission avec téléphone uniquement
    Given Je suis sur la page du formulaire
    # Numéro fictif respectant le format français
    When Je remplis le champ "Téléphone" avec "0612345678"
    And Je remplis les autres champs obligatoires
    And Je clique sur "Envoyer"
    Then Le système accepte la soumission

# Scénario d'erreur
Scenario: Rejet si aucun contact fourni
    Given Je remplis tous les champs sauf email et téléphone
    When Je tente de soumettre le formulaire
    Then Je vois l'erreur "Contact obligatoire"
    And Le formulaire n'est pas masqué
