
import webbrowser

# 1. Definimos la ruta donde está instalado Firefox en tu Windows
# Usamos el parámetro '-new-tab' para forzar que cada URL sea una pestaña
ruta_firefox = "C:/Program Files/Mozilla Firefox/firefox.exe"

# 2. Registramos Firefox en Python
# Le ponemos un apodo, por ejemplo: 'zorro'
webbrowser.register('zorro', None, webbrowser.BackgroundBrowser(ruta_firefox))

archivo_urls = "links.txt"

try:
    with open(archivo_urls, "r") as archivo:
        for linea in archivo:
            url = linea.strip()
            if url:
                print(f"Mandando a Firefox: {url}")
                # 3. Usamos nuestro apodo 'zorro' para abrir la pestaña
                webbrowser.get('zorro').open_new_tab(url)
except FileNotFoundError:
    print("El archivo links.txt no se encuentra. ¡Revisa tu carpeta de trabajo!")