from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Configurar opciones de Chrome
chrome_options = Options()
chrome_options.add_argument("--incognito")  # <--- Habilita el modo incógnito

# Inicializar el driver con las opciones
driver = webdriver.Chrome(options=chrome_options)

# Abrir una página web
driver.get("https://www.google.com")