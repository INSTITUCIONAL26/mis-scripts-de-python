export function es_email(texto: unknown): boolean {
  if (typeof texto !== 'string') return false;
  const t = texto.trim();
  const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return re.test(t);
}
