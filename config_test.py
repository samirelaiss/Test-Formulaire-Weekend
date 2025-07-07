import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="module")
def setup_driver():
    """
    Fixture principale - Gère le cycle de vie du WebDriver
    - Installe automatiquement ChromeDriver
    - Configure les options pour les tests
    - Nettoie après les tests
    """
    # Configuration
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Exécution sans UI
    options.add_argument("--no-sandbox")
    
    # Initialisation
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(5)  # Wait implicite de secours
    
    yield driver  # Point d'exécution des tests
    
    # Nettoyage
    driver.quit()
