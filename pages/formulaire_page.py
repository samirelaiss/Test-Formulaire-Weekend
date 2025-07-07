from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

class FormulairePage:
    """Page Object pour le formulaire week-end"""
    
    # Locators
    NOM = (By.ID, "nom")
    PRENOM = (By.ID, "prenom")
    VILLE = (By.ID, "ville")
    EMAIL = (By.ID, "email")
    TELEPHONE = (By.ID, "telephone")
    SUBMIT = (By.CSS_SELECTOR, "button[type='submit']")
    MODAL = (By.ID, "myModal")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def remplir_formulaire(self, nom, prenom, ville_index, email="", telephone=""):
        self.set_nom(nom)
        self.set_prenom(prenom)
        self.select_ville(ville_index)
        if email:
            self.set_email(email)
        if telephone:
            self.set_telephone(telephone)
        self.submit()

    def set_nom(self, valeur):
        self.driver.find_element(*self.NOM).send_keys(valeur)

    def set_prenom(self, valeur):
        self.driver.find_element(*self.PRENOM).send_keys(valeur)

    def select_ville(self, index):
        Select(self.driver.find_element(*self.VILLE)).select_by_index(index)

    def set_email(self, valeur):
        self.driver.find_element(*self.EMAIL).send_keys(valeur)

    def set_telephone(self, valeur):
        self.driver.find_element(*self.TELEPHONE).send_keys(valeur)

    def submit(self):
        self.driver.find_element(*self.SUBMIT).click()

    def get_modal_text(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.MODAL)
        ).text
    def get_villes_list(self):
    """Récupère la liste des villes depuis le dropdown"""
    select = Select(self.driver.find_element(*self.VILLE_SELECT))
    return [option.text for option in select.options if option.text.strip()]
