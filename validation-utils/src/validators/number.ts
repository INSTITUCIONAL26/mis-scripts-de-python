export function es_numero(valor: unknown): boolean {
  if (valor === null || valor === undefined) return false;
  const n = Number(String(valor).trim());
  return typeof n === "number" && Number.isFinite(n);
}

export function es_entero(valor: unknown): boolean {
  if (!es_numero(valor)) return false;
  return Number.isInteger(Number(String(valor).trim()));
}

export function es_float(valor: unknown): boolean {
  if (!es_numero(valor)) return false;
  const n = Number(String(valor).trim());
  return !Number.isInteger(n);
}

export function esta_en_rango(numero: unknown, minimo: number, maximo: number): boolean {
  if (!es_numero(numero)) return false;
  const n = Number(String(numero).trim());
  return n >= minimo && n <= maximo;
}

export function es_positivo(numero: unknown): boolean {
  if (!es_numero(numero)) return false;
  return Number(String(numero).trim()) > 0;
}
