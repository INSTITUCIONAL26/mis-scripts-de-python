export function es_url(texto: unknown): boolean {
  if (typeof texto !== "string") return false;
  try {
    const u = new URL(texto);
    return ["http:", "https:"].includes(u.protocol);
  } catch {
    return false;
  }
}

export function es_telefono(texto: unknown): boolean {
  if (typeof texto !== "string") return false;
  const clean = texto.replace(/[\s-()+.]/g, "");
  return /^\d{9,15}$/.test(clean);
}

export function es_codigo_postal(texto: unknown): boolean {
  if (typeof texto !== "string") return false;
  const clean = texto.trim();
  return /^\d{4,6}$/.test(clean);
}

export function es_uuid(texto: unknown): boolean {
  if (typeof texto !== "string") return false;
  return /^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i.test(
    texto.trim()
  );
}

export function es_hex_color(texto: unknown): boolean {
  if (typeof texto !== "string") return false;
  return /^#?([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$/.test(texto.trim());
}

export function es_alfa(texto: unknown): boolean {
  if (typeof texto !== "string") return false;
  return /^[A-Za-zÃÃ‰ÃÃ“ÃšÃœÃ‘Ã¡Ã©Ã­Ã³ÃºÃ¼Ã±\s]+$/.test(texto.trim());
}

export function es_alfa_num(texto: unknown): boolean {
  if (typeof texto !== "string") return false;
  return /^[A-Za-z0-9ÃÃ‰ÃÃ“ÃšÃœÃ‘Ã¡Ã©Ã­Ã³ÃºÃ¼Ã±\s]+$/.test(texto.trim());
}

export function longitud_entre(texto: unknown, minimo: number, maximo: number): boolean {
  if (typeof texto !== "string") return false;
  const len = texto.length;
  return len >= minimo && len <= maximo;
}

export function matches_regex(texto: unknown, pattern: RegExp | string): boolean {
  if (typeof texto !== "string") return false;
  const re = typeof pattern === "string" ? new RegExp(pattern) : pattern;
  return re.test(texto);
}
