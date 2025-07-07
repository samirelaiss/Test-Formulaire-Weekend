import pytest
import requests
from pages.formulaire_page import FormulairePage
from requests.exceptions import RequestException

class TestAPIIntegration:
    """Tests d'intégration avec l'API geo.gouv.fr - Priorité 2"""
    
    def test_api_geo_accessible(self):
        """Test : API géographique répond correctement"""
        try:
            url = "https://geo.api.gouv.fr/departements/59/communes"
            params = {"fields": "nom,code,population", "format": "json"}
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            assert len(data) > 0
            assert "Lille" in [ville["nom"] for ville in data]
            
        except RequestException as e:
            pytest.fail(f"L'API géographique est inaccessible: {str(e)}")
    
    def test_villes_chargees_dans_select(self, formulaire_page):
        """Test : Villes correctement chargées dans le select"""
        page = FormulairePage(formulaire_page) 
        page.wait_for_page_load()
        
        villes = page.get_villes_list()
        
        assert len(villes) > 10
        assert "Lille" in villes
        
        # Vérifier tri par population (Lille en premier)
        assert villes[0] == "Lille"
    
    def test_api_indisponible(self, mocker):
        """Test : Comportement quand l'API est indisponible"""
        # Simuler une erreur de l'API
        mocker.patch('requests.get', side_effect=RequestException("API down"))
        
        with pytest.raises(RequestException):
            url = "https://geo.api.gouv.fr/departements/59/communes"
            requests.get(url)
