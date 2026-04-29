"""PROGRAMA PARA ABRIR DIRECCIONES WEB EN DIFERENTES PESTAÑA DEL NAVEGADOR EN MODO INCOGNITO

"""

import webbrowser

# 1. Configuramos la ruta de Chrome con el parámetro de incógnito
# El '%s' es un espacio vacío donde Python pondrá cada URL después
ruta_chrome = "C:/Program Files/Google/Chrome/Application/chrome.exe --incognito %s"

# 2. Registramos este comportamiento en Python
# Le damos un nombre corto como 'chrome_incognito'
webbrowser.register("chrome_incognito", None, webbrowser.BackgroundBrowser("C:/Program Files/Google/Chrome/Application/chrome.exe"))

archivos_urls = "links.txt"

try:
    with open(archivos_urls, "r") as archivo:
        for Linea in archivo:
            url = Linea.strip()
            if url:
                print(f"Abriendo en incognito: {url}")
                # 3. Usamos el navegador que registramos arriba
                webbrowser.get("chrome_incognito").open_new_tab(url)
except FileNotFoundError:
    print("Error : el archivo links.txt no existe en la carpeta.")            



# NOTA Ejecútalo desde tu terminal GitBash con: python nombre_de_tu_archivo.py
