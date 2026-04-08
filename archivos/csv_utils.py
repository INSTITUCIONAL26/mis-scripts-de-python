"""Utilidades para leer/escribir CSV de forma simple."""

import csv


def leer_csv(path, encoding='utf-8'):
    with open(path, newline='', encoding=encoding) as f:
        reader = csv.DictReader(f)
        return list(reader)


def escribir_csv(path, rows, fieldnames, encoding='utf-8'):
    with open(path, 'w', newline='', encoding=encoding) as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
