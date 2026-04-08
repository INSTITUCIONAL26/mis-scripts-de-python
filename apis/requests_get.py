"""Funciones simples para peticiones GET usando requests."""

import requests


def fetch_json(url, timeout=10):
    """Devuelve un dict con la respuesta JSON o None en error."""
    try:
        r = requests.get(url, timeout=timeout)
        r.raise_for_status()
        return r.json()
    except Exception:
        return None
