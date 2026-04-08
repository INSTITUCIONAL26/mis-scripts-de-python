export function es_dni(texto: unknown): boolean {
  if (typeof texto !== 'string') return false;
  const t = texto.trim().toUpperCase();
  const clean = t.replace(/[^A-Z0-9]/g, '');
  const letras = 'TRWAGMYFPDXBNJZSQVHLCKE';

  const dniMatch = clean.match(/^(\d{8})([A-Z])$/);
  if (dniMatch) {
    const num = parseInt(dniMatch[1], 10);
    const letra = dniMatch[2];
    return letras[num % 23] === letra;
  }

  const nieMatch = clean.match(/^([XYZ])(\d{7})([A-Z])$/);
  if (nieMatch) {
    const pref = nieMatch[1] === 'X' ? '0' : nieMatch[1] === 'Y' ? '1' : '2';
    const num = parseInt(pref + nieMatch[2], 10);
    const letra = nieMatch[3];
    return letras[num % 23] === letra;
  }

  const nifMatch = clean.match(/^([A-W])(\d{7})([0-9A-J])$/);
  if (nifMatch) return true;

  return false;
}
