from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

class FormulairePage:
    """
    Page Object Model (POM) pour le formulaire week-end
    Centralise tous les locators et interactions
    """
    
    # Locators avec commentaires explicites
    NOM_INPUT = (By.ID, "nom")  # Champ input nom
    PRENOM_INPUT = (By.ID, "prenom")  # Champ input prénom
    VILLE_SELECT = (By.ID, "ville")  # Dropdown des villes
    EMAIL_INPUT = (By.ID, "email")  # Champ email
    TEL_INPUT = (By.ID, "telephone")  # Champ téléphone
    SUBMIT_BTN = (By.CSS_SELECTOR, "button[type='submit']")  # Bouton d'envoi
    MODAL_MSG = (By.ID, "modal-content")  # Message de confirmation/erreur

    def __init__(self, driver):
        """Initialise avec le WebDriver et configure les waits"""
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Wait explicite de 10s

    def remplir_champ(self, locator, valeur):
        """
        Remplit un champ générique avec vérification
        Args:
            locator: Tuple (By, selector)
            valeur: Texte à saisir
        """
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.clear()
        element.send_keys(valeur)

    def select_ville_par_index(self, index):
        """
        Sélectionne une ville dans le dropdown
        Args:
            index: Position dans la liste (1-based)
        """
        Select(self.driver.find_element(*self.VILLE_SELECT)).select_by_index(index)

    def soumettre_formulaire(self):
        """Clique sur le bouton de soumission et attend la réponse"""
        self.driver.find_element(*self.SUBMIT_BTN).click()
        self.wait.until(EC.visibility_of_element_located(self.MODAL_MSG))

    def get_message_confirmation(self):
        """Récupère le texte de confirmation après soumission"""
        return self.driver.find_element(*self.MODAL_MSG).text
