import pytest
from pages.formulaire_page import FormulairePage

class TestDonneesValides:
    """Tests des cas nominaux avec données valides"""
    
    @pytest.mark.smoke
    def test_soumission_email_valide(self, setup_driver):
        """
        Test que le formulaire accepte un email valide
        - Remplit tous les champs requis
        - Vérifie la confirmation
        """
        # Arrange
        page = FormulairePage(setup_driver)
        test_data = {
            "nom": "EndToEnd_User",
            "prenom": "Test_Flow",
            "ville_index": 1,
            "email": "e2e@validation.test"
        }
        
        # Act
        page.remplir_champ(page.NOM_INPUT, test_data["nom"])
        page.remplir_champ(page.PRENOM_INPUT, test_data["prenom"])
        page.select_ville_par_index(test_data["ville_index"])
        page.remplir_champ(page.EMAIL_INPUT, test_data["email"])
        page.soumettre_formulaire()
        
        # Assert
        assert "Merci" in page.get_message_confirmation()

class TestValidations:
    """Tests des règles de validation métier"""
    
    @pytest.mark.parametrize("email,tel,attendu", [
        ("test@example.org", "", True),  # Email seul
        ("", "0612345678", True),  # Téléphone seul
        ("", "", False)  # Aucun contact
    ])
    def test_validation_contact(self, setup_driver, email, tel, attendu):
        """
        Test paramétré des règles de contact obligatoire
        Args:
            email: Valeur à tester (string vide si non fourni)
            tel: Valeur à tester (string vide si non fourni)
            attendu: Résultat booléen attendu
        """
        # Configuration du test
        page = FormulairePage(setup_driver)
        
        # Execution
        if email:
            page.remplir_champ(page.EMAIL_INPUT, email)
        if tel:
            page.remplir_champ(page.TEL_INPUT, tel)
        page.soumettre_formulaire()
        
        # Vérification
        resultat = "Merci" in page.get_message_confirmation()
        assert resultat == attendu
