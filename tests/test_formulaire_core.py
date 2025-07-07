import pytest
from pages.formulaire_page import FormulairePage

class TestFormulaireCore:
    """Tests critiques du formulaire"""
    
    def test_soumission_valide_email(self, formulaire_page):
        """Test avec email valide"""
        page = FormulairePage(formulaire_page)
        page.remplir_formulaire(
            nom="TestUser",
            prenom="Valid",
            ville_index=1,
            email="test@example.org"
        )
        assert "Merci" in page.get_modal_text()

    def test_soumission_valide_telephone(self, formulaire_page):
        """Test avec téléphone valide"""
        page = FormulairePage(formulaire_page)
        page.remplir_formulaire(
            nom="TestUser",
            prenom="Valid",
            ville_index=1,
            telephone="0612345678"
        )
        assert "Merci" in page.get_modal_text()

    def test_soumission_invalide(self, formulaire_page):
        """Test sans contact"""
        page = FormulairePage(formulaire_page)
        page.remplir_formulaire(
            nom="TestUser",
            prenom="Invalid",
            ville_index=1
        )
        assert "Veuillez remplir" in page.get_modal_text()
