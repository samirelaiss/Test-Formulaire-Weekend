Fonctionnalité: Validation du formulaire de réservation week-end

  Scenario: Soumission valide avec email
    Étant donné que je suis sur la page du formulaire
    Quand je remplis le champ "Nom" avec "Tester_QA"
    Et je remplis le champ "Prénom" avec "Automation"
    Et je sélectionne "Lyon" dans la liste des villes
    Et je remplis le champ "Email" avec "qa.tester@example.org"
    Et je clique sur le bouton "Envoyer"
    Alors je vois le message "Merci pour vos informations"
    Et le formulaire disparaît

  Scenario: Soumission valide avec téléphone
    Étant donné que je suis sur la page du formulaire
    Quand je remplis le champ "Nom" avec "Test_Perf"
    Et je remplis le champ "Prénom" avec "Load_Runner"
    Et je sélectionne "Marseille" dans la liste des villes
    Et je remplis le champ "Téléphone" avec "0698765432"
    Et je clique sur le bouton "Envoyer"
    Alors je vois le message de confirmation
    Et le formulaire disparaît

  Scenario: Soumission invalide - champs manquants
    Étant donné que je suis sur la page du formulaire
    Quand je remplis le champ "Nom" avec "Test_Error"
    Et je laisse le champ "Prénom" vide
    Et je clique sur le bouton "Envoyer"
    Alors je vois le message d'erreur "Champ obligatoire"
    Et le formulaire reste visible

  Scenario: Chargement des villes
    Étant donné que la page du formulaire est chargée
    Alors la liste déroulante "Ville" contient au moins 10 villes
    Et les villes sont triées par ordre décroissant de population
    Et "Paris" apparaît en première position

  Scenario: Protection contre XSS
    Étant donné que je suis sur la page du formulaire
    Quand je remplis le champ "Nom" avec "<script>alert('attack')</script>"
    Et je remplis les autres champs obligatoires :
      | Prénom    | Security_Test |
      | Ville     | Nice          |
      | Email     | safe@example.org |
    Et je clique sur "Envoyer"
    Alors le script ne s'exécute pas
    Et je vois le message de confirmation normal
