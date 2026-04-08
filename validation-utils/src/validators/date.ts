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
