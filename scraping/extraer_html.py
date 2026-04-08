"""Funciones de scraping con BeautifulSoup como ejemplo."""

from bs4 import BeautifulSoup


def extraer_titulos(html):
    """Devuelve una lista de textos de elementos <h1> encontrados."""
    soup = BeautifulSoup(html, 'html.parser')
    return [h.get_text(strip=True) for h in soup.find_all('h1')]
