# Test Technique QA - Formulaire Week-end

## Contexte
Test automatisé d'un formulaire de destination week-end avec validation métier et intégration API géographique.

**Technologies** : Python, Selenium, Pytest  
**Approche** : Page Object Pattern, tests paramétrés  

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

# Tests avec rapport HTML
pytest --html=report.html --self-contained-html
```

## Stratégie de Test

### Priorisation 
1. **Priorité 1** :  
   - Validation formulaire  
   - Règles métier critiques  

2. **Priorité 2** :  
   - Intégration API  
   - Fonctionnalités UI  

3. **Documentation** :  
   - README et structure projet  

## Architecture

```
test-formulaire-weekend/
├── tests/                   
│   ├── test_formulaire_core.py     # Tests principaux
│   └── test_api_integration.py     # Tests API
├── pages/                   
│   └── formulaire_page.py          # Page Object
├── conftest.py             # Configuration pytest
├── tests_gherkin.txt
├── requirements.txt        
└── README.md              
```

## Résultats

**Métriques** :
- 6 tests automatisés  
- Couverture des cas critiques  

**Points forts** :
- Architecture modulaire  
- Tests paramétrés  
- Intégration API géographique  

## Prochaines améliorations possibles
- Tests multi-navigateurs  
- Intégration continue  
- Validation des formats de saisie  

---
**Développé par** : Samir EL AISSAOUY  
**Date** : 07/07/2025  
```
