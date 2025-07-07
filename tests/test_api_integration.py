import pytest
import requests
from pages.formulaire_page import FormulairePage
from requests.exceptions import RequestException

class TestAPIIntegration:
    """Tests d'intégration avec l'API geo.gouv.fr"""
    
    def test_api_geo_accessible(self):
        """Test que l'API géographique répond correctement"""
        url = "https://geo.api.gouv.fr/departements/59/communes"
        params = {"fields": "nom", "format": "json"}
        
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        
        data = response.json()
        assert len(data) > 0, "L'API ne retourne aucune donnée"
        assert any(ville["nom"] == "Lille" for ville in data), "Lille manquante dans les résultats"
    
    def test_villes_chargees_dans_select(self, formulaire_page):
        """Test que les villes sont chargées dans le formulaire"""
        page = FormulairePage(formulaire_page)
        villes = page.get_villes_list()
        
        assert len(villes) > 0, "Aucune ville chargée dans le select"
        assert "Lille" in villes, "Ville principale manquante"
