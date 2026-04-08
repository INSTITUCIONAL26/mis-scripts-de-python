export function normalizeString(input: string): string {
    return input
        .trim() // Elimina espacios al inicio y al final
        .replace(/[^a-zA-Z0-9 ]/g, '') // Elimina caracteres especiales
        .replace(/\s+/g, ' '); // Reemplaza múltiples espacios por uno solo
}