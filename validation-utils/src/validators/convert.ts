export function convertir_a_entero(valor: unknown): number | null {
  if (valor === null || valor === undefined) return null;
  const n = parseInt(String(valor).trim(), 10);
  return Number.isNaN(n) ? null : n;
}

export function convertir_a_float(valor: unknown): number | null {
  if (valor === null || valor === undefined) return null;
  const f = parseFloat(String(valor).trim());
  return Number.isNaN(f) ? null : f;
}
