Set-Location -LiteralPath 'C:\Users\MARCOGALU\OneDrive\Desktop\portafolio_scrips'

# Crear carpetas
New-Item -ItemType Directory -Path validation-utils\src\validators -Force | Out-Null

# dni.ts
@'
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
'@ | Set-Content -Path .\validation-utils\src\validators\dni.ts -Encoding utf8

# email.ts
@'
export function es_email(texto: unknown): boolean {
  if (typeof texto !== 'string') return false;
  const t = texto.trim();
  const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return re.test(t);
}
'@ | Set-Content -Path .\validation-utils\src\validators\email.ts -Encoding utf8

# number.ts
@'
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
'@ | Set-Content -Path .\validation-utils\src\validators\number.ts -Encoding utf8

# convert.ts
@'
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
'@ | Set-Content -Path .\validation-utils\src\validators\convert.ts -Encoding utf8

# date.ts
@'
export function es_fecha(texto: unknown): boolean {
  if (typeof texto !== "string") return false;
  const t = texto.trim();
  const iso = /^\d{4}-\d{2}-\d{2}$/;
  const dmy = /^\d{2}\/\d{2}\/\d{4}$/;

  let date: Date | null = null;
  if (iso.test(t)) {
    date = new Date(t);
  } else if (dmy.test(t)) {
    const [dd, mm, yyyy] = t.split("/").map(Number);
    date = new Date(yyyy, mm - 1, dd);
  } else {
    return false;
  }

  if (!(date instanceof Date) || Number.isNaN(date.getTime())) return false;

  const year = date.getFullYear();
  const month = date.getMonth() + 1;
  const day = date.getDate();

  if (iso.test(t)) {
    const [y, m, d] = t.split("-").map(Number);
    return year === y && month === m && day === d;
  } else {
    const [dStr, mStr, yStr] = t.split("/");
    return year === Number(yStr) && month === Number(mStr) && day === Number(dStr);
  }
}
'@ | Set-Content -Path .\validation-utils\src\validators\date.ts -Encoding utf8

# misc.ts
@'
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
  return /^[A-Za-zÁÉÍÓÚÜÑáéíóúüñ\s]+$/.test(texto.trim());
}

export function es_alfa_num(texto: unknown): boolean {
  if (typeof texto !== "string") return false;
  return /^[A-Za-z0-9ÁÉÍÓÚÜÑáéíóúüñ\s]+$/.test(texto.trim());
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
'@ | Set-Content -Path .\validation-utils\src\validators\misc.ts -Encoding utf8

# validators index
@'
export * from "./dni";
export * from "./email";
export * from "./number";
export * from "./convert";
export * from "./date";
export * from "./misc";
'@ | Set-Content -Path .\validation-utils\src\validators\index.ts -Encoding utf8

# src index
@'
import * as v from "./validators";
export default v;

if ((require as any).main === module) {
  console.log("es_dni 12345678Z ->", v.es_dni("12345678Z"));
  console.log("es_email a@b.com ->", v.es_email("a@b.com"));
  console.log("es_fecha 31/12/2020 ->", v.es_fecha("31/12/2020"));
  console.log("es_numero \"5.5\" ->", v.es_numero("5.5"));
}
'@ | Set-Content -Path .\validation-utils\src\index.ts -Encoding utf8

# Git: add, commit, push
git add validation-utils
git commit -m "Add validation-utils: full set of validators" 2>$null
git push -u origin main