# Test Technique QA - Formulaire Week-end

## Contexte
Test automatisé d'un formulaire de destination week-end avec validation métier et intégration API géographique.

Technologies : Python, Selenium, Pytest  
Approche : Page Object Pattern, tests paramétrés, priorisation business  

## Installation et Exécution

### Prérequis
- Python 3.8+
- Chrome/Chromium installé
- Fichier `ceWeekEnd.html` dans le répertoire racine

### Installation
```bash
git clone https://github.com/samirelaiss/test-formulaire-weekend.git
cd test_formulaire_weekend
pip install -r requirements.txt
```

### Exécution des tests
```bash
# Tous les tests
pytest -v

# Tests priorité 1 uniquement  
pytest tests/test_formulaire_core.py -v

# Tests de sécurité
pytest tests/test_formulaire_core.py::TestFormulaireCore::test_xss_protection -v

# Tests avec rapport HTML
pytest --html=report.html --self-contained-html

# Avec logging détaillé
pytest -v | tee test_execution.log
```

### Techniques
- Gestion robuste des chemins : Utilisation de `os.path` pour une meilleure portabilité
- Journalisation détaillée : Logging complet pour le débogage
- Test de sécurité XSS : Vérification de la protection contre les injections
- Gestion des erreurs API : Tests pour les cas d'indisponibilité de l'API
- Validation des formats : Tests paramétrés pour email/téléphone

## Stratégie de Test

### Priorisation (2h max)
1. Priorité 1 : 
   - Validation formulaire
   - Règles métier critiques
   - Tests de sécurité XSS

2. Priorité 2 : 
   - Intégration API
   - Fonctionnalités UI
   - Gestion des erreurs

3. Documentation : 
   - README et structure
   - Logging des tests


## Architecture

```
test-formulaire-weekend/
├── tests/                   
│   ├── test_formulaire_core.py     # Tests critiques + sécurité
│   └── test_api_integration.py     # Tests API avec gestion erreurs
├── pages/                   
│   └── formulaire_page.py          # PO avec logging intégré
├── features/                
│   └── formulaire_weekend.feature
├── conftest.py             # Configuration pytest + logging
├── requirements.txt        
└── README.md              
```


## Résultats

Métriques :
- 8 tests automatisés
- ~90% de couverture fonctionnelle
- Logs complets dans `test_execution.log`

Points forts :
- Monitoring via système de logging
- Documentation technique complète

## Prochaines améliorations possibles
- Tests multi-navigateurs
- Validation des formats email/téléphone côté client
- Tests de performance (load time)
- Intégration continue (GitHub Actions)

---
Développé par : Samir EL AISSAOUY
Date : 07/07/2025
```
