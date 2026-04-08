"""Punto de entrada del proyecto - ejemplo de uso de los módulos."""

from apis.requests_get import fetch_json
from scraping.extraer_html import extraer_titulos


def main():
    print("Proyecto: mis-scripts-de-python")
    # ejemplo mínimo (no ejecuta nada por defecto)
    print("Módulos disponibles: apis, scraping, archivos, utilidades")


if __name__ == '__main__':
    main()
